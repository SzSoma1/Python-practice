abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
def caesar(og_text, shift_am, encode_or_decode):
    caesar_text = ""
    if encode_or_decode == "decode":
                shift_am *= -1
    for letter in og_text:
        if letter not in abc:
            caesar_text += letter
        else:
            shifted_pos = abc.index(letter) + shift_am
            shifted_pos %= len(abc)
            caesar_text += abc[shifted_pos]
    print(f"Here is the result: {caesar_text}")
    
run = True

while run:
    direction = input("Type 'encode' or decode!:\n").lower()
    text = input("Type ur message:\n").lower()
    shift = int(input("Type ur shift number!:\n"))
        
    caesar(og_text=text, shift_am=shift, encode_or_decode=direction)
    restart = input("Type 'yes' if u go again or type 'no' if u dont\n").lower()
    if restart == "no":
        run = False
        print("Goodbye!")
    