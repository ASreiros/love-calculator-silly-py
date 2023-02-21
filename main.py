#You are going to write a program that tests the compatibility between two people.
#To work out the love score between two people:
#Take both people's names and check for the number of times the letters in the word TRUE occurs.
#Then check for the number of times the letters in the word LOVE occurs.
#Then combine these numbers to make a 2 digit number.


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

test_word_1 = "true"
test_word_2 = "love"
name1 = name1.lower()
name2 = name2.lower()
points_t = 0
points_l = 0
i = 0
y = 0
while i < len(test_word_1):
    points_t += name1.count(test_word_1[i])
    points_t += name2.count(test_word_1[i])
    i += 1

while y < len(test_word_2):
    points_l += name1.count(test_word_2[y])
    points_l += name2.count(test_word_2[y])
    y += 1

points_total = int(str(points_t) + str(points_l))

if points_total > 90 or points_total < 10:
    print(f'Your score is {points_total}, you go together like coke and mentos.')
elif 50 > points_total > 40:
    print(f'Your score is {points_total}, you are alright together.')
else:
    print(f'Your score is {points_total}.')




