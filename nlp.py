import string
text=open("hello.txt",encoding="UTF-8").read()
# print(text)
lower=text.lower()
# print(lower)
finned=lower.replace("\n","")
# print(finned)
clean=finned.translate(str.maketrans("","",string.punctuation))
# print(clean)
token_words=clean.split(" ")
print(token_words)
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
cleanned=[]
for i in token_words:
    if i not in stop_words:
        cleanned.append(i)
print(cleanned)
d=[]
with open("emotion.txt","r",encoding="UTF_8") as f:
    for i in f:
        klen=i.replace("\n","").replace(",","").strip().replace(" ","").replace("'","")
        word,emotion=klen.split(":")
        if word in cleanned:
            d.append(emotion)
from collections import Counter
w=Counter(d)
print(w)
import matplotlib.pyplot as plt
fig,ax=plt.subplots()
ax.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig("graph.png")
plt.show()