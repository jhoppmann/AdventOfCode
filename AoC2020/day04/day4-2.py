import re
from pprint import pprint

with open('input.txt') as file:
    passport_data = file.read().splitlines()


def build_strings(passport_data: list) -> list:
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
            passport[split_field[0]] = split_field[1]
        passport_list.append(passport)
    return passport_list


def is_valid(passport: dict) -> bool:
    if len(passport['byr']) != 4 or int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
        return False
    if len(passport['iyr']) != 4 or int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
        return False
    if len(passport['eyr']) != 4 or int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
        return False
    height = passport['hgt']
    if not height.endswith('in') and not height.endswith('cm'):
        return False
    height_value = int(re.findall('\\d+', height)[0])
    if height.endswith('cm') and (height_value < 150 or height_value > 193):
        return False
    if height.endswith('in') and (height_value < 59 or height_value > 76):
        return False
    if not re.match('#[a-f0-9]{6}', passport['hcl']):
        return False
    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if not re.fullmatch('\\d{9}', passport['pid']):
        return False
    return True


passport_strings = build_strings(passport_data)
passports = build_passports(passport_strings)
required_fields_present = []

for passport in passports:
    if len(passport.keys()) == 8:
        required_fields_present.append(passport)
    if len(passport.keys()) == 7 and 'cid' not in passport.keys():
        required_fields_present.append(passport)

result = sum(is_valid(p) for p in required_fields_present)
for pdict in [p for p in required_fields_present if is_valid(p)]:
    print(pdict['pid'])

print(result)
