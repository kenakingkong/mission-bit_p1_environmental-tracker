"""
Part 2
- Define input prompts as string variables (prompt_meals and prompt_showers)
- Replace the direct input prompts with the new string variables
- Store calculations in constants (meal_impact, shower_impact, total_impact).
- Reformat output message with stored calculation variables using the format() method.
- Test code.
"""

# todo, missing the meals environmental prompts

TOTAL_WEEKLY_SHOWERS_PROMPT = "How many showers do you take per week? "
AVG_SHOWER_LENGTH_PROMPT = "How long are your showers (in minutes)? "
TOTAL_DAILY_MEALS_PROMPT = "How many meals do you eat in a day? "

WATER_USED_PER_SHOWER = 2  # avg 2g water used per 1min shower

def main():
    total_weekly_showers = input(TOTAL_WEEKLY_SHOWERS_PROMPT)
    avg_shower_length = input(AVG_SHOWER_LENGTH_PROMPT)

    weekly_water_usage = int(total_weekly_showers) * (int(avg_shower_length) * WATER_USED_PER_SHOWER)

    print("\nYou shower {} times per week and take {} minute long showers".format(total_weekly_showers, avg_shower_length))
    print("This means you use {} gallons of water in a week\n".format(weekly_water_usage))


    total_daily_meals = input(TOTAL_DAILY_MEALS_PROMPT)

    # do calculation here???

    print("You eat {} meals in a day".format(total_daily_meals))
    print("This means you use ___ of ___ in a week".format(total_daily_meals))

    return


if __name__ == "__main__":
    main()
