NUMBER_MAP = {
'zero': 0,
'one': 1,
'two': 2, 
'three': 3, 
'four': 4, 
'five': 5, 
'six': 6,
'seven': 7, 
'eight': 8, 
'nine': 9
}

# converts the given string int number and word to int 
def find_digit(string :str):
    return [x  for x in string if x.isdigit()]

def find_wdigit(string :str):
    nums = []
    # searches the given string from dict
    for x in NUMBER_MAP.keys():
        if string.find(x) != -1:
            nums.append(NUMBER_MAP.get(x))
    return nums

# function checkers for start and end, returns if finds an integer.
def check_end(string :str):
    words = []
  # checks on the end of the int, returns if string has match
    for j in reversed(string):
        words.append(j)
        # flipping the string array to get the word or number
        word = "".join(words[::-1])
        if find_digit(word):
            return int("".join(find_digit(word)))
        elif find_wdigit(word):
            return int(find_wdigit(word)[0])

def check_start(string :str):
    words = []
    # checks on the start of the int, returns if string has match
    for j in string:
        words.append(j)
        word = "".join(words)
        if find_digit(word):
            return int("".join(find_digit(word)))
        elif find_wdigit(word):
            return int(find_wdigit(word)[0]) 

# brute forcing by checking the numbers start and end
sum = 0
with open("case2.txt", "r") as f:
    file_content = f.read()
    for x in file_content.split('\n'):
        words = []
        sum += int(f"{check_start(x)}{check_end(x)}")

print(sum)

            
                
                
