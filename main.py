from bs4 import BeautifulSoup
import requests
import json

def get_info():
    # respons = requests.get("https://valorantinfo.com/ru/agents/")

    # with open("site.txt", "w") as file:
    #     file.write(respons.text)


    try:
        with open("site.txt", "r") as file:
            content = file.read()
            soup = BeautifulSoup(content, "html.parser")
            card_name = soup.find_all("h3", class_="h5 card-title mc-1 m-1")
            cards = []
            for card in card_name:
                cards.append(card.text.strip())
            result_name = {"name": cards}

        with open("info.json", "w", encoding="utf-8") as info:
            json.dump(result_name,info, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Ошибочка): {e}")
    
def main():
    get_info()

if __name__ == "__main__":
    main()