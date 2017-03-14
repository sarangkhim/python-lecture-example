import re

#print(re.sub(r'\b(\d{4}-\d{4})', r'<I>\1</I>', 'copyright mincom 1985-2017'))
#print(re.sub(r'-', '@', 'xyz-google.com'))

print(re.findall(r'[^4-6]', '12345678'))
#print(re.findall(r'app|w*', 'application orange banana apple'))

#print(re.split(r'[:. ]+', 'apple orange:banana  .tomato'))
#print(re.split(r'([:. ])+', 'apple orange:banana  .tomato'))

#print(bool(re.match('[0-9]*th', '1th  2017th')))
#print(bool(re.search('[0-9]*th', '   2017th')))
