# Assignment 3: Sleep Time Tracker

This project is a Python program that tracks and analyzes daily sleep data over a specified number of days. It handles user inputs to collect sleep records, allows correcting data at a specific index, searches for specific data points, and outputs key metrics such as minimum, maximum, and total sleep times.

## Features

- **Dynamic Data Collection:** Prompts the user to enter data for any given number of days.
- **Data Modification:** Built-in `replace_value` function safely updates records at any user-specified index.
- **Data Searching:** Custom `find_first` function implements a linear search to find the index of a specific sleep target.
- **Statistical Analytics:** The `summarize` function analyzes the dataset to find the minimum, maximum, and total hours of sleep recorded.
- **Sorted View:** Outputs a clean, ascending-order representation of the updated data alongside the original entry sequence.

## Code Architecture

The program relies on three core helper functions to manage data mutation, searching, and computation:

1. `replace_value(values, index, new_value)`: Modifies the list element at the specific index.
2. `find_first(values, target)`: Performs a custom search returning the index of the first matching element, or `-1` if the target is not found.
3. `summarize(values)`: Returns a tuple containing the minimum, maximum, and sum total of the data structure.

## How to Run

1. Make sure you have **Python 3.x** installed on your machine.
2. Open your terminal or command prompt.
3. Run the script using the following command:
   ```bash
   python assignment3.py
   ```

## Example Run

### Input:
```text
Enter the number of days: 5
Enter sleep time in hours: 8
Enter sleep time in hours: 6
Enter sleep time in hours: 8
Enter sleep time in hours: 7
Enter sleep time in hours: 5
Enter the index to correct: 1
Enter the new sleep time: 8
Enter the sleep time to search for: 8
```

### Output:
```text
Original: [8, 6, 8, 7, 5]
Updated: [8, 8, 8, 7, 5]
Sorted: [5, 7, 8, 8, 8]
Minimum sleep time: 5 hours
Maximum sleep time: 8 hours
Total sleep time: 36 hours
First matching index: 0
Matching values: 3
```
