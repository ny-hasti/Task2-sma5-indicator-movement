# Task2-sma5-indicator-movement
# 📘 Simple Moving Average (SMA-5)
This script calculates a 5-day simple moving average **without using any built-in functions**

This code creates a DataFrame with dates and closing prices, then manually calculates the 5-day Simple Moving Average (SMA) without using built-in functions. For each row, it sums the previous 5 close values and divides by 5. The result is added as a new SMA_5 column.
# Steps 

**1. Prepare data** — make a DataFrame df with columns Date and close.

**2. Create output container** — make an empty list sma_value to hold the SMA values (one per row).

**3. Loop through rows** — for each row index i from 0 to len(df)-1:

  **->**If there are fewer than 5 previous values (i.e. i < 4) append None (or numpy.nan) because a 5-day average can't be             computed yet.

  **->**Otherwise compute the sum of the last 5 close values (indices i-4 through i) and divide by 5 to get the SMA. Append
            that average to sma_value.

**5. Attach result to DataFrame** — set df['SMA_5'] = sma_value.

**6. (Optional cleanup)** — convert None to NaN, round results, or use pd.Series(sma_value).astype(float) if needed.
