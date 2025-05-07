import os
import requests
from datetime import datetime, timedelta


DOWNLOAD_DIR = "nse_bhavcopies"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://www.nseindia.com"
}


start_date = datetime(2014, 1, 1)
end_date = datetime.today()

session = requests.Session()
session.headers.update(HEADERS)

current_date = start_date

while current_date <= end_date:
    
    if current_date.weekday() < 5:
        day = current_date.strftime('%d')
        month = current_date.strftime('%b').upper()
        year = current_date.strftime('%Y')
        date_str = current_date.strftime('%d%m%Y')
        
        filename = f"cm{date_str}bhav.csv.zip"
        url = f"https://www1.nseindia.com/content/historical/EQUITIES/{year}/{month}/{filename}"
        filepath = os.path.join(DOWNLOAD_DIR, filename)
        
        if not os.path.exists(filepath):
            try:
                print(f"Downloading: {filename}")
                response = session.get(url, timeout=10)
                if response.status_code == 200:
                    with open(filepath, "wb") as f:
                        f.write(response.content)
            except Exception as e:
                print(f"Error on {date_str}: {e}")
    current_date += timedelta(days=1)