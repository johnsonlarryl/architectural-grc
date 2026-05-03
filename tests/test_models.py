import json
import logging
import time

from architectural_grc.model.incident_report import build_summary_payload, generate_incident_report

logging = logging.getLogger(__name__)


def test_incident_report_model():
    summary_payload = build_summary_payload()
    report_generation_expect_time = 20.0
    logging.warning("=== PRECOMPUTED SUMMARY PAYLOAD ===")
    logging.warning(json.dumps(summary_payload, indent=2))
    logging.warning("\n=== GENERATED OHS INCIDENT REPORT ===\n")

    start = time.perf_counter()
    report = generate_incident_report()
    elapsed = time.perf_counter() - start
    logging.warning(report)
    report = generate_incident_report()

    assert report
    assert elapsed <= report_generation_expect_time, f"Execution took too long: {elapsed:.4f}s > {report_generation_expect_time}s"
