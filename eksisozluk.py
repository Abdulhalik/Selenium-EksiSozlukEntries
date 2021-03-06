from selenium import webdriver
import time
import random

browser = webdriver.Chrome('/Users/abdulhalik/PycharmProjects/Selenium-EksiSozlukEntries/venv/chromedriver')
URL = "https://eksisozluk.com/fatih-sultan-mehmet--42269?p="

pageCount = 1
entryCount = 1
entries = []
randomPages = []
# Generate random pages until 10 and browse them every 3 seconds
# -- 10 sayfa olana kadar 3 saniyede bir rastgele sayfa üret
while pageCount <= 10:
    randomPage = random.randint(1, 65)
    randomPages.append(randomPage)
    # Add random page number to end of the url
    # -- URL'in sonuna rastgele üretilmiş sayfa numarası ekle
    newUrl = URL + str(randomPage)
    browser.get(newUrl)
    # Get elements named on Content in that page
    # -- Content isimli elementleri sayfadan al
    # For multiple element use find_elements.... instead of find element....
    elements = browser.find_elements_by_css_selector('.content')
    # And push them into the Entry List for each page
    # -- Ve her birinin listeye ekle
    for element in elements:
        entries.append(element.text)
    time.sleep(3)
    pageCount += 1

pageCount = 1

# Write all entries into the Txt File
with open("entries.txt", "w", encoding= "UTF-8") as file:
    file.write("EKSI SOZLUK - SOME ENTRIES ABOUT FATIH SULTAN MEHMED HAN \n")
    file.write("Generated Pages: ")
    for pageNumber in randomPages:
        file.write(str(pageNumber) + " - ")
    file.write("\n------------------------------------------------------\n")
    for entry in entries:
        file.write(str(pageCount) + ".\n" + entry + "\n")
        file.write("************************************\n")
        pageCount += 1

browser.close()
