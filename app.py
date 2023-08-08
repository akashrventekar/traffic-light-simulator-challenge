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

    # Not convoluting this logic with checking if one light is on at a single time. The user doesn't have a way to input
    # get_traffic_light
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


# Verified that printing can be sequential without clearing should be fine
def print_traffic_lights(red_duration: str, yellow_duration: str, green_duration: str):
    print(get_traffic_light(red=True, yellow=False, green=False))
    time.sleep(red_duration)

    print(get_traffic_light(red=False, yellow=True, green=False))
    time.sleep(yellow_duration)

    print(get_traffic_light(red=False, yellow=False, green=True))
    time.sleep(green_duration)


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
        f'Enter the duration (in seconds) for {color} light color to stay lit before transitioning or type exit to exit the program: ')
    while not valid_input(user_input):
        print(f'{color} duration: {user_input} is invalid')
        user_input = input(
            f'Enter the duration (in seconds) for {color} light color to stay lit before transitioning or type exit to exit the program: ')
    return int(user_input)


'''Several ways to implement: 
* Using Threads to run the program 
* I could write two different programs 
- One to take input and save it as a file (config for the second program) [This can use input or use sysargs/argparse]. 
Can't have two programs write at the same time, that will lead to corruption (need to lock it) 
- The second program reads from the file and executes the traffic lights accordingly 
* Easier for this program to just get the inputs sequentially and print out results sequentially 
including multiple runs and inputs <-- Using this approach
* We can also do a single run of this program and stop
* Could have created a class'''
if __name__ == "__main__":
    try:
        # Assumption take inputs each round
        while True:
            user_input_red_duration = get_valid_input(color="red")
            user_input_yellow_duration = get_valid_input(color="yellow")
            user_input_green_duration = get_valid_input(color="green")

            print_traffic_lights(red_duration=user_input_red_duration, yellow_duration=user_input_yellow_duration,
                                 green_duration=user_input_green_duration)
            print('Finished a round of traffic simulation')
    except KeyboardInterrupt:
        print("Stopped Traffic Light Simulator due to interruption.")
