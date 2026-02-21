"""
Part 1
- Write a method that prompts the user to enter the number of showers they take per week.
- Write a method that prompts the user to enter how long their average showers are.
- Define a constant for average water usage per shower.
- Calculate and print the total water consumption based on the user input.
- Use Python’s string formatting to neatly label and display the water consumption results.
- Test code.
"""

WATER_USED_PER_SHOWER = 2  # avg 2g water used per 1min shower

def main():
    total_weekly_showers = input("How many showers do you take per week? ")
    avg_shower_length = input("How long are your showers (in minutes)? ")
    weekly_water_usage = int(total_weekly_showers) * (int(avg_shower_length) * WATER_USED_PER_SHOWER)

    # print("\nOn average, you take " + avg_shower_length + " minute long showers, " + total_weekly_showers + " times per week\n")
    print("\nYou shower {} times per week and take {} minute long showers".format(total_weekly_showers, avg_shower_length))
    print("This means you use {} gallons of water a week\n".format(weekly_water_usage))

    return


if __name__ == "__main__":
    main()
