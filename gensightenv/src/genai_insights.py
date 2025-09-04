import pandas as pd

def generate_summary_text(daily_summary, weekly_summary, common_issues, engineer_workload):
    def format_date(date):
        if isinstance(date, pd.Timestamp):
            return date.strftime('%d-%b-%Y')
        return str(date)

    try:
        most_frequent_issue = f"{common_issues.iloc[0]['Issue Description']} ({common_issues.iloc[0]['Count']} occurrences)"
    except (KeyError, IndexError):
        most_frequent_issue = "Data unavailable"

    try:
        top_engineer_name = engineer_workload.iloc[0]['Engineer Name']
        top_engineer_count = engineer_workload.iloc[0]['Issues Handled']
        top_engineer = f"{top_engineer_name} with {top_engineer_count} issues handled."
    except (KeyError, IndexError):
        top_engineer = "Data unavailable"

    try:
        peak_day = daily_summary.loc[daily_summary['Issue Count'].idxmax(), 'Date']
        peak_day_count = daily_summary['Issue Count'].max()
        avg_daily = round(daily_summary['Issue Count'].mean(), 2)
        trend = "increasing" if daily_summary['Issue Count'].iloc[-1] > daily_summary['Issue Count'].iloc[0] else "decreasing"
    except (KeyError, IndexError, ValueError):
        peak_day = peak_day_count = avg_daily = trend = "Data unavailable"

    try:
        peak_week_row = weekly_summary.loc[weekly_summary['Issue Count'].idxmax()]
        peak_week_start = peak_week_row['Week Start']
        peak_week_end = peak_week_row['Week End']
        peak_week_count = peak_week_row['Issue Count']
        avg_weekly = round(weekly_summary['Issue Count'].mean(), 2)
    except (KeyError, IndexError, ValueError):
        peak_week_start = peak_week_end = peak_week_count = avg_weekly = "Data unavailable