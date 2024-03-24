from flask import Flask, render_template, request
from collections import Counter
import random
import time
from memory_profiler import profile, memory_usage

app = Flask(__name__)

def roll_dice(num_dice, num_sides):
    """
    Simulate rolling dice.

    Parameters:
    - num_dice (int): Number of dice to roll.
    - num_sides (int): Number of sides for each die.

    Returns:
    - list: A list containing the results of the dice rolls.
    """
    # Generate random numbers for specified number of dice with given number of sides
    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    return rolls

@app.route('/', methods=['GET', 'POST'])
def dice_rolling_simulator():
    if request.method == 'POST':
        num_dice = int(request.form['num_dice'])
        num_sides = int(request.form['num_sides'])

        # Measure the memory usage before rolling dice
        mem_usage_before = memory_usage()[0]

        # Measure the time taken for the roll
        start_time = time.time()

        # Roll the dice
        rolls = roll_dice(num_dice, num_sides)

        total_time = time.time() - start_time

        # Measure the memory usage after rolling dice
        mem_usage_after = memory_usage()[0]
        total_memory = mem_usage_after - mem_usage_before

        total = sum(rolls)

        # Update rolls history
        rolls_history = Counter(rolls)

        return render_template('index.html', result=True, num_dice=num_dice, num_sides=num_sides,
                               total=total, average_time_per_roll=total_time / num_dice,
                               average_memory_usage_per_roll=total_memory / num_dice,
                               rolls_history=rolls_history)
    else:
        return render_template('index.html', result=False)

if __name__ == "__main__":
    app.run(debug=True)