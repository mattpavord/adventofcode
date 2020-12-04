from typing import List, Dict
import re


def load_data() -> List[Dict]:
    passports = []
    passport = {}
    for line in open('data/day_4.txt'):
        line = line.replace('\n', '')
        if not line:  # end of passport
            passports.append(passport)
            passport = {}
        else:
            attributes = line.split(' ')
            for attribute in attributes:
                key, value = attribute.split(':')
                passport[key] = value
    passports.append(passport)
    return passports


def check_byr(value: str):
    return 1920 <= int(value) <= 2002


def check_iyr(value: str):
    return 2010 <= int(value) <= 2020


def check_eyr(value: str):
    return 2020 <= int(value) <= 2030


def check_hgt(value: str):
    if value.endswith('in'):
        return 59 <= int(value[:-2]) <= 76
    if value.endswith('cm'):
        return 150 <= int(value[:-2]) <= 193


def check_hcl(value: str):
    if len(value) != 7 or value[0] != '#':
        return False
    if re.match('^[\w\d]*$', value[1:]):
        return True
    return False


def check_ecl(value: str):
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def check_pid(value: str):
    return value.isdigit() and len(value) == 9


def task_1(passports: List[Dict]):
    valid_passports = 0
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for passport in passports:
        for field in required_fields:
            if field not in passport:
                break
        else:
            valid_passports += 1
    return valid_passports


def task_2(passports: List[Dict]):
    valid_passports = 0
    check_map = {
        'byr': check_byr,
        'iyr': check_iyr,
        'eyr': check_eyr,
        'hgt': check_hgt,
        'hcl': check_hcl,
        'ecl': check_ecl,
        'pid': check_pid,
    }
    for passport in passports:
        for field in check_map:
            if field not in passport:
                break
            elif not check_map[field](passport[field]):
                break
        else:
            valid_passports += 1
    return valid_passports


def main():
    passports = load_data()
    print(task_1(passports))
    print(task_2(passports))


if __name__ == '__main__':
    main()
