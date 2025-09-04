import matplotlib.pyplot as plt
import seaborn as sns

def plot_daily_summary(daily_summary):
    plt.figure(figsize=(10, 6))
    sns.barplot(data=daily_summary, x='Date', y='Issue Count', palette='Blues_d')
    plt.title('Daily Issue Count Overview', fontsize=14)
    plt.xlabel('Date')
    plt.ylabel('Number of Issues')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    for i, v in enumerate(daily_summary['Issue Count']):
        plt.text(i, v + 0.5, str(v), ha='center', fontsize=10)
    plt.tight_layout()
    plt.savefig('daily_issue_count.png')

def plot_weekly_summary(weekly_summary):
    plt.figure(figsize=(10, 6))
    sns.barplot(data=weekly_summary, x='Week', y='Issue Count', palette='Greens_d')
    plt.title('Weekly Issue Count Overview', fontsize=14)
    plt.xlabel('Week')
    plt.ylabel('Number of Issues')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    for i, v in enumerate(weekly_summary['Issue Count']):
        plt.text(i, v + 0.5, str(v), ha='center', fontsize=10)
    plt.tight_layout()
    plt.savefig('weekly_issue_count.png')

def plot_common_issues(common_issues):
    plt.figure(figsize=(8, 8))
    plt.pie(common_issues['Count'], labels=common_issues['Issue Description'],
            autopct='%1.1f%%', startangle=140)
    plt.title('Distribution of Top 10 Common Issues', fontsize=14)
    plt.tight_layout()
    plt.savefig('common_issues_pie.png')

def plot_engineer_workload(engineer_workload):
    plt.figure(figsize=(8, 8))
    plt.pie(engineer_workload['Issues Handled'], labels=engineer_workload['Engineer Name'],
            autopct='%1.1f%%', startangle=140)
    plt.title('Engineer Workload Distribution', fontsize=14)
    plt.tight_layout()
    plt.savefig('engineer_workload_pie.png')
