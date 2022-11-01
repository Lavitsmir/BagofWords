#Enzo Bloss Stival
"""Sua tarefa será  gerar a matriz termo documento, dos documentos recuperados da internet e 
imprimir esta matriz na tela. Para tanto: 
a) Considere que todas as listas de sentenças devem ser transformadas em listas de vetores, 
onde cada item será uma das palavras da sentença. 
b) Todos  os  vetores  devem  ser  unidos  em  um  corpus  único  formando  uma  lista  de  vetores, 
onde cada item será um lexema.  
c) Este único corpus será usado para gerar o vocabulário. 
d) O  resultado  esperado  será  uma  matriz  termo  documento  criada  a  partir  da  aplicação  da 
técnica bag of Words em todo o corpus.  
"""
from bs4 import BeautifulSoup
import requests
import pandas
import re

sentencas = []
urls = ["https://www.ibm.com/cloud/learn/natural-language-processing", "https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP", "https://www.datarobot.com/blog/what-is-natural-language-processing-introduction-to-nlp/", "https://hbr.org/2022/04/the-power-of-natural-language-processing", "https://machinelearningmastery.com/natural-language-processing/"]
for link in urls:
    url = requests.get(link).content
    html = BeautifulSoup(url, "html.parser")
    for data in html(['style', 'script']):
        data.decompose()
    html = ' '.join(html.stripped_strings)
    html = re.sub("[\n\t]", "", html)
    html = re.split("[.!:?;]", html)
    sentencas.append(html)
palavras = set()
matriz = []
for sentenca in sentencas:
    for frase in sentenca:
        for palavra in frase.split():
            palavras.add(palavra)
palavras = list(palavras)
contagem = [0] * len(palavras)
print(palavras)

for sentenca in sentencas:
    for frase in sentenca:
        for palavra in frase.split():
            contagem[palavras.index(palavra)] += 1
    matriz.append(contagem)
    contagem = [0] * len(palavras)

matriz = pandas.DataFrame(matriz, columns=palavras)
display(matriz)
