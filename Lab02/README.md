# Lab02 - Crawler simples

Objetivo: navegar por páginas web e extrair título e links, respeitando robots.txt, delay entre pedidos e User-Agent.

## Como executar

Instalar dependências:

```bash
pip install -r requirements.txt
```

```bash
python crawler.py https://example.com 3 --output saida.json
```

Para filtrar apenas links do mesmo domínio (bónus):

```bash
python crawler.py https://example.com 3 --mesmo-dominio
```

Para extrair também `h1`, `h2` e `p` (bónus):

```bash
python crawler.py https://example.com 3 --extrair-texto
```

## Saída

O ficheiro JSON tem o formato:

```json
[
  {
    "url": "https://example.com",
    "titulo": "Example Domain",
    "links": ["https://www.iana.org/domains/example"]
  }
]
```

## Perguntas de reflexão

1. Respeitar o robots.txt é importante porque define regras do próprio site sobre o que pode ou não ser acedido por crawlers, reduz risco de abuso e evita violar políticas.
2. Um crawler mal implementado pode sobrecarregar servidores, causar bloqueios (IP ban), recolher dados indevidos, gerar custos e até criar problemas legais/éticos.
3. Crawling é descobrir/navegar páginas (seguir links e mapear). Scraping é extrair dados de páginas (conteúdo estruturado) depois de as obter.
