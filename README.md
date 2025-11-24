# Task2-sma5-indicator-movement
This code creates a DataFrame with dates and closing prices, then manually calculates the 5-day Simple Moving Average (SMA) without using built-in functions. For each row, it sums the previous 5 close values and divides by 5. The result is added as a new SMA_5 column.

***1️⃣ Create a DataFrame***

We first create a DataFrame with:
Date Column
Close Price Column

data = {
    'Date' : pd.date_range("2018-01-01", periods=15),
    'close':[100,102,104,106,108,200,201,202,203,204,205,207,208,300,302],
}
df = pd.DataFrame(data)

**2️⃣ Create an empty list to store SMA values**
sma_value = []

**3️⃣ Loop through each row using i**
If less than 5 values are available (i < 4), SMA cannot be calculated → store None.

When 5 values are available, calculate SMA manually.

for i in range(len(df)):
    if i < 4:
        sma_value.append(None)
    else:
        Total = 0
        # Calculate sum of last 5 values
        for j in range(i-4, i+1):
            Total += df.loc[j, 'close']
        sma_value.append(Total / 5)

**4️⃣ Add the SMA list to the DataFrame**
   df['SMA_5'] = sma_value

**5️⃣ Print the output**
print(df[['Date','close','SMA_5']])

📌 Example Output
         Date  close  SMA_5
0  2018-01-01    100   NaN
1  2018-01-02    102   NaN
2  2018-01-03    104   NaN
3  2018-01-04    106   NaN
4  2018-01-05    108   104.0
5  2018-01-06    200   124.0
...
