"""
Example usage for Somatosensory Cutaneous Silent Period (CSP) Skill.
"""

from client import CutaneousSilentPeriodClient


def main():
    client = CutaneousSilentPeriodClient()

    print("--- Case 1: Normal Physiological Upper Extremity CSP ---")
    normal_case = client.evaluate_csp(
        onset_latency_ms=58.5,
        end_latency_ms=94.0,
        baseline_emg_rms_uv=120.0,
        silent_emg_rms_uv=8.5,
        limb="Upper Limb (C8-T1)",
        target_muscle="Abductor Pollicis Brevis (APB)",
        patient_age_years=35
    )
    print("Onset Latency:", normal_case["csp_kinetics"]["onset_latency_ms"], "ms")
    print("Duration:", normal_case["csp_kinetics"]["duration_ms"], "ms")
    print("Suppression Depth:", normal_case["csp_kinetics"]["suppression_depth_pct"], "%")
    print("CSP Status:", normal_case["neurophysiological_assessment"]["csp_status"])
    print("Pathophysiology:", normal_case["neurophysiological_assessment"]["pathophysiology_summary"])
    print()

    print("--- Case 2: Cervical Spondylotic Myelopathy (Shortened CSP) ---")
    myelopathy_case = client.evaluate_csp(
        onset_latency_ms=62.0,
        end_latency_ms=78.0,
        baseline_emg_rms_uv=95.0,
        silent_emg_rms_uv=38.0,
        limb="Upper Limb (C8-T1)",
        patient_age_years=62
    )
    print("Duration:", myelopathy_case["csp_kinetics"]["duration_ms"], "ms")
    print("Suppression Depth:", myelopathy_case["csp_kinetics"]["suppression_depth_pct"], "%")
    print("CSP Status:", myelopathy_case["neurophysiological_assessment"]["csp_status"])
    print("Pathophysiology:", myelopathy_case["neurophysiological_assessment"]["pathophysiology_summary"])
    print()

    print("--- Case 3: Peripheral Small-Fiber A-Delta Conduction Delay ---")
    delay_case = client.evaluate_csp(
        onset_latency_ms=86.0,
        end_latency_ms=124.0,
        baseline_emg_rms_uv=110.0,
        silent_emg_rms_uv=12.0,
        limb="Upper Limb (C8-T1)",
        patient_age_years=54
    )
    print("Onset Latency:", delay_case["csp_kinetics"]["onset_latency_ms"], "ms")
    print("CSP Status:", delay_case["neurophysiological_assessment"]["csp_status"])
    print("Pathophysiology:", delay_case["neurophysiological_assessment"]["pathophysiology_summary"])


if __name__ == "__main__":
    main()
