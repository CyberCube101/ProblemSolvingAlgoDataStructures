'''The theorem states that a monkey hitting keys at random on a typewriter
keyboard for an infinite amount of time will almost surely type a given text, such as the complete works of William Shakespeare. .'''

goal = 'methinks it is like a weasel'

import random
import string


def generatOne(strlen):
    alpha = 'abcdefghijklmnopqrstuvwxyz '
    res = ""
    for i in range(strlen):
        res = res + random.choice(alpha)

    return res


print(generatOne(28))


#####################################################

def score(goal, teststring):
    numSame = 0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            numSame += 1
    return numSame / len(goal)


if __name__ == '__main__':
    print(score(goal, generatOne(28)))
