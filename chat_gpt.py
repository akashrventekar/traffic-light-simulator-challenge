# This is the chatgpt solution. Very Elegant ;) Just need to add exception handling to make this perfect

import time
import threading

class TrafficLightSimulator:
    def __init__(self):
        self.green_duration = 0
        self.yellow_duration = 0
        self.red_duration = 0
        self.running = False

    def set_light_durations(self):
        self.green_duration = int(input("Enter green light duration (seconds): "))
        self.yellow_duration = int(input("Enter yellow light duration (seconds): "))
        self.red_duration = int(input("Enter red light duration (seconds): "))

    def traffic_light(self):
        while self.running:
            print("\033[32mGREEN\033[0m")
            time.sleep(self.green_duration)
            print("\033[33mYELLOW\033[0m")
            time.sleep(self.yellow_duration)
            print("\033[31mRED\033[0m")
            time.sleep(self.red_duration)

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
        input("Press Enter to stop the simulation...")
        simulator.stop()
        print("Exiting Traffic Light Simulator")
    except KeyboardInterrupt:
        simulator.stop()
        print("Traffic Light Simulator shutdown due to interruption.")
