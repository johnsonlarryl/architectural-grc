import pandas as pd


def load_sap_data() -> pd.DataFrame:
    rows = [
        {
            "work_order": "WO-774921",
            "equipment": "R-201",
            "material": "Agent Y",
            "planned_start": "2026-04-22 10:00:00",
            "campaign": "New Product Launch",
            "cleaning_required": True,
            "cleaning_status": "Partially Complete",
            "maintenance_note": "Do not introduce reactive agents until solvent clearance confirmed.",
            "approver": "John",
        },
        {
            "work_order": "WO-774922",
            "equipment": "R-201",
            "material": "Ethanol",
            "planned_start": "2026-04-22 07:30:00",
            "campaign": "Line Preparation",
            "cleaning_required": True,
            "cleaning_status": "Not Electronically Closed",
            "maintenance_note": "Final purge verification pending",
            "approver": "John",
        },
    ]
    return pd.DataFrame(rows)
