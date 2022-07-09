import string
def encode_text():
    letters = list(string.ascii_lowercase)
    istring = input("Enter the text to encode: ")
    slist = list(istring)
    encoded = []
    for item in slist :
      if item == "." :
       znum = "::"
      elif item == " ":
       znum ="##"
      elif item == ",":
       znum ="$$"
      elif item == "?":
       znum = ";;"
      else:
       if item.isupper() :
        num = letters.index(item.lower()) +1
       else:
        num = letters.index(item) +1
       znum = str(num).zfill(2)
      encoded.append(znum)
		
    encodedstring = "".join(encoded)
    print(encodedstring)

def decode_text():
  text2decode = input("Enter the text to decode : ")
  list1 = text2decode[::2]
  list2 = text2decode[1::2]
  result =[]
  zippedtuple = [*zip(list1,list2)]
  for item1,item2 in zippedtuple :
    finalnum = item1+item2
    if finalnum == "::" :
       resultchar = "."
       result.append(resultchar)
    elif finalnum == "##":
       resultchar =" "
       result.append(resultchar)
    elif finalnum == "$$":
       resultchar =","
       result.append(resultchar)
    elif finalnum == ";;":
       resultchar = "?"
       result.append(resultchar)
    else:
      result.append(string.ascii_lowercase[int(finalnum) - 1])
          

      
  decodedstring = "".join(result)
  print(decodedstring)

print("""
1. Encode Text
2. Decode Text
""")
choice = input("Enter Your Choice: ")
if choice == "1" :
  encode_text()
elif choice == "2" :
  decode_text()
else :
  print("Enter Correct Choice!")




