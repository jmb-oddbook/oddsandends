# ------------------------------------
# From Angela Yu's "100 Days of Code"
# ------------------------------------

# Caesar Cipher

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cypher(dir, plaintext, shift_nr):
    cypher_text = ""
    if dir == "encode":
        for letter in plaintext:
            new_position = (alpha.index(letter) + shift_nr)%26
            cypher_text += alpha[new_position]
    else:
        for letter in plaintext:
            new_position = (alpha.index(letter) - shift_nr)%26
            cypher_text += alpha[new_position]
    return cypher_text
    
again = "yes"

while again == "yes":
    direction = input("Type 'encode', or 'decode': ")
    # ToDo: regex filter for punctuation
    message = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    
    # Output
    print(f"The {direction}d message is " + caesar_cypher(direction, message, shift))
    
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.")

print("Goodbye!")
