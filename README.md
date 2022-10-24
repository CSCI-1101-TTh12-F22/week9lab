# Week 9 Section Activities

This week I'd like you to do a few review exercises on data structures (list, tuple, set, dictionary) and functions as a self-evaluation exercise. 

## Data Structures

### Basic
1. Create a dictionary that map months to the number of days they have. Then print out each key-value pair on its own line.

2. Create a set of 10 celebrities or athletes that you like. Ask a user for their favorite celebrity or athelete. Check to see if that celebrity or athlete is also in your set. If so, print out a message saying you like that person, too.

3. Create a tuple that contains your name, height in inches, and favorite color. Create two more tuples that contains this information for two of your friends. Put these tuples into a list. Loop through the list, then print out only the name and favorite color for each person.

### More Challenging

Task: Create a dictionary that maps each word in a text to the number of vowels it has, e.g., `elephant -> 3`.

* Copy and paste a short news story into a text file on your desktop.
* Write a function that opens the file, reads it into a string, and splits that string into words. For each word, add it to a dictionary, making its value the number of vowels it has. Then return the dictionary.
* Write a main function that calls this function and the prints out the number of keys in the dictionary.

### Expert

Task: Create a dictionary that maps a number to a set of words that have that number of letters, e.g.,
```
      3 -> {"dog", "cat", "pie"}
      5 -> {"trees", "couch", "piano"}
```

* Using the same file write a function that opens the file, reads it into a string, and splits that string into words. For each word, count its letters to get your dictionary key. Go retrieve that key's value (if it exists), and add this new word to the set that is its value.
* Write a main function that calls this function and the prints out each key-value pair on its own line.

## Functions

1. Write a function that takes two integer arguments and returns True if the first is larger than the second, and False otherwise. Then, write a main method that calls this function, and based on what the function returns, prints out which of the two ints is larger.

2. Write a function that takes two integers arguments and returns their product and their sum. Write another function that takes two integer arguments and calls the first function and returns True if the product is larger than the sum, False otherwise. Write a main function that calls the second function and prints out a message like "the sum of x and y is greater/less than the product of x and y"
