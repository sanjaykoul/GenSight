import pandas as pd

def aggregate_data(data_by_date):
    all_data = pd.concat(data_by_date.values(), keys=data_by_date.keys())
    all_data.reset_index(level=0, inplace=True)
    all_data.rename(columns={'level_0': 'Date'}, inplace=True)
    return all_data

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
