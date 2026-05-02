from typing import Any, Dict, List


def load_shift_reports() -> List[Dict[str, Any]]:
    rows = [
        {
            "report_id": "SHIFT-AM-220426-01",
            "author": "Operator A",
            "shift": "Day",
            "timestamp": "2026-04-22 08:45:00",
            "text": (
                "Cleaning on Reactor R-201 ran long overnight. Team was asked to compress the "
                "cleaning window to stay aligned with launch schedule. Residual solvent concern "
                "was mentioned during turnover."
            ),
        },
        {
            "report_id": "SHIFT-AM-220426-02",
            "author": "Supervisor B",
            "shift": "Day",
            "timestamp": "2026-04-22 09:35:00",
            "text": (
                "Engineering noted R-201 is a continuous production asset and not ideal for "
                "rapid multi-process transitions. Operators requested confirmation of ethanol "
                "clearance before Agent Y introduction."
            ),
        },
        {
            "report_id": "SHIFT-AM-220426-03",
            "author": "Operator C",
            "shift": "Day",
            "timestamp": "2026-04-22 10:07:00",
            "text": (
                "Observed temperature and pressure spike within minutes after Agent Y feed started. "
                "Emergency shutdown initiated after reactor event."
            ),
        },
    ]

    return rows
