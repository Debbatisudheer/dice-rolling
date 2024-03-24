from collections import Counter
import random
import time
from memory_profiler import profile, memory_usage


def roll_dice(num_dice, num_sides):
    # Generating random numbers for specified number of dice with given number of sides
    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    return rolls


@profile
def main():
    print("Welcome to the Dice Rolling Simulator!")
    total_rolls = 0
    rolls_history = Counter()
    total_time = 0
    total_memory = 0

    while True:
        num_dice = int(input("Enter the number of dice to roll: "))
        num_sides = int(input("Enter the number of sides for each die: "))

        # Measure the memory usage before rolling dice
        mem_usage_before = memory_usage()[0]

        # Measure the time taken for the roll
        start_time = time.time()

        # Roll the dice
        rolls = roll_dice(num_dice, num_sides)

        total_time += time.time() - start_time

        # Measure the memory usage after rolling dice
        mem_usage_after = memory_usage()[0]
        total_memory += mem_usage_after - mem_usage_before

        total = sum(rolls)

        # Update rolls history
        total_rolls += 1
        rolls_history.update(rolls)

        print("Total:", total)

        # Display performance analysis
        print("\nPerformance Analysis:")
        print("Average time per roll:", total_time / total_rolls if total_rolls > 0 else "N/A")
        print("Average memory usage per roll:", total_memory / total_rolls if total_rolls > 0 else "N/A")

        # Display statistics
        print("\nStatistics:")
        print("Total number of rolls:", total_rolls)
        print("Rolls History:")
        for roll, frequency in rolls_history.items():
            print(f"{roll}: {frequency} times")

        repeat = input("\nRoll again? (yes/no): ").lower()
        if repeat != 'yes':
            break


if __name__ == "__main__":
    main()