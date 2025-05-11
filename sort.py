import os
from datetime import datetime

folder = "nse_bhavcopies"  # Replace with your folder name

for filename in os.listdir(folder):
    if filename.startswith("cm") and filename.endswith(".csv"):
        try:
            # Extract '02Jan2014' from 'cm02Jan2014bhav.csv'
            date_part = filename[2:11]  # '02Jan2014'
            date_obj = datetime.strptime(date_part, "%d%b%Y")
            new_name = date_obj.strftime("%Y-%m-%d") + ".csv"

            old_path = os.path.join(folder, filename)
            new_path = os.path.join(folder, new_name)

            os.rename(old_path, new_path)
            print(f"Renamed: {filename} → {new_name}")
        except Exception as e:
            print(f"Skipping {filename}: {e}")