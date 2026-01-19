"""
Validation Analysis Script for W&B Trace Adapter

Usage: python analyze_validation.py <results.json>

Outputs:
- Summary statistics
- Statistical test results
- Threshold checks per EVALUATION_METHODOLOGY.md
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from statistics import mean, stdev

# Optional: uncomment when scipy is available
# from scipy import stats


@dataclass
class ValidationResults:
    """Container for validation study results."""
    
    condition: str
    times: List[float]  # Attribution times in minutes
    correct: List[bool]  # Attribution accuracy
    notes: Optional[List[str]] = None
    
    @property
    def mean_time(self) -> float:
        return mean(self.times) if self.times else 0.0
    
    @property
    def std_time(self) -> float:
        return stdev(self.times) if len(self.times) > 1 else 0.0
    
    @property
    def accuracy(self) -> float:
        return sum(self.correct) / len(self.correct) if self.correct else 0.0
    
    @property
    def n(self) -> int:
        return len(self.times)


def load_results(filepath: str) -> Dict[str, ValidationResults]:
    """Load validation results from JSON file.
    
    Expected format:
    {
        "baseline_a": {"times": [...], "correct": [...], "notes": [...]},
        "baseline_b": {"times": [...], "correct": [...], "notes": [...]},
        "treatment": {"times": [...], "correct": [...], "notes": [...]}
    }
    """
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    results = {}
    for condition, values in data.items():
        results[condition] = ValidationResults(
            condition=condition,
            times=values.get("times", []),
            correct=values.get("correct", []),
            notes=values.get("notes")
        )
    
    return results


def print_summary(results: Dict[str, ValidationResults]) -> None:
    """Print summary statistics table."""
    print("\n" + "=" * 50)
    print("ROOT CAUSE ATTRIBUTION TIME")
    print("=" * 50)
    print(f"{'Condition':<15} {'Mean (min)':<12} {'Std Dev':<10} {'N':<5}")
    print("-" * 45)
    
    for condition, r in results.items():
        print(f"{condition:<15} {r.mean_time:<12.2f} {r.std_time:<10.2f} {r.n:<5}")
    
    print("\n" + "=" * 50)
    print("ATTRIBUTION ACCURACY")
    print("=" * 50)
    print(f"{'Condition':<15} {'Accuracy (%)':<12} {'N':<5}")
    print("-" * 35)
    
    for condition, r in results.items():
        print(f"{condition:<15} {r.accuracy * 100:<12.1f} {r.n:<5}")


def calculate_improvement(results: Dict[str, ValidationResults]) -> None:
    """Calculate improvement metrics."""
    print("\n" + "=" * 50)
    print("IMPROVEMENT METRICS")
    print("=" * 50)
    
    if 'treatment' in results and 'baseline_b' in results:
        t = results['treatment']
        b = results['baseline_b']
        
        if b.mean_time > 0:
            time_reduction = ((b.mean_time - t.mean_time) / b.mean_time) * 100
            print(f"Time reduction vs Baseline B: {time_reduction:.1f}%")
        
        accuracy_diff = (t.accuracy - b.accuracy) * 100
        print(f"Accuracy improvement vs Baseline B: {accuracy_diff:+.1f} percentage points")
    
    if 'treatment' in results and 'baseline_a' in results:
        t = results['treatment']
        a = results['baseline_a']
        
        if a.mean_time > 0:
            time_reduction = ((a.mean_time - t.mean_time) / a.mean_time) * 100
            print(f"Time reduction vs Baseline A: {time_reduction:.1f}%")


def run_statistical_tests(results: Dict[str, ValidationResults]) -> None:
    """Run statistical tests (requires scipy)."""
    print("\n" + "=" * 50)
    print("STATISTICAL TESTS")
    print("=" * 50)
    
    try:
        from scipy import stats
        
        if 'baseline_b' in results and 'treatment' in results:
            b = results['baseline_b']
            t = results['treatment']
            
            # T-test for attribution time
            t_stat, p_value = stats.ttest_ind(b.times, t.times)
            print(f"\nTreatment vs Baseline B (time):")
            print(f"  t-statistic: {t_stat:.3f}")
            print(f"  p-value: {p_value:.4f}")
            print(f"  Significant (p<0.05): {'YES' if p_value < 0.05 else 'NO'}")
            
            # Effect size (Cohen's d)
            pooled_std = ((len(b.times) - 1) * b.std_time**2 + 
                         (len(t.times) - 1) * t.std_time**2) / (len(b.times) + len(t.times) - 2)
            pooled_std = pooled_std ** 0.5
            if pooled_std > 0:
                cohens_d = (b.mean_time - t.mean_time) / pooled_std
                print(f"  Cohen's d: {cohens_d:.3f}")
                
    except ImportError:
        print("Note: Install scipy for statistical testing")
        print("  pip install scipy")
        print("\nManual calculation needed for:")
        print("  - Two-sample t-test (or Mann-Whitney U)")
        print("  - Effect size (Cohen's d)")
        print("  - Chi-square test for accuracy differences")


def check_thresholds(results: Dict[str, ValidationResults]) -> None:
    """Check against thresholds from EVALUATION_METHODOLOGY.md."""
    print("\n" + "=" * 50)
    print("THRESHOLD CHECKS (per EVALUATION_METHODOLOGY.md)")
    print("=" * 50)
    
    if 'treatment' not in results:
        print("No treatment condition found.")
        return
    
    t = results['treatment']
    
    # Accuracy threshold: ≥80%
    accuracy_threshold = 0.80
    accuracy_pass = t.accuracy >= accuracy_threshold
    print(f"\n1. Attribution accuracy ≥80%:")
    print(f"   Result: {t.accuracy:.1%}")
    print(f"   Status: {'✓ PASS' if accuracy_pass else '✗ FAIL'}")
    
    # Falsifiability: accuracy should be >70%
    falsify_threshold = 0.70
    falsify_pass = t.accuracy >= falsify_threshold
    print(f"\n2. Not falsified (accuracy >70%):")
    print(f"   Result: {t.accuracy:.1%}")
    print(f"   Status: {'✓ NOT FALSIFIED' if falsify_pass else '✗ FALSIFIED'}")
    
    # Time improvement check (if baseline available)
    if 'baseline_b' in results:
        b = results['baseline_b']
        if b.mean_time > 0:
            improvement = (b.mean_time - t.mean_time) / b.mean_time
            improve_pass = improvement > 0
            print(f"\n3. Time improvement vs Baseline B:")
            print(f"   Result: {improvement:.1%} {'faster' if improvement > 0 else 'slower'}")
            print(f"   Status: {'✓ IMPROVED' if improve_pass else '✗ NO IMPROVEMENT'}")


def generate_report_fragment(results: Dict[str, ValidationResults]) -> str:
    """Generate markdown fragment for validation report."""
    lines = ["## Auto-Generated Results Summary", ""]
    
    # Time table
    lines.append("### Primary Metric: Root Cause Attribution Time")
    lines.append("")
    lines.append("| Condition | Mean Time (min) | Std Dev | N |")
    lines.append("|-----------|-----------------|---------|---|")
    for condition, r in results.items():
        lines.append(f"| {condition} | {r.mean_time:.2f} | {r.std_time:.2f} | {r.n} |")
    lines.append("")
    
    # Accuracy table
    lines.append("### Secondary Metric: Attribution Accuracy")
    lines.append("")
    lines.append("| Condition | Accuracy (%) | N |")
    lines.append("|-----------|--------------|---|")
    for condition, r in results.items():
        lines.append(f"| {condition} | {r.accuracy * 100:.1f} | {r.n} |")
    lines.append("")
    
    # Improvement
    if 'treatment' in results and 'baseline_b' in results:
        t = results['treatment']
        b = results['baseline_b']
        if b.mean_time > 0:
            time_reduction = ((b.mean_time - t.mean_time) / b.mean_time) * 100
            lines.append(f"**Improvement over Baseline B**: {time_reduction:.1f}% time reduction")
            lines.append("")
    
    return "\n".join(lines)


def main(filepath: str) -> None:
    """Main entry point."""
    print(f"Loading validation results from: {filepath}")
    results = load_results(filepath)
    print(f"Loaded {len(results)} conditions: {list(results.keys())}")
    
    print_summary(results)
    calculate_improvement(results)
    run_statistical_tests(results)
    check_thresholds(results)
    
    # Generate report fragment
    print("\n" + "=" * 50)
    print("MARKDOWN FRAGMENT (copy to validation_report.md)")
    print("=" * 50)
    print(generate_report_fragment(results))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze_validation.py <results.json>")
        print()
        print("Example results.json format:")
        print(json.dumps({
            "baseline_a": {"times": [12.5, 15.0, 18.2], "correct": [True, True, False]},
            "baseline_b": {"times": [8.5, 10.2, 12.1], "correct": [True, True, True]},
            "treatment": {"times": [4.2, 5.1, 6.8], "correct": [True, True, True]}
        }, indent=2))
        sys.exit(1)
    
    main(sys.argv[1])
