
import requests 
from bs4 import BeautifulSoup 
  
def find_animals(): 
    url='https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
    animals = {}
    while True:
        resp=requests.get(url)
        soup=BeautifulSoup(resp.text,'html.parser')
        temp = soup.find("div",attrs={"class":"mw-category mw-category-columns"})
        for j in range(200):
            result = temp.find("a").text
            if result[0] == 'A':
                return animals
            if result[0] not in animals:
                animals[result[0]] = 1
            else:
                animals[result[0]] += 1
            temp.find("a").decompose()
        #print(soup.find("a", string="Следующая страница"))
        url = "https://ru.wikipedia.org" + soup.find("a", string="Следующая страница")['href']
        #print(url)
    #now we want to print only the text part of the anchor. 
    #find all the elements of a, i.e anchor 
    """
    for i in l.findAll("a"): 
        print(i.text) 
    """
    
          
if __name__ == "__main__":
    print(find_animals())
