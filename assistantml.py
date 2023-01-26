#Updated Code to include machine learning using pytorch and RoBERTa
import random
import importlib
import torch
from transformers import RobertaTokenizer, RobertaForMaskedLM
from commands import assistantvoice
import tokenizer

commandslist = ["endprogram", "flip", "joke", "roll", "settimer", "time", "add", "subtract", "multiply", "divide", "searchgoogle", "imagesearch", "openapp"]

#other variables
wakeupreply = ("Hello, What would you like me to do?", "Yes?", "How can I help?")
command = ''
vort = ''

# Load the RoBERTa tokenizer and model
tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
model = RobertaForMaskedLM.from_pretrained('roberta-base')

def voiceortext(finding):
    if vort == "voice":
        thing = assistantvoice.takeCommand()
    elif vort == "text":
        thing = input(f"{finding}: ")
    return thing

#Do you want to type or talk
if vort != 'text' and vort != 'voice':
    vort = input("Would You like to start in text or voice mode? ")
    vort = vort.lower()

print(f"You Chose {vort} Mode")

#Always Runs
while True:
    

    if vort == "voice":
        wakeup = assistantvoice.takeCommand()
        assistantvoice.speak(random.choice(wakeupreply))

    elif vort == "text":
        assistantvoice.speak(random.choice(wakeupreply))
        wakeup = "sam"

    #if wakeup word heard
    if 'Sam' or 'Samantha' in wakeup:
        command = voiceortext("Command")
        for cmd in commandslist:
            module = importlib.import_module(f'commands.{cmd}')
            if module.command_matches_input(command):
                module.execute(command)
                break
        else:
            # Use RoBERTa to predict the next word
            input_ids = torch.tensor(tokenizer.encode(command)).unsqueeze(0)  # Batch size 1
            outputs = model(input_ids)[0]
            most_likely_token_id = outputs.max(dim=1)[1]
            most_likely_token = tokenizer.decode(most_likely_token_id)
            most_likely_token = tokenizer.decode(most_likely_token_id)
            print(most_likely_token)
            assistantvoice.speak(f"I'm sorry, I don't understand that command. Did you mean {most_likely_token}?")

    #if wakeup word not heard
    else:
        command = voiceortext("Command")
        for cmd in commandslist:
            module = importlib.import_module(f'commands.{cmd}')
            if module.command_matches_input(command):
                module.execute(command)
                break
        else:
            # Use RoBERTa to predict the next word
            input_ids = torch.tensor(tokenizer.encode(command)).unsqueeze(0)  # Batch size 1
            outputs = model(input_ids)[0]
            most_likely_token_id = outputs.max(dim=1)[1]
            most_likely_token = tokenizer.decode(most_likely_token_id)
            most_likely_token = tokenizer.decode(most_likely_token_id)
            print(most_likely_token)
            assistantvoice.speak(f"I'm sorry, I don't understand that command. Did you mean {most_likely_token}?")