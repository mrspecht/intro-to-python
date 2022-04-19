# Flow control (continue)

films = ["Terminator", "Robocop", "Big", "Back to the future"]

for film in films:                                                              # 'continue' is a statement that causes the flow to stop the
    if film == "Robocop":                                                       # execution of the current iteration and go on to the next,
        continue                                                                # preventing any other instruction from being executed
    print(film)
