import requests
import os
from bs4 import BeautifulSoup


def user_search():
    search = raw_input('Enter the name of the title: ')
    url = 'https://www.youtube.com/results?search_query=' + search
    sc = requests.get(url)
    soup = BeautifulSoup(sc.text, 'html.parser')
    title = soup.findAll('h3', {'class': 'yt-lockup-title '})
    link = []
    for i in range(min(10, len(title))):
        link.append(title[i].find('a')['href'])
    for i in range(min(10, len(title))):
        print (str(i+1)+'. '+title[i].find('a').text)
    print("0. Exit")
    return link


while(True):
    choice = int(input("1. Download Song\n2. Download Video\n0. Exit\n"))
    if choice == 0:
        print("\nBye\n")
        break

    if (choice == 1):
        link = user_search()
        while True:
                user_input = int(input('Enter the song number to download: '))
                if user_input == 0:
                    print("\nBye\n")
                    break
                elif user_input not in range(1, 11):
                    print ('Enter a valid song number')
                    continue
                else:
                    print ('Downloading the requested song')
                    os.system("youtube-dl --extract-audio --audio-format mp3  --audio-quality  0 " + 'https://www.youtube.com' + link[user_input-1])
                    print("\n\n")
                    break

    if (choice == 2):
        link = user_search()
        while True:
                user_input = int(input('Enter the video number to download: '))
                if user_input == 0:
                    print("\nBye\n")
                    break
                elif user_input not in range(1, 11):
                    print ('Enter a valid video number')
                    continue
                else:
                    print ('Downloading the requested video')
                    os.system("youtube-dl " + 'https://www.youtube.com' + link[user_input-1])
                    print("\n\n")
                    break

    else:
        print("Choose a valid choice number")
        continue
