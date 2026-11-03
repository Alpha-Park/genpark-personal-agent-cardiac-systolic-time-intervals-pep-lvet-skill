"""
MCP Server for Cardiac Systolic Time Intervals (PEP/LVET) & Myocardial Inotropy Skill.
Exposes JSON-RPC Model Context Protocol tools for assessing pre-ejection period, left ventricular ejection time, and Weissler indices.
"""

import sys
import json
from typing import Dict, Any
from client import SystolicTimeIntervalsClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_systolic_intervals",
                "description": "Calculates cardiac PEP/LVET ratio, Weissler rate-corrected indices (PEPI, LVETI), and myocardial inotropic efficiency score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "pep_ms": {
                            "type": "number",
                            "description": "Pre-Ejection Period (PEP) in milliseconds (e.g. 95.0)."
                        },
                        "lvet_ms": {
                            "type": "number",
                            "description": "Left Ventricular Ejection Time (LVET) in milliseconds (e.g. 290.0)."
                        },
                        "heart_rate_bpm": {
                            "type": "number",
                            "description": "Resting or active heart rate in beats per minute (e.g. 72.0)."
                        }
                    },
                    "required": ["pep_ms", "lvet_ms", "heart_rate_bpm"]
                }
            }
        ]
    }


def handle_request(client: SystolicTimeIntervalsClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_systolic_intervals":
            res = client.evaluate_systolic_intervals(
                pep_ms=float(args.get("pep_ms", 95.0)),
                lvet_ms=float(args.get("lvet_ms", 290.0)),
                heart_rate_bpm=float(args.get("heart_rate_bpm", 72.0))
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method {name} not found"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": "Invalid request"
            }
        }


def main():
    client = SystolicTimeIntervalsClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": str(e)}
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
