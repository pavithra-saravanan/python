punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
no_punct = ""
mystr = "Hello!!!, he said ---and went."
for char in mystr:
   if char not in punctuations:
       no_punct = no_punct + char
print(no_punct)

