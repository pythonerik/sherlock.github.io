print('''
  __  __                        ____          _
 |  \/  | ___  _ __ ___  ___   / ___|___   __| | ___
 | |\/| |/ _ \| '__/ __|/ _ \ | |   / _ \ / _` |/ _ \
 | |  | | (_) | |  \__ \  __/ | |__| (_) | (_| |  __/
 |_|__|_|\___/|_|  |___/\___|  \____\___/ \__,_|\___|
  / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __
 | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |_| |  __/ | | |  __/ | | (_| | || (_) | |
  \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|
''')

morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
              'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
              'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
              '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.':'. _ . _ . _', '?':'. . _ _ . .'}

user_input = input("What would you like to generate into Morse Code? ")

def encrypt(user_input):
    morse_message = ''
    input_upper = user_input.upper()
    for letter in input_upper:
        if letter != ' ':
            if letter in morse_dict:
                morse_message += morse_dict[letter] + ' '
            else:
                morse_message += letter
        else:
            morse_message += ' '
    return morse_message

print(encrypt(user_input))
print(user_input.upper())