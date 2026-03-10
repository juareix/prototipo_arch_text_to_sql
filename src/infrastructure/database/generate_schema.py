import sqlite3
import os
import json

DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'olist.sqlite'))


def get_tables(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]
    return tables


def get_table_schema(conn, table_name):
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = []
    for col in cursor.fetchall():
        columns.append({
            "name": col[1],
            "type": col[2],
            "notnull": bool(col[3]),
            "default": col[4],
            "pk": bool(col[5])
        })
    return columns


def generate_schema(db_path):
    conn = sqlite3.connect(db_path)
    tables = get_tables(conn)
    schema = {}
    for table in tables:
        schema[table] = get_table_schema(conn, table)
    conn.close()
    return schema


def main():
    schema = generate_schema(DB_PATH)
    output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'docs', 'schemas', 'olist_schema.json'))
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(schema, f, indent=2, ensure_ascii=False)
    print(f"Schema gerado em {output_path}")

if __name__ == "__main__":
    main()
