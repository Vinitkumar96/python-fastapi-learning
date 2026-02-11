countries = ["usa","canada","india"]

print(countries[0])
print(countries[-1])

print(len(countries))

countries.append("spain")
countries.insert(1,"italy")

print(countries) 

countries[0],countries[1] = countries[1],countries[0] #swap without temp

countries.sort()
print(countries)


lol=[23,12,41,4]
lol.sort()
lol.reverse()
print(lol)
