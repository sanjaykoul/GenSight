
def generate_summary_text(daily_summary, engineer_workload, common_issues):
    summary = f"""
    Daily Trends:
    - Peak issue day: {daily_summary.loc[daily_summary['Issue Count'].idxmax(), 'Date']} with {daily_summary['Issue Count'].max()} issues.
    - Average daily issues: {daily_summary['Issue Count'].mean():.2f}

    Engineer Performance:
    - Top engineer: {engineer_workload.iloc[0]['Engineer Name']} with {engineer_workload.iloc[0]['Issues Handled']} issues handled.

    Common Issues:
    - Most frequent issue: {common_issues.iloc[0]['Issue Description']} ({common_issues.iloc[0]['Count']} occurrences)
    """
    return summary
