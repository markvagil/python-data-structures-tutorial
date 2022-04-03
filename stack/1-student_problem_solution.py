
# Concatenate all of the words together to make a sentence.

words = ["My", "most", "favorite", "programming", "language", "is", "python"]

# Type your code below
# Your result should be "My most favorite programming language is python."

# SOLUTION
sentence = "" # establish our sentence variable
last_word = words[len(words)-1] # find the last word

for word in words: # for each word in the words list
    if word == last_word: # if we are on the last word do this
        sentence += word + "."
    else: # for all other words do this
        sentence += word + " "

print(sentence) # print the completed sentence

"""
We completed this by using a simple for loop to add each word to our sentence variable with a space,
and then by checking to see if we had reached the last word, we added the last word with a period to 
complete the sentence and print it.
"""