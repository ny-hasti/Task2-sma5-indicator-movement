# ============================================
#create simple moving average in the dataframe
# without using predefined function use own logic
# ============================================
import pandas as pd

data = {
    'Date' : pd.date_range("2018-01-01", periods=15),
    'close':[100,102,104,106,108,200,201,202,203,204,205,207,208,300,302],
}

df=pd.DataFrame(data)

#---------------SmA_5 logic for 5 day average-----------
sma_value = []
#--------function--------
for i in range(len(df)):
    if i<4:#if  less than 5 value available
        sma_value.append(None)
    else:

        # store->sum of last 5 close
        Total = 0#start with 0
        for j in range(i-4,i+1):#(5-4,5+1)(1,6)so,(1,2,3,4,5)
            Total += df.loc[j,'close']#j= row num,close column name
        sma_value.append(Total/5)

df['SMA_5']=sma_value

# ---------------- Output ----------------
print(df[['Date','close','SMA_5']])
