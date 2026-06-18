import json
import time
from urllib.parse import urldefrag, urljoin, urlparse
from urllib.robotparser import RobotFileParser

import requests
from bs4 import BeautifulSoup


def _normalize_url(url):
    if not url:
        return None

    url = url.strip()
    if not url:
        return None

    url, _ = urldefrag(url)
    parsed = urlparse(url)

    if parsed.scheme and parsed.scheme not in ('http', 'https'):
        return None

    if parsed.scheme in ('http', 'https') and not parsed.netloc:
        return None

    return url


def _same_domain(url_a, url_b):
    return urlparse(url_a).netloc.lower() == urlparse(url_b).netloc.lower()


def _load_robots(url_inicial, user_agent, timeout_s):
    robots_url = urljoin(url_inicial, '/robots.txt')
    try:
        resp = requests.get(
            robots_url,
            headers={'User-Agent': user_agent},
            timeout=timeout_s,
        )
    except requests.RequestException:
        return None

    if resp.status_code == 404:
        return None

    if resp.status_code < 200 or resp.status_code >= 300:
        return None

    rp = RobotFileParser()
    rp.set_url(robots_url)
    rp.parse(resp.text.splitlines())
    return rp


def crawler(
    url_inicial,
    max_paginas,
    *,
    delay_s=1.0,
    user_agent='PAC2025SimpleCrawler/1.0',
    timeout_s=10,
    mesmo_dominio=False,
    extrair_texto=False,
    output_json='crawler_output.json',
):
    url_inicial = _normalize_url(url_inicial)
    if not url_inicial:
        raise ValueError('url_inicial invalida')

    if max_paginas <= 0:
        raise ValueError('max_paginas deve ser > 0')

    robots = _load_robots(url_inicial, user_agent, timeout_s)

    visitadas = set()
    fila = [url_inicial]
    resultados = []

    while fila and len(visitadas) < max_paginas:
        url = fila.pop(0)
        url = _normalize_url(url)
        if not url or url in visitadas:
            continue

        if robots and not robots.can_fetch(user_agent, url):
            visitadas.add(url)
            continue

        try:
            resp = requests.get(
                url,
                headers={'User-Agent': user_agent},
                timeout=timeout_s,
            )
        except requests.RequestException:
            visitadas.add(url)
            continue

        content_type = resp.headers.get('Content-Type', '')
        if 'text/html' not in content_type:
            visitadas.add(url)
            continue

        if resp.status_code < 200 or resp.status_code >= 300:
            visitadas.add(url)
            continue

        soup = BeautifulSoup(resp.text, 'html.parser')

        titulo = ''
        if soup.title and soup.title.get_text(strip=True):
            titulo = soup.title.get_text(strip=True)

        links_abs = []
        for a in soup.find_all('a', href=True):
            href = (a.get('href') or '').strip()
            if not href or href.startswith('#'):
                continue
            if href.startswith(('mailto:', 'javascript:', 'tel:')):
                continue

            abs_url = _normalize_url(urljoin(url, href))
            if not abs_url:
                continue

            if abs_url not in links_abs:
                links_abs.append(abs_url)

        item = {
            'url': url,
            'titulo': titulo,
            'links': links_abs,
        }

        if extrair_texto:
            item['h1'] = [h.get_text(' ', strip=True) for h in soup.find_all('h1')]
            item['h2'] = [h.get_text(' ', strip=True) for h in soup.find_all('h2')]
            item['p'] = [p.get_text(' ', strip=True) for p in soup.find_all('p')]

        resultados.append(item)
        visitadas.add(url)

        for l in links_abs:
            if mesmo_dominio and not _same_domain(url_inicial, l):
                continue
            if l not in visitadas and l not in fila:
                fila.append(l)

        if delay_s:
            time.sleep(delay_s)

    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)

    return resultados


def _main():
    import argparse

    p = argparse.ArgumentParser()
    p.add_argument('url_inicial')
    p.add_argument('max_paginas', type=int)
    p.add_argument('--delay', type=float, default=1.0)
    p.add_argument('--user-agent', default='PAC2025SimpleCrawler/1.0')
    p.add_argument('--timeout', type=int, default=10)
    p.add_argument('--mesmo-dominio', action='store_true', default=False)
    p.add_argument('--extrair-texto', action='store_true', default=False)
    p.add_argument('--output', default='crawler_output.json')
    args = p.parse_args()

    crawler(
        args.url_inicial,
        args.max_paginas,
        delay_s=args.delay,
        user_agent=args.user_agent,
        timeout_s=args.timeout,
        mesmo_dominio=args.mesmo_dominio,
        extrair_texto=args.extrair_texto,
        output_json=args.output,
    )


if __name__ == '__main__':
    _main()
