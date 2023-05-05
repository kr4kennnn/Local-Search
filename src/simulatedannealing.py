import csv
import matplotlib.pyplot as plt 
import random
import seaborn as sns 
import math

def classify(indv):
    correctCount = 0
    with open('data/imdb_1.csv', newline='', encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:                                              #iterating through row by row
            first_col = row[0]                                          #review column
            second_col = row[1]                                         #sentiment column
            words = first_col.split()                                   #assigning review column to words
            sentiment = second_col.split()[0]                           #assigning sentiment column to a variable
            countGood = 0
            countBad = 0
            for word in words:                                          #iterating through all the words in the review column of one row
                for i in range(N//2):                                   #first half of indv for good sentiments
                    if (indv[i] == word):
                        countGood += 1

                for i in range(N//2, N):                                #second half of indv for bad sentiments
                    if (indv[i] == word):
                        countBad += 1

            if (countGood > countBad):                                  #compare the good and bad words' match count and assign a class
                classifyAs = "positive"
            elif (countGood < countBad):
                classifyAs = "negative"
            else:
                classifyAs = random.choice(["positive", "negative"])    #randomize if equal
            if (sentiment == classifyAs):
                correctCount += 1

    return correctCount / 5000                                          #calculate precision by dividing by review count


N = 6                                                                   #assigning the length of the individual
indv = [None] * N                                                       #initialize
with open('dictionary_1.txt', 'r', encoding="utf-8") as f:              #read the dictionary file
    lines = f.readlines()
    for i in range(N):
        indv[i] = random.choice(lines).split()[0]                       #randomly assign a word  to the individual


precision = classify(indv)                                              #calculate precision
precisionA = []                                                         #precision array for plotting
precisionA.append(precision)
print(indv)                                                             #print randomly assigned first individual and precision
print(precision)

indvCount = 1
bestIndex = indvCount                                                   #assigning the first individual's index to the best one
bestP = precision                                                       #assigning the first individual's precison to the best one
bestI = indv[:]                                                         #assigning the first individual as the best

for i in range(N):                                                      #for every element of individual
    t=1
    while True:
        with open('dictionary_1.txt', 'r', encoding="utf-8") as f:      #read the dictionary file
            lines = f.readlines()
            T= 1 * 0.5**t                                               #probability formula
            if round(T,4)==0:                                           #breaking the loop if T is equal to 0
                break
            rand = random.choice(lines).split()[0]                      #randomly assign a word from the dictionary to a variable
            nextI = indv[:]                                             #copying the original individual to the new list
            nextI[i] = rand                                             #changing the i-th element of new list to the random word 
            NeighborR = classify(nextI)                                 #calculating the new precision
            if NeighborR > precision :
                indv = nextI[:]                                         #change the original individual if there is an improvement
                precision = NeighborR                                   #assign new precision
                indvCount += 1                                          #increase the number of individuals
                if(NeighborR > bestP):                                  #check the new precision against the best one
                    bestP = precision                                   #change the best individual if the new precision is bigger
                    bestI = indv[:]
                    bestIndex = indvCount                               #keep the index
                print("\n")                                             #prints for visualising every changed element of individual
                print(indv) 
                print(precision)                
                precisionA.append(precision)                  
            else :
                prob = math.e ** (( NeighborR - precision )/T)          #calculate the probability for simulated annealing
                p= random.uniform(0,1)
                if p < prob :                                           #accept the worse precision anyway if the condition is satisfied
                    indv = nextI[:]
                    precision = NeighborR
                    indvCount +=1
                    print("\n")
                    print(indv)
                    print(precision)
                    precisionA.append(precision)
            t+=1

print("Best result is individual is: Ind #" + str(bestIndex))           #printing the best individual
print(bestI)
print("with a precision of: " + str(bestP))

x = list(range(1, indvCount+1))                                         #plotting precisions for every individual
sns.lineplot(x=x, y=precisionA, marker='o', linestyle='-')
plt.xlabel('Individual Count')
plt.ylabel('Precision')
plt.title('Precision by individuals')

plt.show()