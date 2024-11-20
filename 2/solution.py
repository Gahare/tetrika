import requests
from bs4 import BeautifulSoup 


def write_to_csv(to_write):
    rus_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' # нетрадиционная сортировка для избежания Ё в начале
    with open("beasts.csv", "w", newline="", encoding="utf-8") as f:
        for i in rus_upper:
            if i in to_write:
                f.write(i+','+str(to_write[i])+'\n')
    f.close()
    return True

def find_animals(): 
    url='https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
    animals = {}
    while True:
        resp=requests.get(url)
        if resp.status_code == 200:
            soup=BeautifulSoup(resp.text,'html.parser')
            temp = soup.find("div",attrs={"class":"mw-category mw-category-columns"}) # поиск контейнера с именами животных
            for j in range(200):
                result = temp.find("a").text
                if result[0] == 'A': #отбрасывание результатов на латынском
                    if write_to_csv(animals) :
                        return True
                    else:
                        return False
                if result[0] not in animals: 
                    animals[result[0]] = 1
                else:
                    animals[result[0]] += 1
                temp.find("a").decompose()
            url = "https://ru.wikipedia.org" + soup.find("a", string="Следующая страница")['href']
        else:
            print("Ошибка запроса страницы википедии")
    
          
if __name__ == "__main__":
    if find_animals():
        print("OK")
    else:
        print("Error")
