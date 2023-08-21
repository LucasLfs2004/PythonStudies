# TODO: define the 'EXPECTED_BAKE_TIME' constant.


EXPECTED_BAKE_TIME = int(40)

# TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.


def bake_time_remaining(time):

    return EXPECTED_BAKE_TIME - time

# TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.


def preparation_time_in_minutes(camadas):
    return 2 * camadas


# TODO: define the 'elapsed_time_in_minutes()' function below.

def elapsed_time_in_minutes(num_layers, elapsed_bake_time):
    return preparation_time_in_minutes(num_layers) + bake_time_remaining(elapsed_bake_time)

    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """


result = elapsed_time_in_minutes(1, 3)
print(result)
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)
