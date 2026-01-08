"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


# CONSTANTS
EXPECTED_BAKE_TIME = 40
TIME_PER_LAYER = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the total preperation time
    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - TIME_PER_LAYER multiplied to the number_of_layers

    Assumes that each layer of lasagna takes 2 minutes to prepare,
    thus each number of layer is multiplied by 2.
    """
    return TIME_PER_LAYER * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Returns the time spent preparing and baking.
    :param number_of_layers: int - the number of layers in the lasagna
    :param elapsed_bake_time: int - the current time the lasagna is baking
    :return: int - preperation time of the lasagna + the elapsed bake time

    Calls the prepration_time_in_minutes function and inputs the number_of_layers.
    Then adds the current bake time of the lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
