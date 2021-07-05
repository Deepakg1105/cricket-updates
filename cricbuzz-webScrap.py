from bs4 import BeautifulSoup
import time
import requests

FAIL = '\033[91m' #red
ENDC = '\033[0m'
BOLD = '\033[1m'
GREEN = '\033[92m'
BLUE = '\033[94m'

def web_scrap():
   

    #s = input("Google for : ")
    #param = {"q", search}
    search = "https://www.cricbuzz.com/"
    html_doc = requests.get(search).content
    soup = BeautifulSoup(html_doc, 'lxml')
    #print(soup.prettify())

    #class_list=soup.find_all('div', class_='cb-col cb-col-100 cb-mini-col cb-min-comp ng-scope')
    class_list=soup.find_all('li', class_='cb-col cb-col-25 cb-mtch-blk cb-vid-sml-card-api videos-carousal-item cb-carousal-item-large cb-view-all-ga')
    print("\n\n\n" + BLUE + BOLD + "------------------C r i c k e t - U p d a t e s-----------------" + ENDC + "\n")
    for i in class_list:
        print(i.get_text())
        print()

if __name__ == "__main__":
    while True:
        web_scrap()
        print(GREEN + BOLD + "R E F R E S H I N G ....." + ENDC + "\t" + FAIL + "*** Hit CTRL+C to stop ***" + ENDC)
        #sleep(60 - time() % 60)
        time.sleep(30)  #run after every 30 seconds
