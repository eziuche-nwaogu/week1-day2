# Print out a string
print("Mary had a little lamb.")
# print out a string and replace the curly braces with parameter in format
print("Its fleece was white as {}.".format("snow"))
# Print out a string
print("And everywhere that Mary went.")
# multiply a single character by 10 and print it out 10 times
print("." * 10)  # what'd that do? It prints the single character 10 times
# declaring a string variable with 12 curly braces
formatter = "{} {} {} {} {} {} {} {} {} {} {} {}"
# print the variable using the format for strings
print(formatter.format(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
# Another example below
print(
    formatter.format(
        "I",
        "am",
        "not",
        "here",
        "to",
        "make",
        "any",
        "jokes",
        "but",
        "some",
        "people",
        "are",
    )
)
# Another example which takes in series of strings
print(
    formatter.format(
        "We will now see how",
        "to do a more complicated",
        "formatting of a string.",
        "This code",
        "looks complex,",
        "but if you do",
        "your comments",
        "above each",
        "line and break",
        "each thing",
        "down to its parts,",
        "you will understand it.",
    )
)
