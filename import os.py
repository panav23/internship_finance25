from datetime import date, timedelta
from jugaad_data.nse import bhavcopy_save
import os


save_dir = "nse_bhavcopies"
os.makedirs(save_dir, exist_ok=True)


start_date = date(2014, 1, 1)
end_date = date.today()

current_date = start_date
while current_date <= end_date:
    try:
        
        bhavcopy_save(current_date, save_dir)
        print(f"Downloaded Bhavcopy for {current_date}")
    except Exception as e:
        print(f"Failed to download Bhavcopy for {current_date}: {e}")
    current_date += timedelta(days=1)