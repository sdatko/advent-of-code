#!/usr/bin/env python3
#
# Task:
# Passports data fields are as follows:
# - byr (Birth Year)
# - iyr (Issue Year)
# - eyr (Expiration Year)
# - hgt (Height)
# - hcl (Hair Color)
# - ecl (Eye Color)
# - pid (Passport ID)
# - cid (Country ID)
# Count the number of valid passports - those that have all required fields.
# Treat cid as optional. In your batch file, how many passports are valid?
#
# Solution:
# We join the whole input file as one long string and then split by double
# newlines to have list of passports. The list of passports can be split
# by any white space to fields. From the available fields we built the set
# and we check if there is no missing field from required on by calculating
# the sets difference.
#

INPUT_FILE = 'input.txt'


def main():
    passports = ''.join(open(INPUT_FILE, 'r').readlines()).split('\n\n')

    valid_passports = 0
    required_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

    for passport in passports:
        fields = passport.split()

        available_fields = set([field.split(':')[0] for field in fields])

        if not (required_fields - available_fields):
            valid_passports += 1

    print(valid_passports)


if __name__ == '__main__':
    main()
