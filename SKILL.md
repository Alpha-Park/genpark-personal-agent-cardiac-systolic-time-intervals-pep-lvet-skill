---
name: genpark-personal-agent-cardiac-systolic-time-intervals-pep-lvet-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for calculating cardiac Pre-Ejection Period (PEP), Left Ventricular Ejection Time (LVET), Weissler rate-corrected indices, and myocardial inotropic kinetics.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Cardiac Systolic Time Intervals (PEP/LVET) Skill

A sovereign personal agent capability for assessing myocardial contractile performance, left ventricular ejection mechanics, and autonomic inotropy through deterministic Weissler systolic time intervals.

## Core Capabilities
- **Pre-Ejection Period (PEP)**: Measures electromechanical delay and isovolumetric contraction phase.
- **Left Ventricular Ejection Time (LVET)**: Duration of aortic blood outflow during ventricular systole.
- **Weissler Corrected Indices**: Rate-standardized PEPI and LVETI metrics.
- **Myocardial Inotropic Efficiency Score (MIES)**: 0-100 rating of myocardial force generation kinetics.

## Fast Invocation
```python
from client import SystolicTimeIntervalsClient

client = SystolicTimeIntervalsClient()
res = client.evaluate_systolic_intervals(
    pep_ms=95.0,
    lvet_ms=290.0,
    heart_rate_bpm=72.0
)
print("PEP/LVET Ratio:", res["pep_lvet_ratio"])
print("Inotropic Score:", res["myocardial_inotropic_score"])
```
