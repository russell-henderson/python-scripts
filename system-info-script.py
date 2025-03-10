import psutil
import platform
import socket
import pandas as pd
import matplotlib.pyplot as plt
import os


def get_system_info():
    info = {
        'OS': platform.system(),
        'OS Version': platform.version(),
        'OS Release': platform.release(),
        'Architecture': platform.architecture()[0],
        'Hostname': socket.gethostname(),
        'IP Address': socket.gethostbyname(socket.gethostname()),
        'CPU Cores': psutil.cpu_count(logical=True),
        'CPU Usage (%)': psutil.cpu_percent(interval=1),
        'RAM Total (GB)': round(psutil.virtual_memory().total / (1024 ** 3), 2),
        'RAM Available (GB)': round(psutil.virtual_memory().available / (1024 ** 3), 2),
        'RAM Used (GB)': round(psutil.virtual_memory().used / (1024 ** 3), 2),
        'Disk Usage (%)': psutil.disk_usage('/').percent,
        'Disk Total (GB)': round(psutil.disk_usage('/').total / (1024 ** 3), 2),
        'Disk Used (GB)': round(psutil.disk_usage('/').used / (1024 ** 3), 2),
        'Disk Free (GB)': round(psutil.disk_usage('/').free / (1024 ** 3), 2)
    }
    return info


def display_info(info):
    print("\n--- System Information ---")
    df = pd.DataFrame(list(info.items()), columns=['Component', 'Value'])
    print(df.to_string(index=False))


def export_to_csv(info):
    df = pd.DataFrame(list(info.items()), columns=['Component', 'Value'])
    df.to_csv('system_info.csv', index=False)
    print("\nSystem information exported to 'system_info.csv'.")


def plot_usage(info):
    components = ['CPU Usage (%)', 'RAM Used (GB)', 'Disk Usage (%)']
    values = [info['CPU Usage (%)'], info['RAM Used (GB)'],
              info['Disk Usage (%)']]

    plt.figure(figsize=(10, 5))
    plt.bar(components, values, color=['blue', 'green', 'orange'])
    plt.title('System Resource Usage')
    plt.ylabel('Usage')
    plt.ylim(0, max(values) + 10)

    for i, value in enumerate(values):
        plt.text(i, value + 0.5, str(value), ha='center')

    plt.savefig('system_usage.png')
    plt.show()


def performance_suggestions(info):
    print("\n--- Performance Suggestions ---")
    if info['RAM Available (GB)'] < 2:
        print("- Consider upgrading your RAM for better performance.")
    if info['Disk Usage (%)'] > 90:
        print("- Your disk space is running low. Consider clearing up some space.")
    if info['CPU Usage (%)'] > 80:
        print("- Your CPU is under heavy load. Check for resource-heavy applications.")
    if info['RAM Used (GB)'] > info['RAM Total (GB)'] * 0.8:
        print("- You are using a significant amount of RAM. Closing unused applications may help.")


def main():
    system_info = get_system_info()
    display_info(system_info)
    export_to_csv(system_info)
    plot_usage(system_info)
    performance_suggestions(system_info)


if __name__ == "__main__":
    main()
