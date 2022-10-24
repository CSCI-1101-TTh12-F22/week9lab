### Data Structures

## Basic

# Create a dictionary that map months to the number of days they have.
# Then print out each key-value pair on its own line.

c1 = 31
c2 = 30
c3 = 28

months = {"Jan":c1, "Mar":c1, "May":c1, "July":c1, "Aug":c1, "Oct":c1,
          "Dec":c1, "Apr":c2, "Jun":c2, "Sept":c2, "Nov":c2, "Feb":c3}

for k,v in months.items():
    print(k, "has", v, "days in non-leap years")



# Create a set of 10 celebrities or athletes that you like.
# Ask a user for their favorite celebrity or athelete.
# Check to see if that celebrity or athlete is also in your set.
# If so, print out a message saying you like that person, too.

mycelebs = {"Bob Odenkirk", "Mia Hamm", "Simone Biles", "Andre3000",
            "John Coltrane", "Rita Moreno", "Hugh Jackman",
            "Angela Lansbury", "Selena Gomez", "Betty White"}

yourceleb = input("Who is your favorite celebrity")
if yourceleb in mycelebs:
    print("Me too!")

# Create a tuple that contains your name, height in inches, and favorite color.
# Create two more tuples that contains this information for two of
# your friends. Put these tuples into a list.
# Loop through the list, then print out only the name
# and favorite color for each person.

me = ("Emily", "70", "blue")
rh = ("Robin", "66", "blue")
dg = ("Delphine", "67", "hazel")
mylist = [me, rh, dg]
for e in mylist:
    print(e[0], e[2])
    



## More Challenging

#Task: Create a dictionary that maps each word in a text to
# the number of vowels it has, e.g., elephant -> 3.

# Copy and paste a short news story into a text file on your desktop.
# (I made one, it's called royals.txt)
# Write a function that opens the file, reads it into a string, and
# splits that string into words. For each word, add it to a dictionary,
# making its value the number of vowels it has. Then return the dictionary.
# Write a main function that calls this function and the prints out the
# number of keys in the dictionary.

def vowelcounter():
    mydict = {}
    vowels = "AEIOUaeiou"
    f = open("royals.txt")
    words = f.read().split()
    for w in words:
        numvow = 0
        for c in w:
            if c in vowels:
                numvow += 1
        mydict[w] = numvow
    return mydict

def main():
    print(len(vowelcounter()))

main()


## Expert

# Task: Create a dictionary that maps a number to a set of words that
# have that number of letters, e.g.,

 #     3 -> {"dog", "cat", "pie"}
 #     5 -> {"trees", "couch", "piano"}

# Using the same file write a function that opens the file,
# reads it into a string, and splits that string into words.
# For each word, count its letters to get your dictionary key.
# Go retrieve that key's value (if it exists),
# and add this new word to the set that is its value.
# Write a main function that calls this function
# and the prints out each key-value pair on its own line.


def wordlength():
    mydict = {}
    f = open("royals.txt")
    words = f.read().split()
    for w in words:
        numlett = len(w)
        if numlett in mydict:
            mydict[numlett].add(w)
        else:
            mydict[numlett] = {w}
    return mydict

def main():
    vowelcountdict = vowelcounter()
    print(len(vowelcountdict))
    wordlengthdict = wordlength()
    for k,v in wordlengthdict.items():
        print(k,v)
    

main()



