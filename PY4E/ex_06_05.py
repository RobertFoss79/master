# str = "X-DSPAM-Confidence: 0.8475"

# ipos = str.find(":")
# # print(ipos)
# piece = str[ipos + 2:]
# # print(piece)
# value = float(piece)
# print(value + 42.0)

text = "X-DSPAM-Confidence:    0.8475"

ipos = text.find(":")
# print(ipos)
piece = text[ipos + 1:].strip()
value = float(piece)
print(piece)
