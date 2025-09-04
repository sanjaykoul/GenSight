def generate_summary_text(daily_summary, weekly_summary, common_issues, engineer_workload):
    from datetime import datetime

    def format_date(date_obj):
        if isinstance(date_obj, str):
            try:
                date_obj = datetime.strptime(date_obj, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                return str(date_obj)
        return date_obj.strftime("%B %d, %Y")

    try:
        most_frequent_issue = f"{common_issues.iloc[0]['Issue Description']} — occurred {common_issues.iloc[0]['Count']} times."
    except (KeyError, IndexError):
        most_frequent_issue = "No issue description available."

    try:
        top_engineer = f"{engineer_workload.iloc[0]['Engineer Name']} handled {engineer_workload.iloc[0]['Issues Handled']} issues."
    except (KeyError, IndexError):
        top_engineer = "No engineer performance data available."

    try:
        peak_day = format_date(daily_summary.loc[daily_summary['Issue Count'].idxmax(), 'Date'])
        peak_day_count = int(daily_summary['Issue Count'].max())
        avg_daily = round(daily_summary['Issue Count'].mean(), 1)
    except (KeyError, IndexError):
        peak_day = peak_day_count = avg_daily = "Data unavailable"

    try:
        peak_week = format_date(weekly_summary.loc[weekly_summary['Issue Count'].idxmax(), 'Week'])
        peak_week_count = int(weekly_summary['Issue Count'].max())
        avg_weekly = round(weekly_summary['Issue Count'].mean(), 1)
    except (KeyError, IndexError):
        peak_week = peak_week_count = avg_weekly = "Data unavailable"

    summary = f"""
### 📊 Issue Tracker Summary

**Daily Trends:**
- 📅 **Peak issue day:** {peak_day} with **{peak_day_count} issues**.
- 📈 **Average daily issues:** Approximately **{avg_daily} issues** per day.

**Weekly Trends:**
- 📅 **Peak issue week:** Starting {peak_week} with **{peak_week_count} issues**.
- 📈 **Average weekly issues:** Around **{avg_weekly} issues** per week.

**Common Issues:**
- ⚠️ **Most frequent issue:** {most_frequent_issue}

**Engineer Performance:**
- 🛠️ **Top engineer:** {top_engineer}
"""
    return summary
