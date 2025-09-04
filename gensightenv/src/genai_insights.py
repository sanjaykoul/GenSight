def generate_summary_text(daily_summary, weekly_summary, engineer_workload, common_issues):
    try:
        most_frequent_issue = f"{common_issues.iloc[0]['Issue Description']} ({common_issues.iloc[0]['Count']} occurrences)"
    except (KeyError, IndexError):
        most_frequent_issue = "No issue description available."

    try:
        top_engineer = f"{engineer_workload.iloc[0]['Engineer Name']} with {engineer_workload.iloc[0]['Issues Handled']} issues handled."
    except (KeyError, IndexError):
        top_engineer = "No engineer performance data available."

    try:
        peak_day = daily_summary.loc[daily_summary['Issue Count'].idxmax(), 'Date']
        peak_day_count = daily_summary['Issue Count'].max()
        avg_daily = daily_summary['Issue Count'].mean()
    except (KeyError, IndexError):
        peak_day = peak_day_count = avg_daily = "Data unavailable"

    try:
        peak_week = weekly_summary.loc[weekly_summary['Issue Count'].idxmax(), 'Week']
        peak_week_count = weekly_summary['Issue Count'].max()
        avg_weekly = weekly_summary['Issue Count'].mean()
    except (KeyError, IndexError):
        peak_week = peak_week_count = avg_weekly = "Data unavailable"

    summary = f"""
    Daily Trends:
    - Peak issue day: {peak_day} with {peak_day_count} issues.
    - Average daily issues: {avg_daily}

    Weekly Trends:
    - Peak issue week: {peak_week} with {peak_week_count} issues.
    - Average weekly issues: {avg_weekly}

    Common Issues:
    - Most frequent issue: {most_frequent_issue}

    Engineer Performance:
    - Top engineer: {top_engineer}
    """
    return summary
