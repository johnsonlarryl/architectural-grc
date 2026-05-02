import pandas as pd


def load_historian_tags() -> pd.DataFrame:
    rows = [
        {"timestamp": "2026-04-22 09:58:00", "asset": "R-201", "tag": "R201_TEMP_C", "value": 72.1, "unit": "C"},
        {"timestamp": "2026-04-22 10:00:00", "asset": "R-201", "tag": "R201_PRESSURE_PSIG", "value": 18.0, "unit": "psig"},
        {"timestamp": "2026-04-22 10:01:00", "asset": "R-201", "tag": "R201_CLEANING_STATUS", "value": "INCOMPLETE", "unit": ""},
        {"timestamp": "2026-04-22 10:02:00", "asset": "R-201", "tag": "R201_BATCH_ID", "value": "BATCH-88421", "unit": ""},
        {"timestamp": "2026-04-22 10:02:10", "asset": "R-201", "tag": "R201_AGENT_Y_FEED", "value": "OPEN", "unit": ""},
        {"timestamp": "2026-04-22 10:03:00", "asset": "R-201", "tag": "R201_TEMP_C", "value": 88.4, "unit": "C"},
        {"timestamp": "2026-04-22 10:03:30", "asset": "R-201", "tag": "R201_PRESSURE_PSIG", "value": 31.5, "unit": "psig"},
        {"timestamp": "2026-04-22 10:04:00", "asset": "R-201", "tag": "R201_TEMP_C", "value": 112.6, "unit": "C"},
        {"timestamp": "2026-04-22 10:04:30", "asset": "R-201", "tag": "R201_PRESSURE_PSIG", "value": 49.8, "unit": "psig"},
        {"timestamp": "2026-04-22 10:05:00", "asset": "R-201", "tag": "R201_TEMP_C", "value": 147.2, "unit": "C"},
        {"timestamp": "2026-04-22 10:05:15", "asset": "R-201", "tag": "R201_PRESSURE_PSIG", "value": 68.4, "unit": "psig"},
        {"timestamp": "2026-04-22 10:05:40", "asset": "R-201", "tag": "R201_HIHI_PRESSURE_ALARM", "value": "ACTIVE", "unit": ""},
        {"timestamp": "2026-04-22 10:06:00", "asset": "R-201", "tag": "R201_CONTAINMENT_STATE", "value": "BREACHED", "unit": ""},
        {"timestamp": "2026-04-22 10:06:05", "asset": "LINE-2", "tag": "LINE2_STATUS", "value": "SHUTDOWN", "unit": ""},
    ]
    return pd.DataFrame(rows)
