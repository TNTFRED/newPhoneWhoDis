# Trying to mess around with encryption, obviously amature

def textToEncrypt():
  text = input("Input Text to be Encrypted: ")
  return text

def encryptText(text):

  encryptedText = text.replace('a','d')
  encryptedText = encryptedText.replace('A','D')
  encryptedText = encryptedText.replace('b','e')
  encryptedText = encryptedText.replace('B','E')
  encryptedText = encryptedText.replace('c','f')
  encryptedText = encryptedText.replace('C','F') 
  encryptedText = encryptedText.replace('d','g')
  encryptedText = encryptedText.replace('D','G')
  encryptedText = encryptedText.replace('e','h')
  encryptedText = encryptedText.replace('E','H')
  encryptedText = encryptedText.replace('f','i')
  encryptedText = encryptedText.replace('F','I')
  encryptedText = encryptedText.replace('g','j')
  encryptedText = encryptedText.replace('G','J')
  encryptedText = encryptedText.replace('h','k')
  encryptedText = encryptedText.replace('H','K')
  encryptedText = encryptedText.replace('i','l')
  encryptedText = encryptedText.replace('I','L')
  encryptedText = encryptedText.replace('j','m')
  encryptedText = encryptedText.replace('J','M')
  encryptedText = encryptedText.replace('k','n')
  encryptedText = encryptedText.replace('K','O')
  encryptedText = encryptedText.replace('l','p')
  encryptedText = encryptedText.replace('L','P')
  encryptedText = encryptedText.replace('m','q')
  encryptedText = encryptedText.replace('M','Q')
  encryptedText = encryptedText.replace('n','r')
  encryptedText = encryptedText.replace('N','R')
  encryptedText = encryptedText.replace('o','s')
  encryptedText = encryptedText.replace('O','S') 
  encryptedText = encryptedText.replace('p','t')
  encryptedText = encryptedText.replace('P','T')
  encryptedText = encryptedText.replace('q','u')
  encryptedText = encryptedText.replace('Q','U')
  encryptedText = encryptedText.replace('r','v')
  encryptedText = encryptedText.replace('R','V')
  encryptedText = encryptedText.replace('s','x')
  encryptedText = encryptedText.replace('S','X')
  encryptedText = encryptedText.replace('t','y')
  encryptedText = encryptedText.replace('T','Y')
  encryptedText = encryptedText.replace('u','z')
  encryptedText = encryptedText.replace('U','Z')
  encryptedText = encryptedText.replace('v','a')
  encryptedText = encryptedText.replace('V','A')
  encryptedText = encryptedText.replace('w','b')
  encryptedText = encryptedText.replace('W','B')
  encryptedText = encryptedText.replace('x','c')
  encryptedText = encryptedText.replace('X','C')
  encryptedText = encryptedText.replace('y','d')
  encryptedText = encryptedText.replace('Y','D')
  encryptedText = encryptedText.replace('z','e')
  encryptedText = encryptedText.replace('Z','E')

  return encryptedText

print(encryptText(textToEncrypt()))