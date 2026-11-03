# Cardiac Systolic Time Intervals (PEP/LVET) & Inotropy Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive evaluation of Pre-Ejection Period (PEP), Left Ventricular Ejection Time (LVET), Weissler rate-corrected indices, and myocardial inotropic kinetics.

```mermaid
flowchart TD
    ECG_PCG["ECG & Phonocardiography / ICG Sensors"] --> PEP_LVET["Systolic Time Intervals Extraction"]
    PEP_LVET --> Weissler["Weissler Equations (PEPI, LVETI, PEP/LVET)"]
    Weissler --> Inotropy["Myocardial Inotropic Efficiency Analysis"]
    Inotropy --> Agent["OpenClaw / Hermes Personal Agent Actions"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **Weissler Standard Indices**: Automatic rate correction according to standard non-invasive cardiography formulas.
- **Inotropic Performance Stratification**: Quantitative evaluation of sympathetic vs depressed myocardial contractility.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import SystolicTimeIntervalsClient

client = SystolicTimeIntervalsClient()
result = client.evaluate_systolic_intervals(
    pep_ms=96.0,
    lvet_ms=295.0,
    heart_rate_bpm=70.0
)
print("PEP/LVET Ratio:", result["pep_lvet_ratio"])
print("Classification:", result["classification"])
```

## License
Apache-2.0
