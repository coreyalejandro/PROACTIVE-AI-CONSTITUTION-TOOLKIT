from __future__ import annotations

import argparse
import json
from pathlib import Path


def must_exist(path: Path) -> None:
    if not path.exists():
        raise SystemExit(f"MISSING: {path}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--adapter-dir', required=True)
    ap.add_argument('--min-instances', type=int, default=100)
    args = ap.parse_args()

    adapter_dir = Path(args.adapter_dir)

    must_exist(adapter_dir / 'USE_CASE_EVIDENCE.md')
    must_exist(adapter_dir / 'validation_results.json')
    must_exist(adapter_dir / 'evidence' / 'run.log')
    must_exist(adapter_dir / 'evidence' / 'manifest.sha256')
    must_exist(adapter_dir / 'evidence' / 'env.json')

    data = json.loads((adapter_dir / 'validation_results.json').read_text(encoding='utf-8'))
    n_base = data.get('n_instances', {}).get('baseline', 0)
    n_pro = data.get('n_instances', {}).get('proactive', 0)
    if n_base < args.min_instances or n_pro < args.min_instances:
        raise SystemExit(f"INSUFFICIENT_INSTANCES: baseline={n_base} proactive={n_pro} min={args.min_instances}")

    # Require a p-value + effect size
    stats = data.get('stats', {})
    if 'p_value_bootstrap' not in stats:
        raise SystemExit('MISSING_STATS: p_value_bootstrap')
    if 'cohens_d_safe_truthfulness' not in stats:
        raise SystemExit('MISSING_STATS: cohens_d_safe_truthfulness')

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
