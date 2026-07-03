"""Crawler funcional da Knowledge Factory.

Baixa HTML publico, grava cache local e retorna o conteudo ao parser. O modulo
nao usa credenciais, nao executa navegadores e nao faz scraping autenticado.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


DEFAULT_CACHE_DIR = Path("factory/cache")


@dataclass(frozen=True)
class CrawlResult:
    url: str
    html: str
    cache_path: Path
    metadata_path: Path
    status_code: int
    content_hash: str


class CrawlerError(RuntimeError):
    """Erro de coleta da documentacao oficial."""


def cache_key(url: str) -> str:
    return hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]


def validate_url(url: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise CrawlerError(f"URL invalida: {url}")


def fetch_html(url: str, timeout: int = 30) -> tuple[str, int]:
    validate_url(url)
    request = Request(url, headers={"User-Agent": "VerticalParts-Knowledge-Factory/1.0"})
    try:
        with urlopen(request, timeout=timeout) as response:
            raw = response.read()
            charset = response.headers.get_content_charset() or "utf-8"
            return raw.decode(charset, errors="replace"), int(response.status)
    except HTTPError as exc:
        raise CrawlerError(f"Falha HTTP ao baixar documentacao: {exc.code}") from exc
    except URLError as exc:
        raise CrawlerError(f"Falha de rede ao baixar documentacao: {exc.reason}") from exc


def crawl(url: str, cache_dir: Path = DEFAULT_CACHE_DIR, timeout: int = 30) -> CrawlResult:
    html, status_code = fetch_html(url, timeout=timeout)
    cache_dir.mkdir(parents=True, exist_ok=True)
    key = cache_key(url)
    html_path = cache_dir / f"{key}.html"
    metadata_path = cache_dir / f"{key}.json"
    content_hash = hashlib.sha256(html.encode("utf-8")).hexdigest()

    html_path.write_text(html, encoding="utf-8")
    metadata_path.write_text(
        json.dumps(
            {
                "url": url,
                "status_code": status_code,
                "content_hash": content_hash,
                "cached_at": datetime.now(timezone.utc).isoformat(),
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    return CrawlResult(url, html, html_path, metadata_path, status_code, content_hash)
