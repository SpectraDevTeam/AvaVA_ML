from commands import assistantvoice

def command_matches_input(input):
    if input == "":
        return True
    else:
        return False

def execute(input):
    
    assistantvoice.speak("Fuck you. I Didn't hear no command")