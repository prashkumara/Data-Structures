paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
paragraph=paragraph.lower()
paragraph = filter(str.isalnum(), paragraph)

print(paragraph)
banned = ["hit"]

words = paragraph.split(" ")
hashmap={}
for w in words:
    print(w)
    if w not in banned:
        if w not in hashmap:
            hashmap.update({w:1})
        else:
            hashmap.update({w:hashmap[w]+1})
print(hashmap)