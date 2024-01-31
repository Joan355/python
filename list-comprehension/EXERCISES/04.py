
string = "Yellow Yaks like yelling And yawning and yesturday they yodled while eating yuky yams"

vowels = "aeiou"
result = {c for c in string if c.lower() not in vowels + " "}
print(result)