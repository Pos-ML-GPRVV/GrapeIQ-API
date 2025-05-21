from database.connection import get_connection
import json
from datetime import datetime, timedelta

class Insert:
    def __init__(self):
        pass
    def save_json(df: dict, year: int):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                INSERT INTO embrapa (year, data_json, due_date)
                VALUES (%s, %s, %s)
                ON CONFLICT (year)
                DO UPDATE SET
                    data_json = EXCLUDED.data_json,
                    due_date = EXCLUDED.due_date
                """,
                (
                    year,
                    json.dumps(df, ensure_ascii=False),
                    datetime.now() + timedelta(days=1)
                )
            )
        except Exception:
            conn.rollback()
            cursor.close()
            conn.close()

        conn.commit()
        cursor.close()
        conn.close()
