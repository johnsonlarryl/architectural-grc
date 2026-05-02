import pandas as pd
import json
from typing import Any, Dict, List

from architectural_grc.prompts.event_narrative_prompt import EVENT_NARRATIVE
from architectural_grc.setup.bom_graphdb import load_bom_graph_db
from architectural_grc.setup.historian import load_historian_tags
from architectural_grc.setup.sap import load_sap_data
from architectural_grc.setup.shift_reports import load_shift_reports


def convert_dataframe_to_records_text(df: pd.DataFrame, title: str) -> str:
    records = df.to_dict(orient="records")
    return f"{title}:\n{json.dumps(records, indent=2, default=str)}"


def convert_list_to_records_text(items: List[Dict[str, Any]], title: str) -> str:
    return f"{title}:\n{json.dumps(items, indent=2, default=str)}"


def build_unified_context() -> Dict[str, str]:
    historian_tags = load_historian_tags()
    sap_records = load_sap_data()
    shift_reports = load_shift_reports()
    bom_records = load_bom_graph_db()

    return {
        "event_narrative": EVENT_NARRATIVE,
        "historian_tags": convert_dataframe_to_records_text(historian_tags, "Historian Tags"),
        "shift_reports": convert_list_to_records_text(shift_reports, "Shift Reports"),
        "sap_rows": convert_dataframe_to_records_text(sap_records, "SAP Records"),
        "neo4j_records": convert_list_to_records_text(bom_records, "Knowledge Graph BOM Records"),
    }


