#try to use list comprehension to create a new problem(ex. set
#1


squares = [x**2 for x in range(11)]
print(squares)
#2


evens = [x for x in range(21) if x % 2 == 0]
print(evens)
#3


words = ["apple", "banana", "cherry", "date"]
word_lengths = [len(word) for word in words]
print(word_lengths)
#4


words = ["apple", "banana", "cherry", "date", "kiwi"]
min_length = int(input("Enter minimum word length: "))

long_words = [word for word in words if len(word) > min_length]
print(long_words)
#Create a code using list compression. 
