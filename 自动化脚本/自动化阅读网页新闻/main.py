import pyttsx3
import requests
from bs4 import BeautifulSoup

def speak(engine,audio):
    engine.say(audio)
    engine.runAndWait
    return None

def main():
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('vocies')
    newVoiceRate=130
    engine.setProperty('rate',newVoiceRate)
    text=str(input("Paste article\n"))
    res=requests.get(text)
    soup=BeautifulSoup(res.text,'html.parser')

    articles=[]
    for i in range(len(soup.select('.p'))):
        article=soup.select('.p')[i].getText.strip()
        articles.append(article)
    text=" ".join(articles)
    speak(engine,text)
    return None

if __name__=='__main__':
    main()