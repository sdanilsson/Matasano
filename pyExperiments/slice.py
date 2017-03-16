# word1 = raw_input("Word 1: ")
# word2 = raw_input("Word 2: ")
# slice1 = word1[len(word1)/2:]
# slice2 = word2[len(word2)/2:]
# print slice1,slice2

# word = 'Python'
# first = word[0:1]
# rest = word[1:]
# result = rest + '-' + first + 'y'
#print result

computer_choice = 'rock'
user_choice = raw_input("Enter rock, paper, or python:\n")

if computer_choice == user_choice:
    print('TIE')
elif user_choice == 'rock' and computer_choice == 'python':
    print('WIN')
else:
    print('You lose :( Computer wins :D')