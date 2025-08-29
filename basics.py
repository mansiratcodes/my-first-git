my_dict = {
    "name":"hannah",
    "age":19,
    "city":"amritsar"
}
print(my_dict["name"])
print(my_dict["age"])

dictionary = {
    "python":"a popular language",
    "variable":" a name that stores data",
    "loop": "a way to repeat code"
}
word = input("enter a word:").lower()
if word in dictionary:
    print(f"{word.capitalize()}: {dictionary[word]}")
else:
    print("sorry,that word is not in the dictionary.")