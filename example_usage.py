"""
Example Usage: Cardiac Systolic Time Intervals (PEP/LVET) Evaluation.
Demonstrates non-invasive calculation of Weissler indices and myocardial inotropy.
"""

from client import SystolicTimeIntervalsClient


def main():
    client = SystolicTimeIntervalsClient()
    print("=== Cardiac Systolic Time Intervals (PEP/LVET) & Inotropy Demo ===")

    # Test Case 1: Healthy resting adult
    res1 = client.evaluate_systolic_intervals(
        pep_ms=96.0,
        lvet_ms=295.0,
        heart_rate_bpm=70.0
    )
    print("\nTest Case 1: Normal Resting Adult")
    print(f"  PEP: {res1['pep_ms']} ms | LVET: {res1['lvet_ms']} ms | HR: {res1['heart_rate_bpm']} bpm")
    print(f"  PEP/LVET Ratio: {res1['pep_lvet_ratio']}")
    print(f"  Weissler PEPI: {res1['weissler_pepi_ms']} ms | LVETI: {res1['weissler_lveti_ms']} ms")
    print(f"  Myocardial Inotropic Score: {res1['myocardial_inotropic_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Adrenergic surge / vigorous exercise
    res2 = client.evaluate_systolic_intervals(
        pep_ms=55.0,
        lvet_ms=220.0,
        heart_rate_bpm=135.0
    )
    print("\nTest Case 2: Adrenergic Exercise Surge")
    print(f"  PEP: {res2['pep_ms']} ms | LVET: {res2['lvet_ms']} ms | HR: {res2['heart_rate_bpm']} bpm")
    print(f"  PEP/LVET Ratio: {res2['pep_lvet_ratio']}")
    print(f"  Weissler PEPI: {res2['weissler_pepi_ms']} ms | LVETI: {res2['weissler_lveti_ms']} ms")
    print(f"  Classification: {res2['classification']}")

    # Test Case 3: Depressed left ventricular contractile state
    res3 = client.evaluate_systolic_intervals(
        pep_ms=145.0,
        lvet_ms=260.0,
        heart_rate_bpm=78.0
    )
    print("\nTest Case 3: Depressed Left Ventricular Inotropy")
    print(f"  PEP: {res3['pep_ms']} ms | LVET: {res3['lvet_ms']} ms | HR: {res3['heart_rate_bpm']} bpm")
    print(f"  PEP/LVET Ratio: {res3['pep_lvet_ratio']}")
    print(f"  Myocardial Inotropic Score: {res3['myocardial_inotropic_score']} / 100")
    print(f"  Classification: {res3['classification']}")
    print(f"  Guidance: {res3['actionable_guidance']}")


if __name__ == "__main__":
    main()
