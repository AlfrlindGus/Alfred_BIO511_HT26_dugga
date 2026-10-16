import pandas as pd
import matplotlib.pyplot as plt
from plotnine import ggplot, aes, geom_point, ggtitle
import random
#Q1

name = 'Alfred'
letter ='A'
lettercount = 0

print(name)
print(len(name))

for x in range(len(name)): #loop turns x into each letter in the name
    if name[x] in letter: #checks if it matches the chosen letter
        lettercount += 1
print(str(lettercount) + str(letter))

#Q2

my_list = [1, 5, "4", "six", 3.14]

def clean_list(list_input): 
    new_list_func = []
    my_listnr = 1
      
    for entry in list_input: 
            try: #we try to append new_list with each entry converted into an integer
                new_list_func.append(int(entry))
                my_listnr += 1
            except:  #since int can only be a number, we expect it to reject anything containing a non-number
                print(f"ERROR: could not convert list entry number {my_listnr} into an integer(function edition)")
    return new_list_func

new_list_function = clean_list(my_list)
print(new_list_function)

#loop through list and use current instance with a var saving previous instance. Add these, then update previous instance for next loop
def sum_list(list_input):
    the_list = list_input
    previousn = None
    sum_list_fake = []
    for entry in the_list:
        if not previousn == None: #prevents messing up the first time it runs. Otherwise we'd get an extra 1 in the output
            sum_entry = entry + previousn
            sum_list_fake.append(sum_entry)
        previousn = entry
    return sum_list_fake

sum_list_real = sum_list(new_list_function)
print(sum_list_real)

#Q3

source_file = 'cnv_data.csv'
file_path_name = 'chromosome_1.png' #I'm just saving it in the same dir but you could specify a path
#read file into pandas dataframe
df = pd.read_csv(source_file)


plot = (
    ggplot(df, aes(x="position_mb", y="log2_ratio"))  
    + geom_point()                                              
    + ggtitle("Chromosome 1")                
)
plot.show()
plot.save(file_path_name, width=4, height=3,dpi=300) 



#Q4
#for range 1-20, Bob is random.randint(1,6) and Alice is random.randint(1,6) if Bob > Alice, add Bob to dict, if Alice < Bob, add Alice, else add draw.

record = {
'Bob': [],
'Alice' : [],
'Draw' : []
}


for match in range

                   