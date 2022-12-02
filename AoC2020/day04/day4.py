with open('input.txt') as file:
    passport_data = file.read().splitlines()


def build_strings(passport_data: str) -> list:
    passports = []
    passport_string = ''
    for line in passport_data:
        if line == '':
            passports.append(passport_string.strip())
            passport_string = ''
        else:
            passport_string += ' ' + line
    if passport_string != '':
        passports.append(passport_string.strip())
    return passports


def build_passports(passport_strings: list) -> list:
    passport_list = []
    for passport_string in passport_strings:
        fields = passport_string.split(' ')
        passport = {}
        for field in fields:
            split_field = field.split(':')
            if len(split_field) < 2:
                print('ERROR', field)
            else:
                passport[split_field[0]] = split_field[1]
        passport_list.append(passport)
    return passport_list


passport_strings = build_strings(passport_data)
passports = build_passports(passport_strings)
result = 0
for passport in passports:
    if len(passport.keys()) == 8:
        result += 1
    if len(passport.keys()) == 7 and 'cid' not in passport.keys():
        result += 1

print(result)


