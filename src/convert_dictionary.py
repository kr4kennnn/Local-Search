import csv

with open('data/imdb_1.csv', newline='', encoding="utf-8") as csvfile:                   #reading dataset
    reader = csv.reader(csvfile)
    with open('imdb_1_raw.txt', 'w', encoding="utf-8") as textfile:                 #writing it to the new text file
        for row in reader:
            textfile.write(row[0] + '\n')


with open('imdb_1_raw.txt', 'r', encoding="utf-8") as file:                         #reading the text file
    word_count = {}
    for line in file:
        words = line.split()                                                        #splitting the whole text to individual words
        for word in words:                                                          
            word_count[word] = word_count.get(word, 0) + 1                          #keeping word counts in a collection

sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)    #sorting word counts in a descending order

with open('dictionary_1.txt', 'w', encoding="utf-8") as file:                       #writing the collection to the dictionary file
    for i, (word, count) in enumerate(sorted_word_count):
        if i >= 100 and count >= 10:                                                #ignoring the first 100 words and counts less than 10
            file.write(f"{word} : {count}\n")