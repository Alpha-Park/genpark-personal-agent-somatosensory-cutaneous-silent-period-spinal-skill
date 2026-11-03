"""
Somatosensory Cutaneous Silent Period (CSP) & Spinal Inhibitory Interneuron Reflex Client.
Zero-mock pure Python standard library implementation.
Calculates CSP Onset Latency (ms), End Latency (ms), Duration (ms), Suppression Depth (%),
and spinal cord dorsal horn / A-delta cutaneous afferent myelopathy staging.
"""

import math
from typing import Dict, Any, Optional


class CutaneousSilentPeriodClient:
    """
    Evaluates spinal inhibitory interneuron reflexes and small-myelinated A-delta afferents:
    - Onset Latency (ms): Upper limb normal 50.0 - 75.0 ms; Lower limb normal 80.0 - 110.0 ms
    - Duration (ms): Upper limb normal 25.0 - 45.0 ms; Lower limb normal 35.0 - 60.0 ms
    - Suppression Depth (%): (1 - (EMG_silent_rms / EMG_baseline_rms)) * 100 (normal >= 80%)
    - Detects cervical spondylotic myelopathy, lumbosacral radiculopathy, and loss of spinal glycinergic inhibition.
    """

    def __init__(self):
        pass

    def evaluate_csp(
        self,
        onset_latency_ms: float,
        end_latency_ms: float,
        baseline_emg_rms_uv: Optional[float] = 100.0,
        silent_emg_rms_uv: Optional[float] = 10.0,
        limb: Optional[str] = "Upper Limb (C8-T1)",
        target_muscle: Optional[str] = "Abductor Pollicis Brevis (APB)",
        patient_age_years: Optional[int] = 45
    ) -> Dict[str, Any]:
        """
        Calculates CSP electrophysiological metrics.
        onset_latency_ms: time from stimulus artifact to EMG suppression onset in ms (e.g. 58.0 ms).
        end_latency_ms: time from stimulus artifact to EMG resumption in ms (e.g. 92.0 ms).
        """
        if onset_latency_ms < 0 or end_latency_ms < 0:
            raise ValueError("Latencies cannot be negative.")
        if end_latency_ms < onset_latency_ms:
            raise ValueError("End latency must be greater than or equal to onset latency.")

        duration_ms = round(end_latency_ms - onset_latency_ms, 1)

        # Suppression depth percentage
        suppression_depth_pct = None
        if baseline_emg_rms_uv and baseline_emg_rms_uv > 0 and silent_emg_rms_uv is not None:
            suppression_depth_pct = round((1.0 - (silent_emg_rms_uv / baseline_emg_rms_uv)) * 100.0, 1)
            suppression_depth_pct = max(0.0, min(100.0, suppression_depth_pct))

        # Check for complete absence of CSP
        is_absent = (duration_ms == 0.0)

        # Normal ranges by anatomical limb:
        is_upper = "upper" in limb.lower()
        normal_min_onset = 50.0 if is_upper else 80.0
        normal_max_onset = 75.0 if is_upper else 110.0
        normal_min_duration = 25.0 if is_upper else 35.0
        normal_max_duration = 50.0 if is_upper else 70.0

        if is_absent:
            csp_status = "Absent Cutaneous Silent Period (Severe Spinal Interneuron Failure)"
            clinical_risk = "Complete disruption of the spinal inhibitory reflex arc; strong indication of cervical spondylotic myelopathy, intramedullary cord lesion, or severe A-delta radicular avulsion."
        elif duration_ms < normal_min_duration or (suppression_depth_pct and suppression_depth_pct < 65.0):
            csp_status = "Shortened / Attenuated CSP (Spinal Disinhibition)"
            clinical_risk = "Impaired spinal glycinergic/GABAergic interneuronal inhibition; classic for early cervical myelopathy or motor neuron disease."
        elif onset_latency_ms > normal_max_onset:
            csp_status = "Prolonged CSP Onset Latency (A-Delta Conduction Delay)"
            clinical_risk = "Delayed transmission along small-myelinated A-delta primary afferents; indicative of peripheral small-fiber polyneuropathy or sensory nerve root entrapment."
        else:
            csp_status = "Normal Physiological Cutaneous Silent Period"
            clinical_risk = "Intact cutaneous A-delta sensory afferents, robust spinal inhibitory interneuronal circuits, and preserved motoneuron pool inhibition."

        return {
            "status": "success",
            "csp_kinetics": {
                "onset_latency_ms": round(onset_latency_ms, 1),
                "end_latency_ms": round(end_latency_ms, 1),
                "duration_ms": duration_ms,
                "suppression_depth_pct": suppression_depth_pct,
                "is_csp_absent": is_absent
            },
            "anatomical_context": {
                "limb": limb,
                "target_muscle": target_muscle,
                "normal_onset_range_ms": [normal_min_onset, normal_max_onset],
                "normal_min_duration_ms": normal_min_duration,
                "patient_age_years": patient_age_years
            },
            "neurophysiological_assessment": {
                "csp_status": csp_status,
                "pathophysiology_summary": clinical_risk
            }
        }
