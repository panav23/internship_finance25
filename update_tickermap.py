import pandas as pd


masterPath  = r'C:\Users\User\OneDrive - Modern High School International\internship\momentum analysis\tick_map.csv'
historyPath = r'C:\Users\User\OneDrive - Modern High School International\internship\momentum analysis\symbolmap.csv'   # ← replace with your history filename

masterDf = pd.read_csv(masterPath, parse_dates=['Effective Date', 'Expiry Date'])

changesDf = pd.read_csv(
    historyPath,
    dtype={'CHANGE_DATE': 'string'}    
)


changesDf['CHANGE_DATE'] = pd.to_datetime(
    changesDf['CHANGE_DATE'],
    format='%d-%b-%y',   
    errors='coerce'      
)


print(changesDf['CHANGE_DATE'].head())

masterDf['ticker'] = masterDf['ticker'].str.strip().str.upper()
for col in ['OLD_TICKER', 'NEW_TICKER']:
    changesDf[col] = (changesDf[col]
                       .astype(str)
                       .str.strip()
                       .str.upper())


changesDf.sort_values('CHANGE_DATE', inplace=True)

for _, row in changesDf.iterrows():
    old, new, d = row['OLD_TICKER'], row['NEW_TICKER'], row['CHANGE_DATE']

    
    maskOld = masterDf['ticker'] == old
    if maskOld.any():
        ukeyOld = masterDf.loc[maskOld, 'UKEY'].iloc[0]
        masterDf.loc[maskOld, 'Expiry Date'] = d - pd.Timedelta(days=1)

    
        maskNew = masterDf['ticker'] == new
        if maskNew.any():
            masterDf.loc[maskNew, 'UKEY']   = ukeyOld
            masterDf.loc[maskNew, 'Effective Date'] = d
        else:
            newRow = {
                'UKEY'           : ukeyOld,
                'ticker'         : new,
                'Effective Date' : d,
                'Expiry Date'    : pd.Timestamp('2100-01-01')
            }
            newRow_df = pd.DataFrame([newRow])
            masterDf = pd.concat([masterDf, newRow_df], ignore_index=True)



masterDf.sort_values('UKEY', inplace=True)
masterDf.to_csv(masterPath, index=False)
