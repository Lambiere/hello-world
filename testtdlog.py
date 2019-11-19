import pandas as pd

file = 'capitales.csv'

cap = pd.read_csv(file, sep = ",", encoding = "ISO-8859-1")

list_cap = cap['Capitale'].__array__()
list_pays = cap['Pays'].__array__()

list_pays_str = ['' for i in range(len(list_pays))]
list_articles_pays = ['' for i in range(len(list_pays))]

k = 0

for pays in list_pays:
    i = 0
    j = 0
    while i < len(pays):
        if (pays[i] == '('):
            j = i
            i += 3
            while (pays[i] != ')'):
                i+=1
            list_pays_str [k] = pays[:j-1]
            list_articles_pays[k] = pays[j+1:i]
        i += 1
    k += 1
    print(k)

liste_pays_avec_articles = [list_articles_pays[i] + ' ' + list_pays_str[i] for i in range(len(list_pays_str))]