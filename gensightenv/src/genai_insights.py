def generate_summary_text(daily_summary, weekly_summary, engineer_workload, common_issues):
    summary = f"""
    Daily Trends:
    - Peak issue day: {daily_summary.loc[daily_summary['Issue Count'].idxmax(), 'Date']} with {daily_summary['Issue Count'].max()} issues.
    - Average daily issues: {daily_summary['Issue Count'].mean():.2f}

    Weekly Trends:
    - Peak issue week: {weekly_summary.loc[weekly_summary['Issue Count'].idxmax(), 'Week']} with {weekly_summary['Issue Count'].max()} issues.
    - Average weekly issues: {weekly_summary['Issue Count'].mean():.2f}

    Common Issues:
    - Most frequent issue: {common_issues.iloc[0]['Issue Description']} ({common_issues.iloc[0]['Count']} occurrences)
    
    Engineer Performance:
    - Top engineer: {engineer_workload.iloc[0]['Engineer Name']} with {engineer_workload.iloc[0]['Issues Handled']} issues handled.
    """

    return summary

