#!/usr/bin/env python3
#
# Task:
# Passports data fields are as follows:
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
# Count the number of valid passports - those that have all required fields
# and valid values. Continue to treat cid as optional. In your batch file,
# how many passports are valid?
#
# Solution:
# In this part we additionally check the values of defined fields.
# The taken approach works, but is ugly, though...
#

INPUT_FILE = 'input.txt'


def main():
    passports = ''.join(open(INPUT_FILE, 'r').readlines()).split('\n\n')

    valid_passports = 0
    required_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

    for passport in passports:
        fields = passport.split()

        available_fields = set([field.split(':')[0] for field in fields])

        fields_are_valid = True

        for field in fields:
            key = field.split(':')[0]
            value = field.split(':')[1]

            if key == 'byr':
                if len(value) != 4:
                    fields_are_valid = False
                    break
                if not all('0' <= letter <= '9' for letter in value):
                    fields_are_valid = False
                    break
                value = int(value)
                if value < 1920 or value > 2002:
                    fields_are_valid = False
                    break

            elif key == 'iyr':
                if len(value) != 4:
                    fields_are_valid = False
                    break
                if not all('0' <= letter <= '9' for letter in value):
                    fields_are_valid = False
                    break
                value = int(value)
                if value < 2010 or value > 2020:
                    fields_are_valid = False
                    break

            elif key == 'eyr':
                if len(value) != 4:
                    fields_are_valid = False
                    break
                if not all('0' <= letter <= '9' for letter in value):
                    fields_are_valid = False
                    break
                value = int(value)
                if value < 2020 or value > 2030:
                    fields_are_valid = False
                    break

            elif key == 'hgt':
                if value[-2:] == 'cm':
                    value = int(value[:-2])
                    if value < 150 or value > 193:
                        fields_are_valid = False
                        break
                elif value[-2:] == 'in':
                    value = int(value[:-2])
                    if value < 59 or value > 76:
                        fields_are_valid = False
                        break
                else:
                    fields_are_valid = False
                    break

            elif key == 'hcl':
                if len(value) != 7:
                    fields_are_valid = False
                    break
                if value[0] != '#':
                    fields_are_valid = False
                    break
                if not all('0' <= letter <= '9' or 'a' <= letter <= 'f'
                           for letter in value[1:]):
                    fields_are_valid = False
                    break

            elif key == 'ecl':
                if value not in ['amb', 'blu', 'brn',
                                 'gry', 'grn', 'hzl', 'oth']:
                    fields_are_valid = False
                    break

            elif key == 'pid':
                if len(value) != 9:
                    fields_are_valid = False
                    break
                if not all('0' <= letter <= '9' for letter in value):
                    fields_are_valid = False
                    break

        if not (required_fields - available_fields) and fields_are_valid:
            valid_passports += 1

    print(valid_passports)


if __name__ == '__main__':
    main()
