
def generate_summaries(df):
    df['Week'] = df['Date'].dt.to_period('W').apply(lambda r: r.start_time)
    df['Month'] = df['Date'].dt.to_period('M').apply(lambda r: r.start_time)

    daily_summary = df.groupby('Date').size().reset_index(name='Issue Count')
    weekly_summary = df.groupby('Week').size().reset_index(name='Issue Count')
    monthly_summary = df.groupby('Month').size().reset_index(name='Issue Count')

    engineer_workload = df['Engineer Name'].value_counts().reset_index()
    engineer_workload.columns = ['Engineer Name', 'Issues Handled']

    common_issues = df['Issue Description'].value_counts().head(10).reset_index()
    common_issues.columns = ['Issue Description', 'Count']

    return daily_summary, weekly_summary, monthly_summary, engineer_workload, common_issues
