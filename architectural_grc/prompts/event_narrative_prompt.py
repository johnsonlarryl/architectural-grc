from langchain_core.prompts import ChatPromptTemplate

EVENT_NARRATIVE = """
At 10:02 AM, the system transitioned to the new batch and Agent Y was introduced into Reactor R-201.
Within minutes, residual ethanol that had not been fully cleared from the system reacted with Agent Y.
The reaction generated heat rapidly, exceeding the system's ability to dissipate it. Temperature sensors
began to spike, followed by a sharp increase in pressure. By 10:06 AM, the reactor exceeded its containment
limits, resulting in a runaway reaction and subsequent explosion. The production line was immediately shut down,
the facility initiated emergency response protocols, and the new product launch was halted temporarily.

At the same time, IT Operations, led by Maya and her highly talented team of senior software engineers,
had integrated a variety of digital systems into a new Redshift OLAP data warehouse. These systems included SAP,
the company's new global shift reporting web application, AVEVA PI historian systems, a knowledge graph database
of secret formulas, and other operational systems. Bringing these disparate systems together into unified panes of
glass allowed business functions across the enterprise to observe the organization, its processes, and its subsystems
from multiple perspectives.

During the event bridge, which had been open since 10:30 AM that morning, leaders and individual contributors from
across the organization gathered in what felt like a Roman colosseum, waiting to see who would become the next casualty
of the moment. As Jordan pressed his team with questions about what had happened, Maya joined the call wearing
noise-canceling earbuds from her son's field trip. Students shouted from a school bus window as they passed the skyline
near the Uptown and Galleria area of Houston. Maya politely interrupted Jordan and dropped a link into the company chat
to the OHS incident report.

At the end of the previous year, Maya's team had architected, designed, and developed the company's new OHS system,
entitled SignalBistro. SignalBistro had been designed to automatically generate incident reports from the OLAP data
that had been ingested as knowledge item embeddings into a Pinecone vector database. These knowledge items also allowed
the team to periodically apply transfer learning to foundational models retrained on the company's historical data before
new data was streamed into Pinecone. Without diving too deeply into those mechanics, Maya explained to senior leadership
and technicians on the call what the report had found. The report also embedded visualizations that explained the state
of the various systems before, during, and after the incident.

The OHS report concluded that the primary cause of the incident was the chemical incompatibility between residual ethanol
and incoming Agent Y, compounded by the failure to complete the required cleaning within the designated window.
Contributing factors included the reuse of a continuous production system not designed for multi-process transitions,
the compression of cleaning intervals to meet business demands, and the dismissal of both engineering and operator warnings.
Ultimately, the failure was not due to a lack of data or awareness, but rather the absence of a governance mechanism capable
of enforcing known process constraints in real time. John and his cohort of process engineers confirmed this conclusion
during the call by running supporting queries in Redshift.
""".strip()


def build_incident_report_prompt() -> ChatPromptTemplate:
    return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
    You are an Occupational Health and Safety (OHS) incident investigation assistant for a
    chemical manufacturing organization.

    Your task:
    1. Analyze the event narrative and the supporting enterprise data.
    2. Produce a professional incident report in clear business language.
    3. Distinguish:
       - primary cause
       - contributing causes
       - timeline of events
       - affected systems/assets
       - immediate actions taken
       - governance/control failures
       - recommended corrective and preventive actions (CAPA)
    4. Ground your conclusions in the supplied data only.
    5. If something is uncertain, say it is uncertain rather than inventing facts.
    6. Return the report in Markdown with these sections:

    # OHS Incident Report
    ## Executive Summary
    ## Incident Overview
    ## Incident Timeline
    ## Evidence by Source System
    ## Root Cause Analysis
    ## Contributing Factors
    ## Immediate Response Actions
    ## Governance and Control Gaps
    ## Corrective and Preventive Actions
    ## Suggested Visualizations
    ## Confidence and Data Gaps

    For "Suggested Visualizations", recommend useful charts but do not render them.
    """.strip(),
                ),
                (
                    "human",
                    """
    Generate the incident report using the following data.

    EVENT NARRATIVE
    {event_narrative}

    {historian_tags}

    {shift_reports}

    {sap_rows}

    {neo4j_records}
    """.strip(),
                ),
            ]
        )
