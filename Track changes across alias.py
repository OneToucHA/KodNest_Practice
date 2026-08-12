value_count = int(input())
original_list = []

# Read and store all values using append()
for _ in range(value_count):
    original_list.append(int(input()))

# Create an alias and a shallow copy
alias_list = original_list
copied_list = original_list.copy()

alias_position = int(input())
alias_value = int(input())
copy_position = int(input())
copy_value = int(input())

# Update one value through the alias
alias_list[alias_position - 1] = alias_value

# Update one value in the copied list
copied_list[copy_position - 1] = copy_value

# Count how many positions contain different values
different_positions = 0
for index in range(value_count):
    if original_list[index] != copied_list[index]:
        different_positions += 1

# Print output exactly as formatted
print(f"Original List: {original_list}")
print(f"Alias List: {alias_list}")
print(f"Copied List: {copied_list}")

if alias_list is original_list:
    print("Alias Shares Original: Yes")
else:
    print("Alias Shares Original: No")

print(f"Different Positions: {different_positions}")