import os
from datetime import datetime

folder = "nse_bhavcopies"

for filename in os.listdir(folder):
    if filename.startswith("cm") and filename.endswith(".zip"):
        date_str = filename[2:10]  # Extract DDMMYYYY
        date_obj = datetime.strptime(date_str, "%d%m%Y")
        new_name = date_obj.strftime("%Y-%m-%d") + ".zip"
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))