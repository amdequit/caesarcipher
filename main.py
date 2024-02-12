#caesar cipher encoder, decoder
import time


alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

"""
  This function takes a string message and an integer shift as input, and prints the original message and encoded message.
"""
def encode(message, shift):
  encoded_message = ""
  print(message)
  message = message.lower()
  for letter in message:
    if letter in alphabet:
      letter_index = alphabet.index(letter)
      new_index = (letter_index + shift) % 26
      encoded_message += alphabet[new_index]
    else:
      encoded_message += letter  # for special characters: if not in alphabet, leave as is
  print(encoded_message)

"""
  This function takes a string message and an integer shift as input, and prints the original message and decoded message.
"""
def decode(message, shift):
  decoded_message = ""
  print(message)
  message = message.lower()
  for letter in message:
    if letter in alphabet:
      letter_index = alphabet.index(letter)
      new_index = (letter_index - shift) % 26
      decoded_message += alphabet[new_index]
    else:
      decoded_message += letter
  print(decoded_message)


"""
  This main function provides a menu for the user to choose whether to encode or decode a message.
"""
def main():
  print("Caesar Cipher: Encoder and Decoder")
  time.sleep(1)
  start = True
  while start is True:
    user_choice = input("\nWould you like to encode or decode a message?\n1) Encode\n2) Decode\n3) Quit\n")
    if user_choice == "1":
      message = input("Enter the message you would like to encode: ")
      shift = int(input("Enter the shift value: "))
      print()
      encode(message, shift)
    if user_choice == "2":
      message = input("Enter the message you would like to decode: ")
      shift = int(input("Enter the shift value: "))
      print()
      decode(message, shift)
    if user_choice == "3":
      print("\nNow exiting...")
      time.sleep(1) 
      print("Exited. Goodbye!")
      start = False
      break


main()
    
  
  

