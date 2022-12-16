"""Module rock paper scissors printing your score."""

ROCK = 1
PAPER = 2
SCISSORS = 3

LOSE = 0
DRAW = 3
WIN = 6

pointAllocation = {
    "A X": ROCK+DRAW,
    "A Y": PAPER+WIN,
    "A Z": SCISSORS+LOSE,
    "B X": ROCK+LOSE,
    "B Y": PAPER+DRAW,
    "B Z": SCISSORS+WIN,
    "C X": ROCK+WIN,
    "C Y": PAPER+LOSE,
    "C Z": SCISSORS+DRAW,
}

def rock_paper_scissors(strategy_list):
    """
        Finds the sum of the score from a list of rock paper scissors outcomes.

        Parameters
        ----------
            outcomes_list : list[str]
                list of outcomes
    """

    score = 0

    for outcome in strategy_list:
        score += pointAllocation[outcome]

    return score

if __name__ == '__main__':
    TEST = 'example.txt'
    REAL = 'input.txt'

    with open(REAL, encoding='UTF-8') as file:
        lines = [line.rstrip() for line in file]

        RESULT = rock_paper_scissors(lines)
        print(RESULT)
