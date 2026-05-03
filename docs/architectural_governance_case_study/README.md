<!-- ABOUT THE PROJECT -->

## About The Project
<div id="readme-top"></div>

# OHS Incident Report Generation & Performance Validation

This project provides a **test harness and validation framework** for generating an **Occupational Health & Safety (OHS) incident report** using an AI-driven model.

This test implements a **Performance SLA Fitness Function (Latency Threshold)**. It is a triggered, dynamic, quantitative, and simple fitness function that validates whether the incident report generation capability meets a defined execution-time constraint. The function executes the full report-generation workflow at runtime, measures the elapsed time using a high-resolution clock, and enforces an upper-bound threshold (`report_generation_expect_time`). Because it is invoked during test execution (e.g., via pytest or CI/CD pipelines), it is considered triggered; because it runs the actual code path, it is dynamic; because it evaluates a numeric metric (seconds), it is quantitative; and because it checks a single condition (elapsed time ≤ threshold), it is simple. Architecturally, this fitness function ensures that the system maintains acceptable latency for LLM-driven report generation and guards against regressions such as increased prompt size, slower external dependencies, or inefficiencies introduced through code changes.

The primary goal is to:

- Generate a structured incident report from aggregated enterprise data sources  
- Validate that the report is successfully produced  
- Ensure the generation completes within an acceptable **performance threshold**

---

<b>Table 1 – Project Archetype</b>

| Type                  | Sub Type                  | Concept                                                                 |
|-----------------------|---------------------------|-------------------------------------------------------------------------|
| AI / LLM Systems      | Report Generation         | Incident summarization from multi-source enterprise data                |
| Software Engineering  | Performance Testing       | Execution timing and SLA validation                                     |
| Governance / GRC      | Operational Risk          | Incident documentation and traceability                                |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Overview

This module tests the integration between:

- **Data aggregation layer** (`build_summary_payload`)
- **LLM-based report generation** (`generate_incident_report`)
- **Performance validation logic**

The test ensures that:

1. A summary payload is constructed correctly  
2. An incident report is generated successfully  
3. The generation time meets defined expectations  

---

## Usage

```
poetry run pytest -k test_incident_report_model -s --log-cli-level=WARNING
```
