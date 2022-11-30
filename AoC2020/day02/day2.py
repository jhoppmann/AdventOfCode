with open('input.txt') as file:
    input_content = file.read().splitlines()

values = [x.split(' ', 1) for x in input_content]

correct_passwords = 0

for password_info in values:
    occurences = password_info[0].split('-')
    character = password_info[1].split(':')[0]
    password = password_info[1].split(':')[1]

    num = password.count(character)
    if int(occurences[1]) >= num >= int(occurences[0]):
        correct_passwords += 1

print(correct_passwords)
