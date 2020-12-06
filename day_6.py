from typing import List


def load_data() -> List[List[str]]:
    all_group_questions = []
    group_questions = []
    for line in open('data/day_6.txt'):
        line = line.replace('\n', '')
        if not line:  # end of passport
            all_group_questions.append(group_questions)
            group_questions = []
        else:
            group_questions.append(line)
    all_group_questions.append(group_questions)
    return all_group_questions


def task_1(all_group_questions: List[List[str]]) -> int:
    count = 0
    for group_questions in all_group_questions:
        unique_questions = set()
        for questions in group_questions:
            for question in questions:
                unique_questions.add(question)
        count += len(unique_questions)
    return count


def task_2(all_group_questions: List[List[str]]) -> int:
    count = 0
    for group_questions in all_group_questions:
        questions_all_answered = [q for q in group_questions[0]]
        for questions in group_questions:
            for q in questions_all_answered.copy():
                if q not in questions:
                    questions_all_answered.remove(q)
        count += len(questions_all_answered)
    return count


def main():
    all_group_questions = load_data()
    print(task_1(all_group_questions))
    print(task_2(all_group_questions))


if __name__ == '__main__':
    main()
