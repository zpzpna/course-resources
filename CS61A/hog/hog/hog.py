"""The Game of Hog."""

from dice import six_sided, make_test_dice
from ucb import main, trace, interact

GOAL = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    result, num_rowling, sowsad_flag= 0, 0, False
    
    while num_rowling<num_rolls:
        curr_dice = dice()
        result, num_rowling = result + curr_dice, num_rowling+1
        if curr_dice == 1:
            sowsad_flag = True 
    if sowsad_flag == True:
        result = 1
    return result
    
        
    
    # END PROBLEM 1


def boar_brawl(player_score, opponent_score):
    """Return the points scored by rolling 0 dice according to Boar Brawl.

    player_score:     The total score of the current player.
    opponent_score:   The total score of the other player.

    """
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def get_ones(num):
        return num%10
    def get_tens(num):
        return num//10%10
    result = abs(get_ones(player_score)-get_tens(opponent_score))*3
    if result == 0:
        result = 1
    return result
    # END PROBLEM 2


def take_turn(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the points scored on a turn rolling NUM_ROLLS dice when the
    player has PLAYER_SCORE points and the opponent has OPPONENT_SCORE points.

    num_rolls:       The number of dice rolls that will be made.
    player_score:    The total score of the current player.
    opponent_score:  The total score of the other player.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if  num_rolls == 0:
        return boar_brawl(player_score,opponent_score)
    else:
        return roll_dice(num_rolls, dice)
    
    # END PROBLEM 3


def simple_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, ignoring Fuzzy Factors.
    """
    score = player_score + take_turn(num_rolls, player_score, opponent_score, dice)
    return score


def hog_gcd(x, y):
    """Return the greatest common divisor between X and Y"""
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    factor_curr = min(x,y)
    if factor_curr == 0:
        return max(x,y)
    while x%factor_curr != 0 or y%factor_curr!=0:
        factor_curr=factor_curr-1
    return factor_curr
    # END PROBLEM 4


def fuzzy_points(score):
    """Return the new score of a player taking into account the Fuzzy Factors rule.
    """
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    gcd = hog_gcd(score,100)
    if gcd >10:
        return gcd//10%10*2+score
    else:
        return score
    # END PROBLEM 4


def fuzzy_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, *including* Fuzzy Factors.
    """
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    score = fuzzy_points(simple_update(num_rolls, player_score, opponent_score, dice))
    return score
    # END PROBLEM 4


def always_roll_5(score, opponent_score):
    """A strategy of always rolling 5 dice, regardless of the player's score or
    the oppononent's score.
    """
    return 5


def play(strategy0, strategy1, update,
         score0=0, score1=0, dice=six_sided, goal=GOAL):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first and Player 1's score second.

    E.g., play(always_roll_5, always_roll_5, fuzzy_update) simulates a game in
    which both players always choose to roll 5 dice on every turn and the Fuzzy
    Factors rule is in effect.

    A strategy function, such as always_roll_5, takes the current player's
    score and their opponent's score and returns the number of dice the current
    player chooses to roll.

    An update function, such as fuzzy_update or simple_update, takes the number
    of dice to roll, the current player's score, the opponent's score, and the
    dice function used to simulate rolling dice. It returns the updated score
    of the current player after they take their turn.

    strategy0: The strategy for player0.
    strategy1: The strategy for player1.
    update:    The update function (used for both players).
    score0:    Starting score for Player 0
    score1:    Starting score for Player 1
    dice:      A function of zero arguments that simulates a dice roll.
    goal:      The game ends and someone wins when this score is reached.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    def player_roll(player_score,opponent_score,strategy):
        num_rolls = strategy(player_score,opponent_score)
        player_score = update(num_rolls, player_score, opponent_score,dice)
        return player_score
        
        
    while score0 < goal and score1 < goal:
        if who:
            score1 = player_roll(score1,score0,strategy1)   #the abstraction: Don't change the formal parameters location used in the function body.
                                                            #Instead,just change the the arguments passed in the function header
        else:                                               #abstract names are prior to concrete names
            score0 = player_roll(score0,score1,strategy0)
        who = 1-who
            
    # END PROBLEM 5
    return score0, score1


#######################
# Phase 2: Strategies #
#######################


def always_roll(n):
    """Return a player strategy that always rolls N dice.

    A player strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(3)
    >>> strategy(0, 0)
    3
    >>> strategy(99, 99)
    3
    """
    assert n >= 0 and n <= 10
    # BEGIN PROBLEM 6
    "*** YOUR CODE HERE ***"
    def always_roll_fixed(player_score,opponent_score):
        return n    
    return always_roll_fixed
    # END PROBLEM 6


def catch_up(score, opponent_score):
    """A player strategy that always rolls 5 dice unless the opponent
    has a higher score, in which case 6 dice are rolled.

    >>> catch_up(9, 4)
    5
    >>> strategy(17, 18)
    6
    """
    if score < opponent_score:
        return 6  # Roll one more to catch up
    else:
        return 5


def is_always_roll(strategy, goal=GOAL):
    """Return whether STRATEGY always chooses the same number of dice to roll
    given a game that goes to GOAL points.

    >>> is_always_roll(always_roll_5)
    True
    >>> is_always_roll(always_roll(3))
    True
    >>> is_always_roll(catch_up)
    False
    """
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"
    def iter_dice(curr_dice,player_score,opponent_score):
        return curr_dice ,strategy(player_score,opponent_score)
        
    def iter_score(player_score,opponent_score):
        opponent_score = opponent_score+1
        if opponent_score == goal and player_score < goal:
            player_score ,opponent_score= player_score+1 ,0
        return player_score, opponent_score
        
    flag = True
    pred_dice, curr_dice= strategy(0,0), strategy(0,1)
    player_score,opponent_score = 0,0
    while opponent_score < goal and player_score < goal:
        if  pred_dice != curr_dice:
            flag = False
            return flag
        player_score, opponent_score = iter_score(player_score, opponent_score)
        pred_dice ,curr_dice = iter_dice(curr_dice,player_score,opponent_score)
    return flag
    # END PROBLEM 7


def make_averaged(original_function, total_samples=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    called TOTAL_SAMPLES times.

    To implement this function, you will have to use *args syntax.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 40)
    >>> averaged_dice(1, dice)  # The avg of 10 4's, 10 2's, 10 5's, and 10 1's
    3.0
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    def averaged_dice(*args):
        sample_num = 0
        dice_sum = 0
        while sample_num<total_samples:
            dice_sum ,sample_num = dice_sum+original_function(*args) ,sample_num+1
        return dice_sum/total_samples
    return averaged_dice
    # END PROBLEM 8


def max_scoring_num_rolls(dice=six_sided, total_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn score
    by calling roll_dice with the provided DICE a total of TOTAL_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    min_num,curr_num,max_avg = 1,1,0
    while curr_num <= 10:
        curr_avg = make_averaged(roll_dice,total_samples)(curr_num,dice)
        if max_avg < curr_avg:
            max_avg, min_num= curr_avg, curr_num
        curr_num = curr_num+1
    return min_num
        
    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1, fuzzy_update)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    six_sided_max = max_scoring_num_rolls(six_sided)
    print('Max scoring num rolls for six-sided dice:', six_sided_max)

    print('always_roll(6) win rate:', average_win_rate(always_roll(6)))  # near 0.5
    print('catch_up win rate:', average_win_rate(catch_up))
    print('always_roll(3) win rate:', average_win_rate(always_roll(3)))
    print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    print('boar_strategy win rate:', average_win_rate(boar_strategy))
    print('fuzzy_strategy win rate:', average_win_rate(fuzzy_strategy))
    print('final_strategy win rate:', average_win_rate(final_strategy))
    "*** You may add additional experiments as you wish ***"


def boar_strategy(score, opponent_score, threshold=12, num_rolls=6):
    """This strategy returns 0 dice if Boar Brawl gives at least THRESHOLD
    points, and returns NUM_ROLLS otherwise. Ignore score and Fuzzy Factors.
    """
    # BEGIN PROBLEM 10
    boar_result = boar_brawl(score,opponent_score)
    if boar_result >= threshold:
        num_rolls = 0
    return num_rolls  # Remove this line once implemented.
    # END PROBLEM 10


def fuzzy_strategy(score, opponent_score, threshold=12, num_rolls=6):
    """This strategy returns 0 dice when your score would increase by at least threshold."""
    # BEGIN PROBLEM 11
    if fuzzy_update(0,score,opponent_score)-score >= threshold:
        num_rolls = 0
    return num_rolls  # Remove this line once implemented.
    # END PROBLEM 11


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.
    
    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 12
    num_rolls = 6
    
    gap = GOAL-score
    
    fuzzy_num = fuzzy_update(0,score,opponent_score)-score
    if  fuzzy_num >= gap or fuzzy_num >= make_averaged(roll_dice,10)(6):
        num_rolls = 0
    return num_rolls  # Remove this line once implemented.
    # END PROBLEM 12


##########################
# Command Line Interface #
##########################

# NOTE: The function in this section does not need to be changed. It uses
# features of Python not yet covered in the course.

@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
