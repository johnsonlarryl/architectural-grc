from typing import Any, Dict, List


def load_bom_graph_db() -> List[Dict[str, Any]]:
    rows = [
        {
            "reactor": "R-201",
            "agent": "Agent Y",
            "incompatible_with": "Ethanol",
            "relationship": "CHEMICALLY_INCOMPATIBLE_WITH",
            "hazard": "Exothermic reaction with rapid gas generation",
            "source_doc": "Process Hazard Analysis v4.2",
            "severity": "Critical",
        },
        {
            "reactor": "R-201",
            "constraint": "Continuous production system not designed for fast multi-process transitions",
            "relationship": "HAS_PROCESS_LIMIT",
            "source_doc": "Equipment Design Basis Memo",
            "severity": "High",
        },
        {
            "reactor": "R-201",
            "warning": "Cleaning interval must not be compressed below validated window",
            "relationship": "HAS_VALIDATION_CONSTRAINT",
            "source_doc": "Cleaning Validation SOP-118",
            "severity": "High",
        },
    ]

    return rows

