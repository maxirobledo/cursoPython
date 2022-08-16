str ='X-DSPAM-Confidence:0.8475'
pos = str.find(':')
#pos = 18
number = float(str[19:])
print(number)