import psutil


def get_battery_percent():
    battery = psutil.sensors_battery()
    if battery:
        return battery.percent
    else:
        return "Battery information not available."


if __name__ == "__main__":
    battery_percent = get_battery_percent()
    print(f"Battery Percentage: {battery_percent}%")
