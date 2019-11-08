#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    answers = []
    if n == 0:
        return [[]]
    for i in range(n):
        answers = merge_answers(answers, [['rock'], ['paper'], ["scissors"]])
    return answers

def merge_answers (answers, answers2):
    return_ansers = []
    if len(answers) == 0:
        return answers2
    for i in range(len(answers)):
        for j in range(len(answers2)):
            return_ansers.append(answers[i] + answers2[j])

    return return_ansers






if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
