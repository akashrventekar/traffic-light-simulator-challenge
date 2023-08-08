import traceback
import logging

logger = logging.getLogger(__name__)
logging.disable(logging.CRITICAL) # You can either enable or disable this

def valid_duration(input_duration) -> bool:
    try:
        duration = int(input_duration)
    except TypeError as e:
        logger.exception(e)
        return False
    except ValueError as e:
        logger.exception(e)
        return False

    return True



if __name__ == "__main__":
    while True:
        user_input = input("Enter the duration (in seconds) for each light color to stay lit before transitioning: ")
        if not valid_duration(user_input):
            print(f'{user_input} is invalid')
            continue    # Quick & Dirty for now



