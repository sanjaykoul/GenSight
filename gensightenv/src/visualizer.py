import matplotlib.pyplot as plt
import seaborn as sns

def plot_daily_summary(daily_summary):
    plt.figure(figsize=(10, 5))
    sns.barplot(data=daily_summary, x='Date', y='Issue Count')
    plt.title('Daily Issue Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('daily_issue_count.png')

def plot_weekly_summary(weekly_summary):
    plt.figure(figsize=(10, 5))
    sns.barplot(data=weekly_summary, x='Week', y='Issue Count')
    plt.title('Weekly Issue Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('weekly_issue_count.png')

def plot_common_issues(common_issues):
    plt.figure(figsize=(8, 8))
    plt.pie(common_issues['Count'], labels=common_issues['Issue Description'], autopct='%1.1f%%')
    plt.title('Top 10 Common Issues')
    plt.tight_layout()
    plt.savefig('common_issues_pie.png')

def plot_engineer_workload(engineer_workload):
    plt.figure(figsize=(8, 8))
    plt.pie(engineer_workload['Issues Handled'], labels=engineer_workload['Engineer Name'], autopct='%1.1f%%')
    plt.title('Engineer Workload')
    plt.tight_layout()
    plt.savefig('engineer_workload_pie.png')
