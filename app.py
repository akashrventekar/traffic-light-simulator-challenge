import time
import logging

logger = logging.getLogger(__name__)
logging.disable(logging.CRITICAL)  # You can either enable or disable this


def get_traffic_light(red: bool = False, yellow: bool = False, green: bool = False) -> str:
    light_on = "|  /####\  |\n" \
               "|  \####/  |"
    light_off = "|    /\    |\n" \
                "|    \/    |"

    red_light = light_off
    yellow_light = light_off
    green_light = light_off

    if red:
        red_light = f'\033[31m{light_on}\033[0m'

    if yellow:
        yellow_light = f'\033[33m{light_on}\033[0m'

    if green:
        green_light = f'\033[32m{light_on}\033[0m'

    return f"""
     ##
    _[]_
  [______]
.----''----.
|   .==.   |
{red_light}
|   .==.   |
|   .==.   |
{yellow_light}
|   .==.   |
|   .==.   |
{green_light}
|   .==.   |
'-.______.-'
    """


def print_traffic_lights(red_duration: str, yellow_duration: str, green_duration: str):
    time.sleep(red_duration)
    print(get_traffic_light(red=True, yellow=False, green=False))
    time.sleep(yellow_duration)
    print(get_traffic_light(red=False, yellow=True, green=False))
    time.sleep(green_duration)
    print(get_traffic_light(red=False, yellow=False, green=True))


def valid_input(user_input: str) -> bool:
    if user_input == 'exit':
        print("Exiting Traffic Light Simulator")
        exit(0)
    try:
        int(user_input)
    except TypeError as e:
        logger.exception(e)
        return False
    except ValueError as e:
        logger.exception(e)
        return False
    return True


def get_valid_input(color: str) -> int:
    user_input = input(
        f'Enter the duration (in seconds) for {color} light color to stay lit before transitioning or enter exit to exit the program: ')
    while not valid_input(user_input):
        print(f'{color} duration: {user_input} is invalid')
        user_input = input(
            f'Enter the duration (in seconds) for {color} light color to stay lit before transitioning or enter exit to exit the program: ')
    return int(user_input)


if __name__ == "__main__":
    '''
    Several ways to do it:
    * Using Threads to run the program
    * I could write two different programs
     - One to take input and save it as a file (config for the second program) [This can use input or use sysargs/argparse]. Can't have two programs write at the same time, that will lead to corruption (need to lock it)
     - The second program reads from the file and executes the traffic lights accordingly 
    * Easier for this program to just get the inputs sequentially and print out results sequentially (Using this approach)
    * You can always create a class, but refraining from doing that
   '''
    while True:
        user_input_red_duration = get_valid_input(color="red")
        user_input_yellow_duration = get_valid_input(color="yellow")
        user_input_green_duration = get_valid_input(color="green")
        print_traffic_lights(red_duration=user_input_red_duration, yellow_duration=user_input_yellow_duration,
                             green_duration=user_input_green_duration)
