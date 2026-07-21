"""
Exception Handling Practice
-----------------------------
Demonstrates try / except / else / finally with multiple specific
except blocks, ordered from most specific to a generic fallback.
"""


def process_data(filename, divisor):
    file = None
    try:
        print(f"Trying to open file '{filename}':\n")
        file = open(filename, "r")
        data = file.read().strip()

        number = int(data)
        result = number / divisor
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except ValueError:
        print("Error: Could not convert file contents into an integer")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        # Only runs if no exception was raised
        print(f"Computed result: {result}")
    finally:
        # Always runs, whether or not an exception occurred
        if file:
            file.close()
            print("File closed successfully")
        print("Process execution cycle complete\n")


if __name__ == "__main__":
    # Set up a sample file so the script is runnable on its own
    with open("sample_input.txt", "w") as f:
        f.write("42")

    process_data("sample_input.txt", 7)     # normal case
    process_data("sample_input.txt", 0)     # ZeroDivisionError
    process_data("missing_file.txt", 1)     # FileNotFoundError

    with open("sample_input.txt", "w") as f:
        f.write("not a number")
    process_data("sample_input.txt", 1)     # ValueError

    import os
    os.remove("sample_input.txt")
