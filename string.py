# convert string in upper case
name = "my name is sumit kalbhor."
print(name.upper())

# convert string to lower case
age = "MY AGE IS 24 YEARS."
print(age.lower())

# string methods
print("SUMIT".isupper())
print("sumit".islower())
print("123".isdecimal())
print("    ".isspace())
print("sumit".startswith("s"))
print("sumit".startswith("u"))
print("sumit".endswith("t"))
print("sumit".endswith("S"))
print(", ".join(["1", "2", "3", "4"]))
print("one,two,three,four".split(","))
print("Hello World".ljust(15) + "!")
print("Hello World".rjust(15))
print("Hello World".center(15))
print("1,2,3,4,2".rstrip(",2"))
print("2,1,2,3,4,2".lstrip(",2"))
print("sumitkalbhor".strip("s"))
print("good morning".replace("morning", "afternoon"))
print("Hello World".replace("l", "w"))
print(len("Hello World"))


