old_password = 'hepxcrrq'


def next_letter(letter: chr) -> chr:
    if letter == 'z':
        return 'a'
    else:
        new_letter = chr(ord(letter) + 1)
        if new_letter == 'i' or new_letter == 'o' or new_letter == 'l':
            return next_letter(new_letter)
        else:
            return new_letter


def is_password_good(password: list) -> bool:
    found_double = False
    double_chars = []
    for i in range(0, len(password) - 1):
        if password[i] == password[i + 1] and password[i] not in double_chars:
            double_chars.append(password[i])
            i = i + 1
    if len(double_chars) <= 1:
        return False
    found_sequence = False
    for i in range(0, len(password) - 2):
        if ord(password[i]) + 1 == ord(password[i + 1]) and ord(password[i]) + 2 == ord(password[i + 2]):
            found_sequence = True
            break
    if not found_sequence:
        return False
    return True


def get_next_password(password: list) -> list:
    position = len(password) - 1
    next_char = next_letter(password[position])
    if next_char != 'a':
        password[position] = next_char
        return password
    else:
        shorter_pw = password[:-1]
        shorter_password = get_next_password(shorter_pw)
        shorter_password.append('a')
        return shorter_password


password = list(old_password)
while not is_password_good(password):
    password = get_next_password(password)
    print(password)

print(''.join(password))

