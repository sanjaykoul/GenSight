
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load Excel file
excel_path = "demo_file.xlsx"  # Update with your actual file path
xls = pd.ExcelFile(excel_path)

# Parse sheets with date-named tabs
data_frames = []
for sheet_name in xls.sheet_names:
    try:
        date = pd.to_datetime(sheet_name, format="%d-%m-%Y")
        df = xls.parse(sheet_name)
        df['Date'] = date
        data_frames.append(df)
    except ValueError:
        continue  # Skip non-date sheets

# Combine all sheets
combined_df = pd.concat(data_frames, ignore_index=True)

# Group by date to get issue counts
daily_summary = combined_df.groupby('Date').size().reset_index(name='Issue Count')

# Identify peak issue day
peak_day = daily_summary.loc[daily_summary['Issue Count'].idxmax()]

# Plot
plt.figure(figsize=(12, 6))
sns.barplot(data=daily_summary, x='Date', y='Issue Count', palette='Blues_d')
plt.axhline(peak_day['Issue Count'], color='red', linestyle='--', label=f"Peak Day: {peak_day['Date'].strftime('%d-%b-%Y')} ({peak_day['Issue Count']} issues)")
plt.xticks(rotation=45)
plt.title("Daily Issue Counts")
plt.xlabel("Date")
plt.ylabel("Number of Issues")
plt.legend()
plt.tight_layout()
plt.show()
