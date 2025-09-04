
import matplotlib.pyplot as plt
import seaborn as sns

def plot_daily_summary(daily_summary):
    plt.figure(figsize=(10, 5))
    sns.barplot(data=daily_summary, x='Date', y='Issue Count')
    plt.title('Daily Issue Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('daily_issue_count.png')

def plot_engineer_workload(engineer_workload):
    plt.figure(figsize=(8, 5))
    sns.barplot(data=engineer_workload, x='Engineer Name', y='Issues Handled')
    plt.title('Engineer Workload')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('engineer_workload.png')

def plot_common_issues(common_issues):
    plt.figure(figsize=(10, 5))
    sns.barplot(data=common_issues, x='Issue Description', y='Count')
    plt.title('Top 10 Common Issues')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('common_issues.png')
