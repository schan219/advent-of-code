"""Module rock paper scissors printing your score."""

ROCK = 1
PAPER = 2
SCISSORS = 3

LOSE = 0
DRAW = 3
WIN = 6

point_allocation = {
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

revised_point_allocation = {
    "A X": SCISSORS+LOSE,
    "A Y": ROCK+DRAW,
    "A Z": PAPER+WIN,
    "B X": ROCK+LOSE,
    "B Y": PAPER+DRAW,
    "B Z": SCISSORS+WIN,
    "C X": PAPER+LOSE,
    "C Y": SCISSORS+DRAW,
    "C Z": ROCK+WIN,
}

def rock_paper_scissors(strategy_list, points):
    """
        Finds the sum of the score from a list of rock paper scissors outcomes.

        Parameters
        ----------
            outcomes_list : list[str]
                list of outcomes

            points: dict[str, int]
                dictionary of point allocation
    """

    score = 0

    for outcome in strategy_list:
        score += points[outcome]

    return score

if __name__ == '__main__':
    TEST = 'example.txt'
    REAL = 'input.txt'

    with open(REAL, encoding='UTF-8') as file:
        lines = [line.rstrip() for line in file]

        RESULT = rock_paper_scissors(lines, point_allocation)
        print(RESULT)

        RESULT = rock_paper_scissors(lines, revised_point_allocation)
        print(RESULT)
