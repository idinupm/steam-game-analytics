import sqlite3

def get_conn():
    return sqlite3.connect("steam.db")

def init_db():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS games(
        appid INTEGER PRIMARY KEY,
        name TEXT,
        playtime_forever INTEGER,
        playtime_2weeks INTEGER
    )
    """)

    conn.commit()
    conn.close()
