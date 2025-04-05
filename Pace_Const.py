import statistics

def pace_to_minutes(pace_str):
    try:
        minutes, seconds = map(int, pace_str.strip().split(":"))
        return minutes + seconds / 60
    except ValueError:
        return None

def minutes_to_pace(decimal_min):
    mins = int(decimal_min)
    secs = round((decimal_min - mins) * 60)
    if secs == 60:
        mins += 1
        secs = 0
    return f"{mins}:{secs:02d}"

def main():
    print("You can enter paces one at a time OR comma-separated (e.g. 7:10, 6:45, 7:00)")
    print("Press ENTER on a blank line to finish.\n")

    pace_list = []

    while True:
        user_input = input("Enter pace(s): ").strip()
        if user_input == "":
            break

        # Check for comma-separated input
        entries = user_input.split(",") if "," in user_input else [user_input]
        for pace_str in entries:
            pace_min = pace_to_minutes(pace_str)
            if pace_min is None:
                print(f"Invalid format: '{pace_str.strip()}'. Use mm:ss format.")
            else:
                pace_list.append(pace_min)

    if not pace_list:
        print("\nNo valid paces entered.")
        return

    mean_pace = statistics.mean(pace_list)
    variance = statistics.pvariance(pace_list) if len(pace_list) > 1 else 0
    stdev = statistics.stdev(pace_list) if len(pace_list) > 1 else 0

    print("\n--- Pace Summary ---")
    print(f"Entries: {len(pace_list)}")
    print(f"Mean Pace: {minutes_to_pace(mean_pace)}")
    print(f"Variance: {round(variance, 4)} min²")
    print(f"Standard Deviation: {minutes_to_pace(stdev)}")

if __name__ == "__main__":
    main()
