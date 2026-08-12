sentence = input()
position = int(input())

# Remove outer spaces and convert the sentence to lowercase
sentence = sentence.strip().lower()

# Replace the required punctuation marks with spaces
punct_list = [".", ",", "!", "?", ";", ":"]
for p in punct_list:
    sentence = sentence.replace(p, " ")

# Split the sentence into words and rebuild the cleaned sentence
words = sentence.split()
cleaned_sentence = " ".join(words)

# Extract the required words and slices
first_word = words[0]
last_word = words[-1]
selected_word = words[position - 1]

first_prefix = first_word[:3]
last_suffix = last_word[-3:]

# Display the complete analysis
print(f"Cleaned Sentence: {cleaned_sentence}")
print(f"Word Count: {len(words)}")
print(f"First Word: {first_word}")
print(f"Last Word: {last_word}")
print(f"Selected Word: {selected_word}")
print(f"First Word Prefix: {first_prefix}")
print(f"Last Word Suffix: {last_suffix}")