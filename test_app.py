from fitness_app import fitness_report

def test_fitness_report():
    expected_output = (
        "----- Fitness Report -----\n"
        "Name            : Niranjan\n"
        "Steps Taken     : 8000\n"
        "Calories Burned : 500\n"
        "Workout Time    : 30 minutes\n"
        "Fitness Score   : 160.00\n"
        "Fitness Level   : Excellent"
    )

    result = fitness_report("Niranjan", 8000, 500, 30)
    assert result == expected_output