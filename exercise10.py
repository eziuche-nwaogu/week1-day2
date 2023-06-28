tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
# more printing with escape sequence
exp1 = """We will now see how to \\ do a more complicated\\ formatting of a string.
This code looks complex,
but if you do your comments above each line
and break each thing down to its parts,
you will understand it."""
# more on printing while using escape sequence
exp2 = "We will now see\n\thow to do\n\ta more complicated\n formatting of a string."
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(exp1)
print(exp2)
print("I am identing the first variable {}".format(tabby_cat))
print("I am adding the second variable {}".format(persian_cat))
print("I am adding the third variable {}".format(fat_cat))
print("I am also adding the fourth variable: {}".format(exp1))
print("And also the fifth variable: {}".format(exp2))
print(f"And another one using the f-formatter: {exp1}")
