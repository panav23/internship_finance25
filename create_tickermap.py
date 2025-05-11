import pandas as pd
import os
from glob import glob

dataFolder = r'C:\Users\User\OneDrive - Modern High School International\internship\momentum analysis\nse_bhavcopies'
filePaths = glob(os.path.join(dataFolder, '*.csv'))


uniqueTickers= set()
for filepath in filePaths:
    df= pd.read_csv(filepath)
    tickers= df['SYMBOL'].unique()
    uniqueTickers.update(tickers)

tickerList= list(uniqueTickers)
tickerList.sort()

effectiveDate = pd.Timestamp('1990-01-01')
expiryDate= pd.Timestamp('2100-01-01')

records = []
idCount= 1
for ticker in tickerList:
    records.append({
        'UKEY': f"{idCount:04d}",
        'ticker': ticker,
        'Effective Date': effectiveDate,
        'Expiry Date': expiryDate
    })
    idCount+= 1

print("Total unique tickers found:", len(uniqueTickers))
print("Sample tickers:", list(uniqueTickers)[:10])


FinalDf = pd.DataFrame(records)
FinalDf.to_csv('tick_map.csv', index=False)


          