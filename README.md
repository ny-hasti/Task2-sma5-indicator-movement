# Task2-sma5-indicator-movement
# 📘 Simple Moving Average (SMA-5)
This script calculates a 5-day simple moving average **without using any built-in functions**

This code creates a DataFrame with dates and closing prices, then manually calculates the 5-day Simple Moving Average (SMA) without using built-in functions. For each row, it sums the previous 5 close values and divides by 5. The result is added as a new SMA_5 column.

# 🔹 Steps 

1. Create a DataFrame with Date and Close price.
2. Loop through each row in the DataFrame.
3. If less than 5 values are available → put None in SMA.
4. If 5 or more values available:
    ->Take the last 5 close prices
    ->Add them
    ->Divide by 5 → this is SMA-5
5.Store the SMA value in a list.
6.Add that list to a new column: SMA_5
7.Print/output the final table.

.

# 🔹 How it works?
- Loop through each row
- If 5 values are not available → SMA = None
- If 5 values available → take last 5 close prices
- Add them and divide by 5
- Store the result in a new column `SMA_5`

This shows how SMA can be calculated manually using basic Python logic and loops.
