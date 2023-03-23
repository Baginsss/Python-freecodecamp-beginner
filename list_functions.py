friends = ["Michał", "Oskar", "Dawid", "Rogal", "Szymon"]
housemates = ["Marta", "Graziana", "Marco", "Jun", "Hiroki", "Chiharu"]
lucky_number = [4, 8, 15, 23, 42]

friends.extend(lucky_number)

print(friends)

friends = ["Michał", "Oskar", "Dawid", "Rogal", "Szymon"]
housemates = ["Marta", "Graziana", "Marco", "Jun", "Hiroki", "Chiharu"]
lucky_number = [4, 8, 15, 23, 42]

friends.append("Asia")
print(friends)

friends = ["Michał", "Oskar", "Dawid", "Rogal", "Szymon"]
housemates = ["Marta", "Graziana", "Marco", "Jun", "Hiroki", "Chiharu"]
lucky_number = [4, 8, 15, 23, 42]

friends.insert(1, "Asia")
print(friends)

friends.remove("Asia")
print(friends)

friends.clear()
print(friends)

friends = ["Michał", "Oskar", "Dawid", "Rogal", "Szymon"]
friends.pop()
print(friends)

friends = ["Michał", "Oskar", "Dawid", "Rogal", "Szymon"]
print(friends.index("Oskar"))

