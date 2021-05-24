from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from threading import Thread
from time import sleep

twitchgamers1 = [
    'https://www.twitch.tv/Foolish__Gamers/clips?filter=clips&range=24hr',
    'https://www.twitch.tv/Ranboolive/clips?filter=clips&range=24hr'
    'https://www.twitch.tv/Philza/clips?filter=clips&range=24hr',
    'https://www.twitch.tv/Tubbolive/clips?filter=clips&range=24hr'
]
twitchgamers2 = [
    'https://www.twitch.tv/tommyinnit/clips?filter=clips&range=24hr',
    'https://www.twitch.tv/sapnap/clips?filter=clips&range=24hr',
    'https://www.twitch.tv/CaptainPuffy/clips?filter=clips&range=24hr',
    'https://www.twitch.tv/quackity/clips?filter=clips&range=24hr'
]
twitchgamers3 = [
    'https://www.twitch.tv/fundy/clips?filter=clips&range=24hr',
    'https://www.twitch.tv/tubbo/clips?filter=clips&range=24hr',
    'https://www.twitch.tv/jackmanifoldtv/clips?filter=clips&range=24hr',
    'https://www.twitch.tv/punz/clips?filter=clips&range=24hr'
]
twitchgamers4 = [
    'https://www.twitch.tv/quackity/clips?filter=clips&range=24hr',
    'https://www.twitch.tv/ranboobutnot/clips?filter=clips&range=24hr',
    'https://www.twitch.tv/hbomb94/clips?filter=clips&range=24hr',
    'https://www.twitch.tv/badboyhalo/clips?filter=clips&range=24hr'
]
twitchgamers5 = [
    'https://www.twitch.tv/tapl/clips?filter=clips&range=24hr',
    'https://www.twitch.tv/CaptainSparklez/clips?filter=clips&range=24hr'
]
results = []
def websession1():
    global results
    driver = webdriver.Chrome('C:\Webdrivers\chromedriver.exe')
    for address in twitchgamers1:
        driver.get(address)
        sleep(3)
        links = driver.find_elements_by_xpath("(//a[@data-a-target='preview-card-image-link'])[position()<=4]")
        card = driver.find_element_by_xpath("//a[@data-a-target='preview-card-image-link']")
        card.send_keys(Keys.END)
        sleep(0.1)
        views = driver.find_elements_by_xpath("(//div[@class='sc-AxjAm iVDSNS']/div[1]/p[1])")
        for link, view in zip(links,views):
            results.append([link.get_attribute('href'),view.text])
def websession2():
    global results
    driver = webdriver.Chrome('C:\Webdrivers\chromedriver.exe')
    for address in twitchgamers2:
        driver.get(address)
        sleep(3)
        links = driver.find_elements_by_xpath("(//a[@data-a-target='preview-card-image-link'])[position()<=4]")
        card = driver.find_element_by_xpath("//a[@data-a-target='preview-card-image-link']")
        card.send_keys(Keys.END)
        sleep(0.1)
        views = driver.find_elements_by_xpath("(//div[@class='sc-AxjAm iVDSNS']/div[1]/p[1])")
        for link, view in zip(links,views):
            results.append([link.get_attribute('href'),view.text])
def websession3():
    global results
    driver = webdriver.Chrome('C:\Webdrivers\chromedriver.exe')
    for address in twitchgamers3:
        driver.get(address)
        sleep(3)
        links = driver.find_elements_by_xpath("(//a[@data-a-target='preview-card-image-link'])[position()<=4]")
        card = driver.find_element_by_xpath("//a[@data-a-target='preview-card-image-link']")
        card.send_keys(Keys.END)
        sleep(0.1)
        views = driver.find_elements_by_xpath("(//div[@class='sc-AxjAm iVDSNS']/div[1]/p[1])")
        for link, view in zip(links,views):
            results.append([link.get_attribute('href'),view.text])
def websession4():
    global results
    driver = webdriver.Chrome('C:\Webdrivers\chromedriver.exe')
    for address in twitchgamers4:
        driver.get(address)
        sleep(3)
        links = driver.find_elements_by_xpath("(//a[@data-a-target='preview-card-image-link'])[position()<=4]")
        card = driver.find_element_by_xpath("//a[@data-a-target='preview-card-image-link']")
        card.send_keys(Keys.END)
        sleep(0.1)
        views = driver.find_elements_by_xpath("(//div[@class='sc-AxjAm iVDSNS']/div[1]/p[1])")
        for link, view in zip(links,views):
            results.append([link.get_attribute('href'),view.text])
def websession5():
    global results
    driver = webdriver.Chrome('C:\Webdrivers\chromedriver.exe')
    for address in twitchgamers5:
        driver.get(address)
        sleep(3)
        links = driver.find_elements_by_xpath("(//a[@data-a-target='preview-card-image-link'])[position()<=4]")
        card = driver.find_element_by_xpath("//a[@data-a-target='preview-card-image-link']")
        card.send_keys(Keys.END)
        sleep(0.1)
        views = driver.find_elements_by_xpath("(//div[@class='sc-AxjAm iVDSNS']/div[1]/p[1])")
        for link, view in zip(links,views):
            results.append([link.get_attribute('href'),view.text])


if __name__ == "__main__":
    thread1 = Thread(target = websession1)
    thread2 = Thread(target = websession2)
    thread3 = Thread(target = websession3)
    thread4 = Thread(target = websession4)
    thread5 = Thread(target = websession5)
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    print("thread finished...exiting")

for result in results:
    result[1] = result[1][:-6]
    if 'K' in result[1]:
        if '.' in result[1]:
            result[1] = result[1].replace('.', '')
            result[1] = result[1].replace('K', '00')
        else:
            result[1] = result[1].replace('K', '000')
    else:
        pass
    result[1] = int(result[1])
results = sorted(results, key=lambda a:a[1])
print(results)