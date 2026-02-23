import schedule
import time
from main import run

run()

#Daily Refresh
schedule.every().day.at("00:00").do(run)

print("Scheduler started")

while True:
    schedule.run_pending()
    time.sleep(60)

