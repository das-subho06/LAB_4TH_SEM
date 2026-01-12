import string
s=input("Enter a sentence: ")
new_s=s
for character in string.punctuation:
    s=s.replace(character,'')
print(s)
s=s.lower()
print(s)
words=s.split()
print(words)
req_dict={}
for i in words:
    if i in req_dict:
        req_dict[i]=req_dict[i]+1
    else:
        req_dict[i]=1
def getvalue(item):
    return item[1]
sorted_words = sorted(req_dict.items(),key=getvalue,reverse=True)
sorted_dict=dict(sorted_words)
print(f"Sorted dictionary is: {sorted_dict}")

