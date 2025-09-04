def generate_summary_text(daily_summary, weekly_summary, common_issues, engineer_workload):
    from datetime import datetime

    def format_date(date):
        if isinstance(date, pd.Timestamp):
            return date.strftime('%d-%b-%Y')
        return str(date)

    try:
        most_frequent_issue = f"{common_issues.iloc[0]['Issue Description']} ({common_issues.iloc[0]['Count']} occurrences)"
    except (KeyError, IndexError):
        most_frequent_issue = "No issue description available."

    try:
        top_engineer_name = engineer_workload.iloc[0]['Engineer Name']
        top_engineer_count = engineer_workload.iloc[0]['Issues Handled']
        top_engineer = f"{top_engineer_name} with {top_engineer_count} issues handled."
    except (KeyError, IndexError):
        top_engineer = "No engineer performance data available."

    try:
        peak_day = daily_summary.loc[daily_summary['Issue Count'].idxmax(), 'Date']
        peak_day_count = daily_summary['Issue Count'].max()
        avg_daily = round(daily_summary['Issue Count'].mean(), 2)
        trend = "increasing" if daily_summary['Issue Count'].iloc[-1] > daily_summary['Issue Count'].iloc[0] else "decreasing"
    except (KeyError, IndexError):
        peak_day = peak_day_count = avg_daily = trend = "Data unavailable"

    try:
        peak_week = weekly_summary.loc[weekly_summary['Issue Count'].idxmax(), 'Week']
        peak_week_count = weekly_summary['Issue Count'].max()
        avg_weekly = round(weekly_summary['Issue Count'].mean(), 2)
    except (KeyError, IndexError):
        peak_week = peak_week_count = avg_weekly = "Data unavailable"

    summary = f"""
    📊 **Daily Trends:**
    - Peak issue day: {format_date(peak_day)} with {peak_day_count} issues.
    - Average daily issues: {avg_daily}
    - Issue trend over time: {trend}

    📅 **Weekly Trends:**
    - Peak issue week: {format_date(peak_week)} with {peak_week_count} issues.
    - Average weekly issues: {avg_weekly}

    🛠️ **Common Issues:**
    - Most frequent issue: {most_frequent_issue}
    - Frequent issues may impact client satisfaction. Recommend prioritizing fixes or automation.

    🧑‍💻 **Engineer Performance:**
    - Top engineer: {top_engineer}
    - Consider reviewing workload balance if {top_engineer_name} consistently handles > {top_engineer_count} issues.

    ⚠️ **GenAI Insights:**
    - The issue volume shows a {trend} trend, indicating potential service strain.
    - {format_date(peak_day)} and week of {format_date(peak_week)} had unusually high issue volumes. Recommend root cause analysis.
    - Automation or SOP updates may help reduce recurrence of frequent issues like: {most_frequent_issue}.
    """

    return summary
