# Morse Code Translator

# Define Morse code mappings (you can extend this as needed)
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' '
}

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        else:
            morse_code += char + ' '
    return morse_code

def morse_to_text(morse_code):
    words = morse_code.split('  ')
    text = ''
    for word in words:
        chars = word.split(' ')
        for char in chars:
            if char in morse_code_dict.values():
                text += list(morse_code_dict.keys())[list(morse_code_dict.values()).index(char)]
        text += ' '
    return text

while True:
    print("Options:")
    print("1: Text to Morse Code")
    print("2: Morse Code to Text")
    print("3: Quit")
    
    choice = input("Enter option (1/2/3): ")
    
    if choice == '1':
        text = input("Enter text to convert to Morse Code: ")
        morse_code = text_to_morse(text)
        print("Morse Code:", morse_code)
    elif choice == '2':
        morse_code = input("Enter Morse Code to convert to text: ")
        text = morse_to_text(morse_code)
        print("Text:", text)
    elif choice == '3':
        break
    else:
        print("Invalid Input")

