"""
Cardiac Systolic Time Intervals (PEP/LVET) & Myocardial Inotropy Engine.
Provides deterministic, zero-dependency modeling of Pre-Ejection Period (PEP),
Left Ventricular Ejection Time (LVET), Weissler rate-corrected indices, and sympathetic inotropy.
"""

from typing import Dict, Any, List, Optional


class SystolicTimeIntervalsClient:
    """
    Deterministic client for calculating cardiac systolic time intervals (PEP, LVET) in milliseconds.
    Pure Python standard library implementation based on Weissler non-invasive cardiography standards.
    """

    def __init__(self):
        pass

    def evaluate_systolic_intervals(
        self,
        pep_ms: float,
        lvet_ms: float,
        heart_rate_bpm: float
    ) -> Dict[str, Any]:
        """
        Calculates PEP/LVET ratio and Weissler rate-corrected indices:
        - PEPI = PEP + (0.4 * HR)
        - LVETI = LVET + (1.7 * HR)
        - Inotropic Ratio = PEP / LVET
        Normal resting PEP/LVET is 0.30 - 0.38.
        """
        if pep_ms <= 0 or lvet_ms <= 0 or heart_rate_bpm <= 30.0:
            return {"error": "Invalid inputs: PEP, LVET, and heart rate must be positive values"}

        ratio = round(pep_ms / lvet_ms, 3)

        # Weissler rate-corrected indices
        pepi = round(pep_ms + (0.4 * heart_rate_bpm), 1)
        lveti = round(lvet_ms + (1.7 * heart_rate_bpm), 1)

        # Myocardial Inotropic Efficiency Score (MIES, 0 - 100):
        # Target ratio 0.30 - 0.36 -> 85 - 95. Ratio > 0.44 -> < 40 (Depressed Inotropy).
        if 0.28 <= ratio <= 0.36:
            mies = min(100.0, 85.0 + (0.36 - ratio) * 100.0)
        elif ratio < 0.28:
            # Hyperdynamic inotropy / high adrenergic surge
            mies = max(65.0, 85.0 - (0.28 - ratio) * 150.0)
        elif ratio <= 0.42:
            mies = 55.0 + ((0.42 - ratio) / 0.06) * 30.0
        elif ratio <= 0.48:
            mies = 30.0 + ((0.48 - ratio) / 0.06) * 25.0
        else:
            mies = max(5.0, 30.0 - (ratio - 0.48) * 100.0)

        mies_score = round(min(100.0, max(5.0, mies)), 1)

        is_hyperdynamic = ratio < 0.28
        is_depressed = ratio > 0.44

        if is_hyperdynamic:
            tier = "HYPERDYNAMIC_SYMPATHETIC_INOTROPY"
            interpretation = f"Shortened PEP relative to ejection time (PEP/LVET {ratio} < 0.28); pronounced beta-adrenergic cardiac inotropic surge."
            guidance = "Elevated myocardial contractile velocity; consistent with acute exercise or strong sympathetic activation."
        elif mies_score >= 75.0:
            tier = "OPTIMAL_MYOCARDIAL_INOTROPIC_EFFICIENCY"
            interpretation = f"Normal balanced systolic time intervals (PEP/LVET {ratio}; PEPI {pepi} ms); healthy left ventricular contractile state."
            guidance = "Myocardial electromechanical coupling is optimal. Ideal baseline hemodynamics."
        elif not is_depressed:
            tier = "MILD_INOTROPIC_RESERVE_ATTENUATION"
            interpretation = f"Mild elongation of isovolumetric contraction phase (PEP/LVET {ratio}); modest contractile reserve reduction."
            guidance = "Monitor hydration, venous return, and incorporate Zone 2 aerobic cardiac conditioning."
        else:
            tier = "DEPRESSED_LEFT_VENTRICULAR_INOTROPY"
            interpretation = f"Significantly elevated PEP/LVET ratio ({ratio} > 0.44); impaired left ventricular contractile kinetics or afterload mismatch."
            guidance = "Depressed systolic inotropy detected. Recommend formal echocardiographic review and blood pressure assessment."

        return {
            "pep_ms": pep_ms,
            "lvet_ms": lvet_ms,
            "heart_rate_bpm": heart_rate_bpm,
            "pep_lvet_ratio": ratio,
            "weissler_pepi_ms": pepi,
            "weissler_lveti_ms": lveti,
            "myocardial_inotropic_score": mies_score,
            "classification": tier,
            "physiological_interpretation": interpretation,
            "actionable_guidance": guidance
        }
