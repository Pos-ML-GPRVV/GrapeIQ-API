from db.connection import get_connection
import pandas as pd
import json

def salvar_dataframe(df: pd.DataFrame, tipo: str, ano: int):
    conn = get_connection()
    cursor = conn.cursor()

    for _, row in df.iterrows():
        if "Item" in df.columns:

            cursor.execute(
                """
                SELECT 1 FROM embrapa
                WHERE tipo = %s AND ano = %s AND item = %s AND subitem = %s
                """,
                (tipo, ano, row.get("Item"), row.get("SubItem"))
            )
            if cursor.fetchone():
                continue

            cursor.execute(
                """
                INSERT INTO embrapa (tipo, ano, item, subitem, quantidade)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    tipo,
                    ano,
                    row.get("Item"),
                    row.get("SubItem"),
                    parse_num(row.get("Quantidade"))
                )
            )

        elif "Países" in df.columns or "País" in df.columns:
            pais = row.get("Países") or row.get("País")

            cursor.execute(
                """
                SELECT 1 FROM embrapa
                WHERE tipo = %s AND ano = %s AND pais = %s
                """,
                (tipo, ano, pais)
            )
            if cursor.fetchone():
                continue

            cursor.execute(
                """
                INSERT INTO embrapa (tipo, ano, pais, quantidade, valor)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    tipo,
                    ano,
                    pais,
                    parse_num(row.get("Quantidade (Kg)")),
                    parse_num(row.get("Valor (US$)"))
                )
            )

    conn.commit()
    cursor.close()
    conn.close()

def parse_num(valor):
    if isinstance(valor, str):
        return int(valor.replace('.', '').replace(',', '').replace('-', '').strip() or 0)
    return valor

def salvar_json(conn, ano: str, dados: list):
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO embrapa_ano (ano, dados)
            VALUES (%s, %s::jsonb)
            ON CONFLICT (ano)
            DO UPDATE SET dados = EXCLUDED.dados;
        """, (ano, json.dumps(dados)))
        conn.commit()
