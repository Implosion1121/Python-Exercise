# Open the input file for reading
with open("file_to_read.txt", "r") as input_file:
    text = input_file.read()

# Calculate the total occurrences of "terrible"
total_terrible_count = text.count("terrible")

# Split the text into words
words = text.split()

# Initialize a variable to keep track of the current count
current_count = 0

# Iterate through the words and replace "terrible" accordingly
for i in range(len(words)):
    if words[i] == "terrible":
        current_count += 1
        if current_count % 2 == 0:
            words[i] = "pathetic"
        else:
            words[i] = "marvelous"

# Join the words back into a single text
new_text = " ".join(words)
new_text = new_text.replace("terrible!", "marvellous!")
# Write the new text to the result file
with open("result.txt", "w") as result_file:
    result_file.write(new_text)

# Display the total count of "terrible"
print("Total occurrences of 'terrible':", total_terrible_count)