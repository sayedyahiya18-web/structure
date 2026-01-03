import sys

def calculate_fitness_level(score):
    if score >= 90:
        return "Excellent"
    elif score >= 70:
        return "Very Good"
    elif score >= 50:
        return "Good"
    else:
        return "Needs Improvement"


def fitness_report(name, steps, calories, workout_time):
    fitness_score = (steps / 100) + (calories / 10) + workout_time
    level = calculate_fitness_level(fitness_score)

    report = (
        "----- Fitness Report -----\n"
        f"Name            : {name}\n"
        f"Steps Taken     : {steps}\n"
        f"Calories Burned : {calories}\n"
        f"Workout Time    : {workout_time} minutes\n"
        f"Fitness Score   : {fitness_score:.2f}\n"
        f"Fitness Level   : {level}"
    )
    return report


# CLI execution only (NOT during pytest import)
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python fitness_app.py Name Steps Calories WorkoutTime")
        sys.exit(1)

    name = sys.argv[1]
    steps = int(sys.argv[2])
    calories = int(sys.argv[3])
    workout_time = int(sys.argv[4])

    print(fitness_report(name, steps, calories, workout_time))
