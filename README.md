# traffic-light-simulator-challenge
:vertical_traffic_light: Program that draws and operates a traditional traffic light :traffic_light:

###  Installation and running the application

* Pre-requisites: The code is written in python. To run this code, you need to have Python 3 installed on your computer
* Clone the repo
    - ```
      git@github.com:akashrventekar/traffic-light-simulator-challenge.git
      ```
* Install the virtual environment and requirements

    - Run the following command:
      - ```commandline
        python3 -m venv venv
        ```
    - Activate the virtual environment:
        - ```commandline
          source venv/bin/activate
          ```
* Install required python packages. These requirements are required only when you want to run tests written with pytest
  - ```
    pip3 install -U -r requirements.txt
    ```
* Run the python code using command line or run it on your IDE

* app.py program gets the input sequentially and prints out results sequentially including multiple runs and inputs
    - You can exit this program by typing exit while providing input or Keyboard interrupt (Ctrl+C)
    - ```commandline
      python app.py
      ```
* chatgpt.py program gets the input sequentially and uses a thread for continuous traffic light simulation
    - You can exit this program by pressing enter or Keyboard interrupt (Ctrl+C)
    - ```commandline
      python chat_gpt.py
      ```
* chatgpt_combined.py program is customized to receive valid input sequentially and uses a thread for continuous traffic light simulation with CLI art
    - You can exit this program by pressing enter or Keyboard interrupt (Ctrl+C)
    - ```commandline
      python chatgpt_combined.py
      ```

    
## Requirements

- [x] The program should take input from a user about how long each light color should stay lit before transitioning
- [x] A graphical user interface or CLI ASCII art are equally acceptable
- [x] Light transitions should be visible to the user
- [x] As your software will be used to operate critical infrastructure a user must not be able to crash the software
- [x] You must print ‘Exiting Traffic Light Simulator’ to the screen when the user instructs the program to exit
- [x] Different message if the simulator must shut itself down.
- [x] You must complete this challenge in Python. 
- [x] (No setup.py or pyinstaller required) You must provide a README file to explain how to build/install and operate your software. Your submission must be your own work. 
- [x] Draws and operates a traditional traffic light.
- [x] You may not send it to us as an email attachment. 
- [x] Add your assumptions

## Evaluation Criteria

- [x] You followed instructions
- [x] Software functions as requested and meets all stated requirements
- [x] (Did not want to pre-maturely optimize the solution with lists) Software is designed for easy extensibility. 
Should you proceed to a later round interview, you will be asked how your software could be modified to accommodate new use cases and traffic light designs. 
You will not be provided with descriptions of these variants at this time.
- [x] Software is designed and implemented for automated testability. It is a benefit if this is demonstrated.
- [x] Software is designed and implemented to support packaging and delivery.
- [x] Software conforms to widely accepted coding style guidelines.
- [x] Software is understandable and supportable by a developer other than yourself.