"""
MCP Server implementation for Somatosensory Cutaneous Silent Period (CSP) Skill.
Exposes standard FastMCP-compatible tools for spinal inhibitory reflex and A-delta sensory conduction profiling.
"""

import sys
import json
from typing import Dict, Any, Optional
from client import CutaneousSilentPeriodClient


def evaluate_cutaneous_silent_period(
    onset_latency_ms: float,
    end_latency_ms: float,
    baseline_emg_rms_uv: Optional[float] = 100.0,
    silent_emg_rms_uv: Optional[float] = 10.0,
    limb: Optional[str] = "Upper Limb (C8-T1)",
    target_muscle: Optional[str] = "Abductor Pollicis Brevis (APB)",
    patient_age_years: Optional[int] = 45
) -> str:
    """
    Evaluates Cutaneous Silent Period (CSP) onset latency, duration, and suppression depth.
    Returns structured analysis of spinal cord interneuronal inhibition and myelopathy risk.
    """
    client = CutaneousSilentPeriodClient()
    result = client.evaluate_csp(
        onset_latency_ms=onset_latency_ms,
        end_latency_ms=end_latency_ms,
        baseline_emg_rms_uv=baseline_emg_rms_uv,
        silent_emg_rms_uv=silent_emg_rms_uv,
        limb=limb,
        target_muscle=target_muscle,
        patient_age_years=patient_age_years
    )
    return json.dumps(result, indent=2)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--tools":
        tools = [
            {
                "name": "evaluate_cutaneous_silent_period",
                "description": "Calculates Cutaneous Silent Period (CSP) onset latency, duration, and suppression depth to evaluate spinal inhibitory interneurons and small-fiber A-delta sensory pathways.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "onset_latency_ms": {"type": "number", "description": "Onset latency of voluntary EMG suppression in ms (normal upper limb: 50 - 75 ms)"},
                        "end_latency_ms": {"type": "number", "description": "End latency / resumption of voluntary EMG in ms"},
                        "baseline_emg_rms_uv": {"type": "number", "description": "Mean baseline pre-stimulus voluntary EMG RMS amplitude in uV (default: 100 uV)"},
                        "silent_emg_rms_uv": {"type": "number", "description": "Mean EMG RMS amplitude during the silent period in uV (default: 10 uV)"},
                        "limb": {"type": "string", "description": "Anatomical limb: 'Upper Limb (C8-T1)' or 'Lower Limb (L5-S1)'"},
                        "target_muscle": {"type": "string", "description": "Muscle recorded (e.g. 'Abductor Pollicis Brevis (APB)')"},
                        "patient_age_years": {"type": "integer", "description": "Patient age in years (default: 45)"}
                    },
                    "required": ["onset_latency_ms", "end_latency_ms"]
                }
            }
        ]
        print(json.dumps(tools, indent=2))
    else:
        # Simple self-test
        client = CutaneousSilentPeriodClient()
        test_res = client.evaluate_csp(
            onset_latency_ms=58.0,
            end_latency_ms=92.0
        )
        print("Self-test passed:")
        print(json.dumps(test_res, indent=2))
