file = open("day1/input.txt", "r")
lines=file.read().splitlines()

answer=0
for line in lines:
    numbers=[]
    for letter in line:
        if letter.isdigit():
            numbers.append(letter)
    answer+=int(numbers[0]+numbers[-1])
print(answer)

