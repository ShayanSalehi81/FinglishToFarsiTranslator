from hazm import Lemmatizer
from collections import defaultdict

lemmatizer = Lemmatizer()


def process_text_file(file_path):
    lemmatized_freq = defaultdict(int)

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split()
            word = parts[0]
            freq = int(parts[1])

            lemma = lemmatizer.lemmatize(word).split('#')[0]

            lemmatized_freq[lemma] += freq

    return lemmatized_freq


def write_frequencies_to_file(frequencies, output_file):
    sorted_frequencies = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)

    with open(output_file, 'w', encoding='utf-8') as file:
        for word, freq in sorted_frequencies:
            file.write(f"{word}\t{freq}\n")
    print(f"Data written to {output_file}")


def delete_line(file_path, line_to_delete):
    """Deletes a specific line from a file."""
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if line_to_delete <= len(lines):
        lines.pop(line_to_delete - 1)

    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(lines)


input_file_path = 'persian-wikipedia.txt'
output_file_path = 'persian-wikipedia_lemmatized.txt'

# Process the file
frequencies = process_text_file(input_file_path)

# Write results to a new file
write_frequencies_to_file(frequencies, output_file_path)

# Remove bad formated lines
delete_line(output_file_path, 35)