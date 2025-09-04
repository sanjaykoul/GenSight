import matplotlib.pyplot as plt
import seaborn as sns

def plot_daily_summary(daily_summary):
    plt.figure(figsize=(12, 6))
    sns.barplot(data=daily_summary, x='Date', y='Issue Count', palette='Blues')
    plt.title('Daily Issue Count Overview', fontsize=16, weight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Number of Issues', fontsize=12)
    plt.xticks(rotation=45, fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    for i, v in enumerate(daily_summary['Issue Count']):
        plt.text(i, v + 0.5, str(v), ha='center', fontsize=10, weight='bold')
    plt.tight_layout()
    plt.savefig('daily_issue_count.png')
    plt.close()

def plot_weekly_summary(weekly_summary):
    plt.figure(figsize=(12, 6))
    sns.barplot(data=weekly_summary, x='Week', y='Issue Count', palette='Greens')
    plt.title('Weekly Issue Count Overview', fontsize=16, weight='bold')
    plt.xlabel('Week', fontsize=12)
    plt.ylabel('Number of Issues', fontsize=12)
    plt.xticks(rotation=45, fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    for i, v in enumerate(weekly_summary['Issue Count']):
        plt.text(i, v + 0.5, str(v), ha='center', fontsize=10, weight='bold')
    plt.tight_layout()
    plt.savefig('weekly_issue_count.png')
    plt.close()

def plot_common_issues(common_issues):
    plt.figure(figsize=(8, 8))
    colors = plt.cm.Paired(range(len(common_issues)))
    wedges, texts, autotexts = plt.pie(
        common_issues['Count'],
        labels=common_issues['Issue Description'],
        autopct='%1.1f%%',
        startangle=140,
        colors=colors,
        wedgeprops={'edgecolor': 'white'}
    )
    for autotext in autotexts:
        autotext.set_fontsize(10)
        autotext.set_weight('bold')
    plt.title('Distribution of Top 10 Common Issues', fontsize=16, weight='bold')
    plt.tight_layout()
    plt.savefig('common_issues_pie.png')
    plt.close()

def plot_engineer_workload(engineer_workload):
    plt.figure(figsize=(8, 8))
    colors = plt.cm.Set3(range(len(engineer_workload)))
    wedges, texts, autotexts = plt.pie(
        engineer_workload['Issues Handled'],
        labels=engineer_workload['Engineer Name'],
        autopct='%1.1f%%',
        startangle=140,
        colors=colors,
        wedgeprops={'edgecolor': 'white'}
    )
    for autotext in autotexts:
        autotext.set_fontsize(10)
        autotext.set_weight('bold')
    plt.title('Engineer Workload Distribution', fontsize=16, weight='bold')
    plt.tight_layout()
    plt.savefig('engineer_workload_pie.png')
    plt.close()
