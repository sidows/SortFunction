command = ""
started = False
while True:
    command = input("> ")
    if command.lower() == "start":
        if started:
            print("The car is already started!")
        else:
            started = True
            print("Starting the car... You started the car.")

    elif command.lower() == "stop":
        if not started:
            print("The car is already stopped!")
        else:
            started = False
            print("Car stopped..")
    elif command.lower() == "help":
        print("Start - Start the car\nStop - Stop the car\nQuit - Quit the program")
    if command.lower() == "quit":
        break
