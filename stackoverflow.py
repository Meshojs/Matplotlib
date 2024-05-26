from matplotlib import pyplot as plt
import csv
from collections import Counter
import pandas as pd


data = pd.read_csv("d2.csv")
id = data["Responder_id"]
langs = data["LanguagesWorkedWith"]


lan_counter = Counter()

for lang in langs :
  lang = str(lang)
  lan_counter.update(lang.split(";"))


langs = []
pop = []

for item in lan_counter.most_common(15):
  langs.append(item[0])
  pop.append(item[1])

rlangs = langs[::-1]
rpop = pop[::-1]

# plt.bar(langs , pop )
plt.barh(rlangs , rpop)
plt.title("Most used programming langs ")
plt.ylabel("PL")
plt.xlabel("Popularity")

plt.show()


