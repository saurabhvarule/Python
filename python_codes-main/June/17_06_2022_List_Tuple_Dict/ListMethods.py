
company = list()

#1. append()

company.append("Meta")
company.append("Apple")
company.append("Amazon")
company.append("Netflix")
company.append("Google")
company.append("Microsoft")

print(company)

#2. copy()

lst2 = company.copy()
print(lst2)

#3. clear()

lst2.clear()
print(lst2)

#4. count(value)

print(company.count("Google"))

#5. extend(iterable)

company.extend({"Amdocs", "Xarient", "Pubmatic"})

#Only iterable type of objects can be extended.
#company.extend(10)                                     

print(company)

#6. index(value)

print(company.index("PTC"))
#print(company.index("Pubmatic", 2, 7))     #ValueError:

#7. insert(index, object)

company.insert(5, "Uber")
print(company)

#8. pop()

print(company.pop())
print(company)

#9. remove

company.remove("Amdocs")
print(company)

#10. reverse()

company.reverse()
print(company)

#11. sort()

company.sort()
print(company)
