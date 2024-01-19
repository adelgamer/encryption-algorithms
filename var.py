import random, os, subprocess, math, lan, itertools

html_markup = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  
</body>
</html>"""

def folder(path, name):
  path = path + name + str(random.randint(1111111, 9999999))
  os.mkdir(path)
  return path

def open_vscode(path):
  try:
    subprocess.Popen(["code", path])
    return True
  except:
    return False

def path_to_name(path, extension = True):
  if extension:
    name = path.split("\\")[-1]
  
  elif not extension:
    name = path.split("\\")[-1].split(".")[-2]
  return name

def s1(goestat = 6, regional = 3.5, geophisique = 5.25):
    #calculation for geostat
    required_geostat = ((170 - (regional * 3) - 21 - 38.7 - 53 - (geophisique * 2) - 16.5))/2
    #calculate for regional
    required_regional = ((170 - (goestat * 2) - 21 - 38.7 - 53 - (geophisique * 2) - 16.5))/3
    #calculate for geophisique
    required_geophisique = ((170 - (goestat * 2) - 21 - 38.7 - 53 - (regional * 3) - 16.5))/2
    return [
    ("Geostat", required_geostat, math.ceil(required_geostat)),
    ("Regional", required_regional, math.ceil(required_regional)),
    ("Geophisique", required_geophisique, math.ceil(required_geophisique))
]
    
def s2(geotech = 1, hydro = 4.5, regional = 4):
    #calculation for geotech
    required_geotech = (140 - (regional * 3) - 20 - 20.7 - 25 - (hydro * 2) - 12 - 13)/2
    #calculate for regional
    required_regional = ((140 - (hydro * 2) - 20 - 20.7 - 25 - (geotech * 2) - 12 - 13))/4
    #calculate for hydro
    required_hydro = ((140 - (geotech * 2) - 20 - 20.7 - 25 - (regional * 4) - 12 - 13))/2
    return [
    ("Geotech", required_geotech, math.ceil(required_geotech)),
    ("Hydro", required_hydro, math.ceil(required_hydro)),
    ("Regional", required_regional, math.ceil(required_regional))
]


def cipher(text = "test", key = 1, direction = "right"):
    #the math.fabs() finction get you the absolute value of a number for example -5 beomes 5
    #checking if the key doesn't exceeed 25
    if math.fabs(key) > 25:
        raise Exception(f"'{key}' is an invalid key, key must be smaller than 25 or greater then -25")
    #making sure the input is in lower case
    text = text.lower()
    #alphabet list
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
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
                raise Exception(f"'{direction}' is an invalid diraction, direction must be either 'left' or 'right'")
        else:
            #adding the the special character to the output
            output += letter
    return output
        
def brute_force(text):
  list = []
  for index in range(26):
    output = cipher(text, index, "left")
    success_percentage_english = lan.recognise_english(output)
    success_percentage_french = lan.recognise_french(text)
    #printing for fun
    # print(output)
    # print(success_percentage)
    # print("\n")
    if success_percentage_english >= 90 or success_percentage_french >= 90:
      list.append((output, index))
  return list

def cipher2(text = "default", key="default", direction = "right"):
    #to lower case characters
    text = text.lower()
    try:
      key = key.lower()
    except AttributeError:
      raise Exception("Key must be a text not a number")
    #alphabet list
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    #lenght of the text to cipher and key
    lenght_text = len(text)
    lenght_key = len(key)
    #checking if key is longer then text or shorter
    if lenght_key > lenght_text:
        #Here key is longer then the text that i'am making it equal to text in lenght
        key = key[:lenght_text]
    elif lenght_key < lenght_text:
        #key lenght is shorter then text that means i'am making it longer then it by muliplying it by the the lenght ratio between
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
            ciphered_character = cipher(text_character, index, direction)
            #appending ciphered character to output
            output += ciphered_character
        else:
            #appending special character without ciphering them
            output += text_character
    return output
  
def brute_force2(text, lenght):
    #alphabet list
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    possible_solutions = []
    # total_iterations = 26 ** lenght
    count = 0
    for i in range(1, lenght + 1):
      count += 1
      combinations = list(itertools.product(alphabet, repeat=i))
      for combo in combinations:
          # print(str((count * 100)/total_iterations) + " %")
          combo = "".join(combo)
          # print(combo)
          output = cipher2(text, combo, "left")
          if lan.recognise_english(output) > 90:
            possible_solutions.append((output, combo))
            print(output + "   " + combo + "\n")
    return possible_solutions

python_programs_dir = "D:\\Programming\\Python\\"
websites_dir = "D:\\xampp\\htdocs\\adelweb\\"
edge = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
python_docs = "C://Users//Adel//AppData//Local//Programs//Python//Python312//Doc//html//index.html"
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]