#!/usr/bin/env python3


def main() -> None:
    forecast = [
        (72, "Sunny"),
        (68, "Cloudy"),
        (70, "Partly Cloudy"),
        (65, "Rain"),
        (67, "Windy"),
        (73, "Thunderstorms"),
        (69, "Sunny"),
    ]

    for day_index, (temperature_fahrenheit, condition) in enumerate(forecast, start=1):
        print(f"Day {day_index}: {temperature_fahrenheit}°F {condition}")


if __name__ == "__main__":
    main()
