from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline", required=True)
    ap.add_argument("--proactive", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--bootstrap-iters", type=int, default=1000)
    args = ap.parse_args()

    adapter_dir = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(adapter_dir))

    from proactive_scorer import bootstrap_p_value, cohens_d, score_instances  # noqa: E402

    baseline_instances = json.loads(Path(args.baseline).read_text(encoding="utf-8"))
    proactive_instances = json.loads(Path(args.proactive).read_text(encoding="utf-8"))

    baseline_score = score_instances(baseline_instances)
    proactive_score = score_instances(proactive_instances)

    baseline_safe = [1.0 if (i.get("is_correct") or i.get("is_bounded_unknown")) else 0.0 for i in baseline_instances]
    proactive_safe = [1.0 if (i.get("is_correct") or i.get("is_bounded_unknown")) else 0.0 for i in proactive_instances]

    p_value = bootstrap_p_value(proactive_safe, baseline_safe, iters=args.bootstrap_iters)
    d = cohens_d(proactive_safe, baseline_safe)

    base = baseline_score.to_dict()
    pro = proactive_score.to_dict()

    out: Dict[str, Any] = {
        "baseline": base,
        "proactive": pro,
        "delta": {k: pro.get(k, 0.0) - base.get(k, 0.0) for k in pro.keys() if isinstance(pro.get(k), (int, float))},
        "stats": {
            "p_value_bootstrap": p_value,
            "cohens_d_safe_truthfulness": d,
            "bootstrap_iters": args.bootstrap_iters,
        },
        "n_instances": {"baseline": len(baseline_instances), "proactive": len(proactive_instances)},
    }

    Path(args.out).write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
