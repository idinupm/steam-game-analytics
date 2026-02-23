from database import get_conn

def insert_games(games):
    conn = get_conn()
    cur = conn.cursor()

    for g in games:
        cur.execute("""
        INSERT OR REPLACE INTO games VALUES (?, ?, ?, ?)
        """, (
            g["appid"],
            g.get("name"),
            g.get("playtime_forever", 0),
            g.get("playtime_2weeks", 0)
        ))

    conn.commit()
    conn.close()
