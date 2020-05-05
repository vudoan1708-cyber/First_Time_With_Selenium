# import selenium, and webdriver
from selenium import webdriver
# import webdriverwait for wait time
from selenium.webdriver.support.ui import WebDriverWait
# import keys for any keyboard triggering
from selenium.webdriver.common.keys import Keys
# import time for   sleep
import time
# import speech recognition
import speech_recognition as sr
# import tkinter
import tkinter as tk

# all the languages
Languages = ['ta', 'mn', 'tl', 'cy', 'kn', 'sn', 'ko', 'ar', 'km', 'bs', 'la', 'cs', 'rw', 'ne', 'sq', 'sw', 'sm', 'mi', 'co', 'hy', 'el', 'st', 'tk', 'ha', 'it', 'sd', 'af', 'sr', 'es', 'bn', 'th', 'is', 'ka', 'ht', 'so', 'ga', 'fr', 'hi', 'ig', 'pt', 'tg', 'ro', 'pl', 'vi', 'en', 'lv', 'mk', 'hr', 'mt', 'te', 'lt', 'ru', 'id', 'iw', 'gl', 'sv', 'ms', 'sl', 'zh-TW', 'ug', 'zh', 'mr', 'fi', 'si', 'xh', 'jw', 'fy', 'pa', 'ku', 'ps', 'hu', 'ml', 'no', 'gd', 'eu', 'or', 'ceb', 'fa', 'bg', 'lb', 'kk', 'et', 'gu', 'lo', 'yi', 'su', 'da', 'am', 'ur', 'hmn', 'de', 'tr', 'tt', 'eo', 'yo', 'sk', 'zu', 'nl', 'be', 'ky', 'haw', 'uk', 'ca', 'zh-CN', 'my', 'uz', 'mg', 'ny', 'ja', 'az', 'ko']

# global dest
# dest = 'en'

r = sr.Recognizer()
r_input = sr.Recognizer()

global search
search = False

def sourceLang():
    # SETUP SPEECH RECOGNITION
    with sr.Microphone() as source:
        audio = r.listen(source)
        try: 
            global dest
            dest = r.recognize_google(audio)
            dest = dest.lower()
            if 'viet' in dest:
                dest = 'vi'
                print(dest)
            elif 'kor' in dest:
                dest = 'ko'
                print(dest)
        except:
            print('Sorry, could not recognise your voice')

def speakLang():
    global keywords
    keywords = ''
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            keywords = r.recognize_google(audio)
            keywords.lower()
            print(keywords)

            global search
            search = True

            if search == True:
                # set the path to the chrom driver executables file
                # link to download: https://sites.google.com/a/chromium.org/chromedriver/downloads
                PATH = 'C:\Program Files (x86)\chromedriver.exe'

                # opts = ChromeOptions()
                # opts.add_experimental_option("excludeSwitches", ['enable-automation'])
                # choose the web browser type to be driven
                driver = webdriver.Chrome(PATH)

                # specify the url to be driven
                driver.get(f'https://translate.google.com/#view=home&op=translate&sl=auto&tl={dest}')

                # set input field
                inputField = 'source'

                # set output field
                outputField = "//div[@class='result tlid-copy-target']"

                # find input field
                input = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(inputField))

                # input = driver.find_element_by_xpath("//textarea[@id='source']")

                # input some keywords into the field
                input.send_keys(keywords)

                # wait for 5 secs
                time.sleep(5)

                # before finding out the output HTML element 
                # as it's hidden before the input field is filled with text
                output = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(outputField))

                print(output.text)
                time.sleep(5)
        except:
            print('Sorry, could not recognise your voice')

    

# tkinter
root = tk.Tk()

canvas = tk.Canvas(root, width = 200, height = 200, bg = 'black')
canvas.pack()

# buttons
sourceBtn = tk.Button(root, text='Speak The Destination Language You Want To Translate To', 
                    padx = 20, pady = 10, fg = 'white', bg = 'black', command = sourceLang)
sourceBtn.pack()

speakBtn = tk.Button(root, text='Speak to Translate',
                    padx = 20, pady = 10, fg = 'white', bg = 'black', command = speakLang)
speakBtn.pack()
root.mainloop()