from app.database.connection import get_connection
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
class Select:
    def __init__(self):
        pass
    def fetch_data_by_year(year: int):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            print(f"Searching for data from year: {year}")
            cursor.execute(
                f"""
                SELECT data_json
                FROM embrapa
                WHERE year = {year}
                """
            )
            result = cursor.fetchall()
            print(f"Resources found: {len(result) if result else 0}")
            return result
        except Exception as e:
            print(f"Error searching for data: {str(e)}")
            return None
        finally:
            cursor.close()
            conn.close()
            
    def fetch_due_date(year: int):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                f"""
                SELECT due_date
                FROM embrapa
                WHERE year = {year}
                """
            )
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error searching for data: {str(e)}")
            return None
        finally:
            cursor.close()
            conn.close()
