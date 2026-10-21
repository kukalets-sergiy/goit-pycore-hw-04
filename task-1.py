"""
Calculate total and average developer salaries from a text file.
Used with a month_dev_salary.txt file containing developer names and salaries in the format: "developer name,salary".
"""


def total_salary(path):
    """Return the total and average salary stored in ``path``.

    Each non-empty line must contain ``developer name,salary``.
    """
    # Initialize total salary and developer count
    total = 0
    developers = 0

    try:
        # Read the file
        with open(path, encoding="utf-8") as file:
            # Loop through each line in the file, starting the line number count at 1
            for line_number, line in enumerate(file, start=1):
                # Strip whitespace from the line
                line = line.strip()
                # Skip empty lines
                if not line:
                    continue

                try:
                    # Split the line into name and salary
                    _, salary = line.split(",", maxsplit=1) # maxsplit=1 ensures we only split on the first comma
                    # Strip whitespace from the salary and convert it to an integer, adding it to the total
                    total += int(salary.strip())
                # Handle errors if the line is not formatted correctly or the salary is not a valid integer
                except (ValueError, TypeError) as error:
                    # Raise a ValueError with a message indicating the line number of the invalid record
                    raise ValueError(
                        f"Invalid salary record on line {line_number}"
                    ) from error
                # Increment the developer count
                developers += 1
    # Handle the case where the file does not exist
    except FileNotFoundError:
        # Return 0 for both total and average if the file is not found
        return 0, 0

    average = total / developers if developers else 0
    return total, average

#  Assign the result of total_salary to total and average, and print the results
total_sal, average_sal = total_salary("month_dev_salary.txt")
print(f"Загальна сума заробітної плати: {total_sal}, Середня заробітна плата: {average_sal}")
# Загальна сума заробітної плати: 6000, Середня заробітна плата: 2000.0
