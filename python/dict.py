
usernames = {
    "vinit": "vinixxx",
    "hulk":"yhull",
    "max":"max__",
    "joe":"joejoe"
}

print(usernames["vinit"])

#built in dictionary methods

print(usernames.keys())
print(usernames.values())
print(usernames.items())

# dict_keys(['vinit', 'hulk', 'max', 'joe'])
# dict_values(['vinixxx', 'yhull', 'max__', 'joejoe'])
# dict_items([('vinit', 'vinixxx'), ('hulk', 'yhull'), ('max', 'max__'), ('joe', 'joejoe')])

for key in usernames.keys():
    print(key + " - " + usernames[key])

# vinit - vinixxx
# hulk - yhull
# max - max__
# joe - joejoe

usernames["max"] = "max123"

usernames.update({"chloe":"chloe123"}) 

del usernames["max"]


# usernames.clear()
# usernames.popitem()