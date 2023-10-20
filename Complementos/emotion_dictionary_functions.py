# Create a dictionary in the form {Word : [emotions]}
def generate_dictionary(file_path):
    dictionary = {}     # Dictionary of Spanish words and their emotions
    count = 0           # Count of word repetitions in the original file
    repeated_words = [] # List of repeated words in the original file (English_word, Spanish_word)
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        headers = lines[0].strip().split('\t')

        # Iterate over the rows in the file, excluding the header
        for line in lines[1:]:
            words = line.strip().split('\t')
            spanish_word = words[-1]
            values = words[1:-1]

            # List of emotions with value 1 in the row
            emotions = [("'" + headers[i + 1] + "'") for i in range(len(values)) if values[i] == '1']

            if len(emotions) == 0:
                continue
            elif spanish_word in dictionary:
                count += 1
                repeated_words.append((words[0], spanish_word))  # (English_word, Spanish_word)
                # Combine old values with new ones and remove duplicates
                dictionary[spanish_word] += emotions
                dictionary[spanish_word] = list(set(dictionary[spanish_word]))
            else:
                # Add the word and its array of emotions to the dictionary
                dictionary[spanish_word] = emotions

    return dictionary, count, repeated_words


# Create a .txt file with the estructure of a dictionary
def generate_dictionary_file(dictionary, output_file):
    with open(output_file, 'w') as file:
        file.write("{\n")
        for word, values in dictionary.items():
            line = f"'{word}': [{', '.join(values)}],\n"
            file.write(line)
        file.write("}\n")


#Create a .txt file 
def generate_repeated_words_file(repeated_words, output_file):
    with open(output_file, 'w') as file:
        for english_word, spanish_word in repeated_words:
            line = f"{english_word}\t{spanish_word}\n"
            file.write(line)


input_file = 'Spanish-NRC-EmoLex-V2.txt'
output_file = 'Dic-Spanish-NRC-V2.txt'
resulting_dictionary, count, repeated_words = generate_dictionary(input_file)
generate_dictionary_file(resulting_dictionary, output_file)

#Function Optional
generate_repeated_words_file(repeated_words,"Palabras-repetidas.txt") 
