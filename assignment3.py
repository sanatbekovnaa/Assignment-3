def replace_value(values, index, new_value):
    values[index] = new_value
    return None

def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1

def summarize(values):
    return (min(values), max(values), sum(values))


num_days = int(input("Enter the number of days: "))
original = []
for _ in range(num_days):
    sleep_time = int(input("Enter sleep time in hours: "))
    original.append(sleep_time)


updated = original[:]
idx = int(input("Enter the index to correct: "))
new_sleep = int(input("Enter the new sleep time: "))
replace_value(updated, idx, new_sleep)
target = int(input("Enter the sleep time to search for: "))
first_index = find_first(updated, target)
target_count = updated.count(target)
minimum, maximum, total = summarize(updated)
sorted_list = sorted(updated)


print(f"\nOriginal: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted_list}")
print(f"Minimum sleep time: {minimum} hours")
print(f"Maximum sleep time: {maximum} hours")
print(f"Total sleep time: {total} hours")

if first_index == -1:
    print("First matching index: Target not found")
else:
    print(f"First matching index: {first_index}")


print(f"Matching values: {target_count}")
