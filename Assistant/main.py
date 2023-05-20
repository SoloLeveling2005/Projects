import argparse
import json
import os
import time
from subprocess import run
from utils import process_dynamic_parts


def main():
    parser = argparse.ArgumentParser(description="Dynamic App Runner")
    parser.add_argument("dynamic_parts", nargs="+", help="Dynamic parts to be processed")
    args = parser.parse_args()

    dynamic_parts = args.dynamic_parts
    apps_data = load_apps_data()
    processed_parts = process_dynamic_parts(dynamic_parts)
    run_apps(processed_parts, apps_data)


def load_apps_data():
    try:
        with open(os.path.dirname(os.path.abspath(__file__))+"\\json_data\\apps.json", "r") as file:
            apps_data = json.load(file)
    except FileNotFoundError:
        print("Error: JSON file 'apps.json' not found.")
        exit(1)
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in 'apps.json' file.")
        exit(1)

    return apps_data


def run_apps(parts, apps_data):
    for part in parts:
        found = False
        for app_name, app_path in apps_data.items():
            part, app_name = part.lower(), app_name.lower()
            if part == app_name:
                time.sleep(2)
                run(app_path, shell=True)
                found = True
                break
        if not found:
            print(f"Error: Application '{part}' not found in the apps list.")


if __name__ == "__main__":
    main()

# os.path.dirname(os.path.abspath(__file__))+"\\labels"
