
import time
import threading
from app import get_valid_input, print_traffic_lights

class TrafficLightSimulator:
    def __init__(self):
        self.green_duration = 0
        self.yellow_duration = 0
        self.red_duration = 0
        self.running = False

    def set_light_durations(self):
        self.red_duration = get_valid_input(color="red")
        self.yellow_duration = get_valid_input(color="yellow")
        self.green_duration = get_valid_input(color="green")

    def traffic_light(self):
        while self.running:
            print_traffic_lights(red_duration=self.red_duration, yellow_duration=self.yellow_duration,
                                 green_duration=self.green_duration)

    def start(self):
        self.set_light_durations()
        self.running = True
        self.thread = threading.Thread(target=self.traffic_light)
        self.thread.start()

    def stop(self):
        self.running = False
        self.thread.join()

if __name__ == "__main__":
    print("Welcome to the Traffic Light Simulator!")
    simulator = TrafficLightSimulator()

    try:
        simulator.start()
        input_command = input("Enter anything to stop the simulation...")
        simulator.stop()
        print("Exiting Traffic Light Simulator")
    except KeyboardInterrupt:
        simulator.stop()
        print("Stopped Traffic Light Simulator due to interruption")
