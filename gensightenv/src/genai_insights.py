def generate_summary_text(daily_summary, weekly_summary, engineer_workload, common_issues):
    try:
        most_frequent_issue = f"{common_issues.iloc[0]['Issue Description']} ({common_issues.iloc[0]['Count']} occurrences)"
    except (KeyError, IndexError):
        most_frequent_issue = "No issue description available."

    try:
        top_engineer = f"{engineer_workload.iloc[0]['Engineer Name']} with {engineer_workload.iloc[0]['Issues Handled']} issues handled."
        top_engineer_name = engineer_workload.iloc[0]['Engineer Name']
        top_engineer_count = engineer_workload.iloc[0]['Issues Handled']
    except (KeyError, IndexError):
        top_engineer = top_engineer_name = top_engineer_count = "Data unavailable"

    try:
        peak_day = daily_summary.loc[daily_summary['Issue Count'].idxmax(), 'Date']
        peak_day_count = daily_summary['Issue Count'].max()
        avg_daily = daily_summary['Issue Count'].mean()
        trend = "increasing" if daily_summary['Issue Count'].iloc[-1] > daily_summary['Issue Count'].iloc[0] else "decreasing"
    except (KeyError, IndexError):
        peak_day = peak_day_count = avg_daily = trend = "Data unavailable"

    try:
        peak_week = weekly_summary.loc[weekly_summary['Issue Count'].idxmax(), 'Week']
        peak_week_count = weekly_summary['Issue Count'].max()
        avg_weekly = weekly_summary['Issue Count'].mean()
    except (KeyError, IndexError):
        peak_week = peak_week_count = avg_weekly = "Data unavailable"

    summary = f"""
    📊 **Daily Trends:**
    - Peak issue day: {peak_day} with {peak_day_count} issues.
    - Average daily issues: {avg_daily:.2f}
    - Issue trend over time: {trend}

    📅 **Weekly Trends:**
    - Peak issue week: {peak_week} with {peak_week_count} issues.
    - Average weekly issues: {avg_weekly:.2f}

    ⚠️ **Operational Risk:**
    - High issue volume on {peak_day} may indicate a systemic or recurring problem.
    - Weekly peak ({peak_week}) should be reviewed for root cause analysis.

    🧑‍💻 **Engineer Performance:**
    - Top engineer: {top_engineer}
    - Consider reviewing workload balance if {top_engineer_name} consistently handles > {top_engineer_count} issues.

    🛠️ **Common Issues:**
    - Most frequent issue: {most_frequent_issue}
    - Frequent issues may impact client satisfaction. Recommend prioritizing fixes or automation.

    ✅ **Recommendations:**
    - Investigate peak periods for root causes.
    - Review engineer workload distribution.
    - Address top recurring issues to reduce future volume.
    - Consider automation or SOP updates for frequent issues.
    """

    return summary
