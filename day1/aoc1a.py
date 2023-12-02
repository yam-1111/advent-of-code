# Day 1: Trebuchet?!

def get_num(string):
    arr2 = [i for i in string if i.isdigit()]
    return (int(arr2[0] + arr2[-1]))
with open("case1a.txt", 'r') as file:
    file_content = file.read()
    print(int(sum([get_num(x) for x in file_content.split('\n')])))

