# Task2-sma5-indicator-movement
# 📘 Simple Moving Average (SMA-5)
This script calculates a 5-day simple moving average **without using any built-in functions**

This code creates a DataFrame with dates and closing prices, then manually calculates the 5-day Simple Moving Average (SMA) without using built-in functions. For each row, it sums the previous 5 close values and divides by 5. The result is added as a new SMA_5 column.
# Steps 

**1. Prepare data** — make a DataFrame df with columns Date and close.

**2. Create output container** — make an empty list sma_value to hold the SMA values (one per row).

**3. Loop through rows** — for each row index i from 0 to len(df)-1:

   ->If there are fewer than 5 previous values (i.e. i < 4) append None (or numpy.nan) because a 5-day average can't be             computed yet.

   ->Otherwise compute the sum of the last 5 close values (indices i-4 through i) and divide by 5 to get the SMA. Append
            that average to sma_value.

**5. Attach result to DataFrame** — set df['SMA_5'] = sma_value.

**6. (Optional cleanup)** — convert None to NaN, round results, or use pd.Series(sma_value).astype(float) if needed.

# Working steps 
'''
Given close = [100,102,104,106,108,200,201,202,203,204,205,207,208,300,302]

Indices: 0..14.

For i = 0,1,2,3 → fewer than 5 values → SMA_5 = None.

For i = 4 (5th row): sum of indices 0..4

Step sums: 100 + 102 = 202
202 + 104 = 306
306 + 106 = 412
412 + 108 = 520

Total = 520. Average = 520 / 5 = 104.0 → SMA_5 = 104.0

For i = 5: indices 1..5 → 102 + 104 + 106 + 108 + 200

102 + 104 = 206
206 + 106 = 312
312 + 108 = 420
420 + 200 = 620

Avg = 620 / 5 = 124.0 → SMA_5 = 124.0

For i = 6: indices 2..6 → 104 + 106 + 108 + 200 + 201

104 + 106 = 210
210 + 108 = 318
318 + 200 = 518
518 + 201 = 719

Avg = 719 / 5 = 143.8 → SMA_5 = 143.8

For i = 7: indices 3..7 → 106 + 108 + 200 + 201 + 202 = 817 → 817/5 = 163.4

For i = 8: indices 4..8 → 108 + 200 + 201 + 202 + 203 = 914 → 914/5 = 182.8

For i = 9: indices 5..9 → 200 + 201 + 202 + 203 + 204 = 1010 → 1010/5 = 202.0

For i = 10: 201 + 202 + 203 + 204 + 205 = 1015 → 1015/5 = 203.0

For i = 11: 202 + 203 + 204 + 205 + 207 = 1021 → 1021/5 = 204.2

For i = 12: 203 + 204 + 205 + 207 + 208 = 1027 → 1027/5 = 205.4

For i = 13: indices 9..13 → 204 + 205 + 207 + 208 + 300

204 + 205 = 409
409 + 207 = 616
616 + 208 = 824
824 + 300 = 1124

Avg = 1124 / 5 = 224.8 → big jump because of 300.

For i = 14: indices 10..14 → 205 + 207 + 208 + 300 + 302

205 + 207 = 412
412 + 208 = 620
620 + 300 = 920
920 + 302 = 1222

Avg = 1222 / 5 = 244.4

**Resulting table** (Date, close, SMA_5)
index	close	SMA_5
0	100	None
1	102	None
2	104	None
3	106	None
4	108	104.0
'''
