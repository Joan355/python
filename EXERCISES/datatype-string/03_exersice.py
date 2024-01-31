"""Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String """

def getF2L2(text:str) -> str:
    lenght = len(text)
    if lenght >= 2:
        return text[0:2] + text[-2:]
    else:
        return ""

result = getF2L2("w3resource")
print(result)

result = getF2L2("w3")
print(result)

result = getF2L2(" w")
print(result == "")


