text="Python is easy and Python is powerful"
words=text.lower().split()
count={}
for word in words:
    count[word]=count.get(word,0)+1
print(count)