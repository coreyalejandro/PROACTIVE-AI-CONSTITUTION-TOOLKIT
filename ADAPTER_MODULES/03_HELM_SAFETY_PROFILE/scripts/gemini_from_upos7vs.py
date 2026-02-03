from __future__ import annotations

import argparse
import json
import os
import sys
import ssl
import urllib.request
from urllib.error import HTTPError, URLError
import random
import time

import certifi
from pathlib import Path


def load_upos7vs_gemini_key(config_path: Path) -> str:
    data = json.loads(config_path.read_text(encoding="utf-8"))
    key = (
        data.get("providers", {})
        .get("gemini", {})
        .get("apiKey")
    )
    if not isinstance(key, str) or not key.strip():
        raise SystemExit(
            f"Gemini API key not found in {config_path} at providers.gemini.apiKey"
        )
    return key.strip()


def call_gemini(api_key: str, model: str, prompt: str, timeout_s: int, max_retries: int) -> str:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    body = {"contents": [{"role": "user", "parts": [{"text": prompt}]}]}

    ssl_context = ssl.create_default_context(cafile=certifi.where())

    for attempt in range(max_retries + 1):
        req = urllib.request.Request(
            url,
            data=json.dumps(body).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=timeout_s, context=ssl_context) as resp:
                data = json.loads(resp.read().decode("utf-8"))

            parts = data["candidates"][0]["content"]["parts"]
            texts = [p.get("text", "") for p in parts if isinstance(p, dict)]
            return "".join(texts).strip()
        except HTTPError as e:
            status = getattr(e, 'code', None)
            if status in (429, 500, 502, 503, 504) and attempt < max_retries:
                retry_after = e.headers.get('Retry-After') if getattr(e, 'headers', None) else None
                if retry_after:
                    try:
                        sleep_s = float(retry_after)
                    except ValueError:
                        sleep_s = 1.0
                else:
                    sleep_s = min(60.0, (2 ** attempt))
                sleep_s += random.uniform(0.0, 0.25)
                time.sleep(sleep_s)
                continue
            raise
        except URLError as e:
            if attempt < max_retries:
                sleep_s = min(60.0, (2 ** attempt)) + random.uniform(0.0, 0.25)
                time.sleep(sleep_s)
                continue
            raise

    raise SystemExit('Failed to call Gemini after retries')



def main() -> int:
    ap = argparse.ArgumentParser(
        description="Reads prompt from stdin, calls Gemini using UPOS7VS stored key, prints response to stdout."
    )
    ap.add_argument(
        "--model",
        default="gemini-2.0-flash",
        help="Gemini model name (e.g. gemini-2.0-flash, gemini-1.5-pro, gemini-1.5-flash)",
    )
    ap.add_argument(
        "--timeout-s",
        type=int,
        default=30,
        help="HTTP timeout seconds per request",
    )
    ap.add_argument(
        "--max-retries",
        type=int,
        default=3,
        help="Retries for 429/5xx responses (keep low to avoid long waits)",
    )
    ap.add_argument(
        "--min-delay-ms",
        type=int,
        default=250,
        help="Sleep this many ms before each API call (rate limit protection)",
    )
    ap.add_argument(
        "--config",
        default=str(Path.home() / ".upos7vs" / "config" / "config.json"),
        help="Path to UPOS7VS config.json",
    )

    args = ap.parse_args()

    prompt = sys.stdin.read()
    if not prompt.strip():
        return 0

    config_path = Path(args.config).expanduser()
    api_key = load_upos7vs_gemini_key(config_path)

    time.sleep(max(0.0, args.min_delay_ms / 1000.0))

    text = call_gemini(api_key=api_key, model=args.model, prompt=prompt, timeout_s=args.timeout_s, max_retries=args.max_retries)
    sys.stdout.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
