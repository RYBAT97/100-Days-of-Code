import string

alphabet = list(string.ascii_lowercase)
print('''
 $$$$$$\                                                           $$$$$$\  $$\           $$\                           
$$  __$$\                                                         $$  __$$\ \__|          $$ |                          
$$ /  \__| $$$$$$\   $$$$$$\   $$$$$$$\  $$$$$$\   $$$$$$\        $$ /  \__|$$\  $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  
$$ |       \____$$\ $$  __$$\ $$  _____| \____$$\ $$  __$$\       $$ |      $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$ |       $$$$$$$ |$$$$$$$$ |\$$$$$$\   $$$$$$$ |$$ |  \__|      $$ |      $$ |$$ /  $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |  $$\ $$  __$$ |$$   ____| \____$$\ $$  __$$ |$$ |            $$ |  $$\ $$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |      
\$$$$$$  |\$$$$$$$ |\$$$$$$$\ $$$$$$$  |\$$$$$$$ |$$ |            \$$$$$$  |$$ |$$$$$$$  |$$ |  $$ |\$$$$$$$\ $$ |      
 \______/  \_______| \_______|\_______/  \_______|\__|             \______/ \__|$$  ____/ \__|  \__| \_______|\__|      
                                                                                $$ |                                    
                                                                                $$ |                                    
                                                                                \__|                                    
''')


def encode_decode(input_text, shift_count, mode):
    if mode == "decode":
        shift_count *= -1
    j = 0
    for item in input_text:
        if item in alphabet:
            current_index = alphabet.index(item)
            new_index = current_index - shift_count
            if new_index > len(alphabet):
                new_index -= len(alphabet)
            elif new_index < 0:
                new_index += len(alphabet)
            input_text[j] = alphabet[new_index]
        j += 1
    print(f"The {mode}ed text for your input will be: {''.join(input_text)}")


while True:
    EncOrDec = input("Would you like to encode or decode text?\n")
    text = list(input("Please enter your text: ").lower())
    shift = int(input("Please enter the margin shift digit you would like to use: "))
    # while 2 > shift or shift > 25:
    #     shift = int(input("Wrong input! Enter shift value between 1 and 25: "))
    if shift > 26 or shift < 0:
        shift = shift % 26
    encode_decode(list(text), shift, EncOrDec)

    again = input("Would you like to restart? (Y/n)\n")
    if again.lower() == "n":
        break

