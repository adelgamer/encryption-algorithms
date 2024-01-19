import math, itertools

class cipher:
  def ceaser_cipher(text = "test", key = 1, direction = "right"):
      #the math.fabs() finction get you the absolute value of a number for example -5 beomes 5
      #checking if the key doesn't exceeed 25
      if math.fabs(key) > 25:
          raise Exception(f"'{key}' is an invalid key, key must be smaller than 25 or greater then -25")
      #making sure the input is in lower case
      text = text.lower()
      #alphabet list
      alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",  "t", "u", "v", "w", "x", "y", "z"]
      #lenght of the list alphabet
      lenght = len(alphabet)
      #placeholder string to encode or decode
      output = ""
      #iterating in the text provided as an argument letter by letter
      for letter in text:
          #checking if the letter is not a special character by checking if it's in alphabet list
          if letter in alphabet:
              #getting the index of the letter inside the alphabet list
              letter_index = alphabet.index(letter)
              #checking the direction of the cipher 'right' or 'left"
              if direction == "right":
                  #checkin if alternative index exceed the list lenght which would cause undex out range error
                  #solving this problem by subtracting the lenght of the list by the alternative index
                  if math.fabs(letter_index + key) >= lenght:
                      #getting the alternative index for the cipher letter in alphabet list
                      alternative_index = (letter_index + key) - lenght 
                      #adding the letter with the alternative index to the output
                      output += alphabet[alternative_index]
                  else:
                      #getting the alternative index for the cipher letter in alphabet list
                      alternative_index = letter_index + key
                      #adding the letter with the alternative index to the output
                      output += alphabet[alternative_index]
              elif direction == "left":
                  #checkin if alternative index exceed the list lenght which would cause undex out range error
                  #solving this problem by subtracting the lenght of the list by the alternative index
                  if math.fabs(letter_index - key) >= lenght:
                      #getting the alternative index for the cipher letter in alphabet list
                      alternative_index = (letter_index - key) - lenght
                      #adding the letter with the alternative index to the output
                      output += alphabet[alternative_index]
                  else:
                      #getting the alternative index for the cipher letter in alphabet list
                      alternative_index = letter_index - key
                      #adding the letter with the alternative index to the output
                      output += alphabet[alternative_index]
              else:
                  raise Exception(f"'{direction}' is an invalid diraction, direction must be either 'left' or   'right'")
          else:
              #adding the the special character to the output
              output += letter
      return output


  def vineger_cipher(text = "default", key="default", direction = "right"):
      #to lower case characters
      text = text.lower()
      try:
        key = key.lower()
      except AttributeError:
        raise Exception("Key must be a text not a number")
      #alphabet list
      alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",  "t", "u", "v", "w", "x", "y", "z"]
      #lenght of the text to cipher and key
      lenght_text = len(text)
      lenght_key = len(key)
      #checking if key is longer then text or shorter
      if lenght_key > lenght_text:
          #Here key is longer then the text that i'am making it equal to text in lenght
          key = key[:lenght_text]
      elif lenght_key < lenght_text:
          #key lenght is shorter then text that means i'am making it longer then it by muliplying it by the the   lenght ratio between
          #text lenght and key lenght
          #i used math ceil to round up and to avoid error caused by multiplication of string in decimal number 
          key = key * (math.ceil(lenght_text/lenght_key))
          #adding white spaces and special characters to the key 
          count = 0
          for character in text:
              if character not in alphabet:
                  key = key[:count] + character + key[count:]
              count += 1
          #checking if key is longer than text
          if len(key) > len(text):
              #if the new key is longer than text make it's lenght equal to text lenght
              key = key[:len(text)]
      #definign output variable
      output = ""
      #iterating in text and key
      for text_character, key_character in zip(text, key):
          #checking if text not a special character by checking if it's inside alphabet
          if text_character in alphabet:
              #determining index from alphabet list based on key_character
              index = alphabet.index(key_character)
              #ciphering character
              ciphered_character = cipher.ceaser_cipher(text_character, index, direction)
              #appending ciphered character to output
              output += ciphered_character
          else:
              #appending special character without ciphering them
              output += text_character
      return output
    
#Testing
# while (True):
#   text = input("Enter a text:\n")
#   print(cipher.vineger_cipher(text, "adel"))
#   print("\n")