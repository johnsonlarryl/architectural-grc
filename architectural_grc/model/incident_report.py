from langchain_openai import ChatOpenAI
from typing import Any, Dict

from architectural_grc.contexts.event_context import build_unified_context
from architectural_grc.prompts.event_narrative_prompt import build_incident_report_prompt
from architectural_grc.setup.historian import load_historian_tags



def get_model() -> ChatOpenAI:
    return ChatOpenAI(
        model="gpt-5.4-mini",
        temperature=0.2,
    )


def generate_incident_report() -> str:
    context = build_unified_context()
    prompt = build_incident_report_prompt()
    llm = get_model()

    chain = prompt | llm
    response = chain.invoke(context)

    return response.content if hasattr(response, "content") else str(response)


def build_summary_payload() -> Dict[str, Any]:
    historian_tags = load_historian_tags()

    max_temp = historian_tags.loc[historian_tags["tag"] == "R201_TEMP_C", "value"].max()
    max_pressure = historian_tags.loc[historian_tags["tag"] == "R201_PRESSURE_PSIG", "value"].max()

    return {
        "incident_id": "INC-2026-04-22-R201-01",
        "asset": "R-201",
        "materials": ["Agent Y", "Residual Ethanol"],
        "max_temperature_c": max_temp,
        "max_pressure_psig": max_pressure,
        "containment_breached": True,
        "line_shutdown": True,
        "likely_primary_failure_mode": "Runaway exothermic reaction",
    }
