import pandas as pd
import os
from glob import glob

folder_path= r'C:\Users\User\OneDrive - Modern High School International\internship\momentum analysis\nse_bhavcopies'
allFiles= sorted(glob(os.path.join(folder_path, '*.csv')))
priceData= []

for file in allFiles:
    date= os.path.basename(file).split('.')[0]
    df= pd.read_csv(file)
    df = df[['SYMBOL', 'CLOSE']].drop_duplicates(subset='SYMBOL').copy()

    df.rename(columns={'CLOSE': date}, inplace=True)
    priceData.append(df)

mergedData= priceData[0]
for df in priceData[1:]:
    mergedData= pd.merge(mergedData, df, on= 'SYMBOL', how= 'outer')

mergedData.set_index('SYMBOL', inplace=True)
mergedData= mergedData.sort_index(axis=1)
returnsDf = mergedData.pct_change(axis=1, fill_method=None)

returnsDf.to_csv("daily_Returns.csv")