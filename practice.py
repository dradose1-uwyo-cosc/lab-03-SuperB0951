names = ["Champ", "Brayden", "Koen", "Houston", "Lily", "Brandon"]
print(names)

# del names [5]
names.remove("Brandon")
print(names)


for name in names:
    print(f"{name} is on my table")
    
names.sort(reverse=True)
print(names)