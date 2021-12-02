import os


def task_1(password_data):
    n_valid_passwords = 0
    for password_line in password_data:
        letter_range, letter, password = password_line.split(' ')
        lower_range = int(letter_range.split('-')[0])
        upper_range = int(letter_range.split('-')[1])
        password.replace('\n', '')
        letter = letter[0]
        if lower_range <= password.count(letter) <= upper_range:
            n_valid_passwords += 1
    return n_valid_passwords


def task_2(password_data):
    n_valid_passwords = 0
    for password_line in password_data:
        indexes, letter, password = password_line.split(' ')
        first_index = int(indexes.split('-')[0])
        second_index = int(indexes.split('-')[1])
        letter = letter[0]
        password.replace('\n', '')
        letter_1 = password[first_index-1]
        letter_2 = password[second_index-1]
        if letter_1 == letter or letter_2 == letter:
            if not (letter_1 == letter and letter_2 == letter):
                n_valid_passwords += 1
    return n_valid_passwords


def main():
    password_data = []
    for line in open(os.getcwd() + '/data/day_2.txt'):
        password_data.append(line)
    print(task_1(password_data))
    print(task_2(password_data))


if __name__ == '__main__':
    main()
