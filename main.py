from database import init_db
from extract import get_owned_games
from load import insert_games
from datetime import datetime

def run():
    print("ETL START - ", datetime.now())

    init_db()
    games = get_owned_games()
    insert_games(games)

    print("ETL END - ", datetime.now())

if __name__ == "__main__":
    run()
