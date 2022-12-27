from time import sleep
from datetime import datetime
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys

import winsound

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
voll = "Leider sind aktuell keine freien Termine verfügbar, bitte versuchen Sie es zu einem späteren Zeitpunkt erneut. Speichern Sie für eine neue Terminsuche Ihren derzeitigen Link nicht ab, sondern verwenden Sie unbedingt den Original-Link oder wählen sich über die Webseite der Stadt Karlsruhe www.karlsruhe.de erneut ein. Unsere Terminangebote umfassen jeweils die nächsten 60 Tage und werden täglich aktualisiert."
keineTermineText = voll
while keineTermineText == voll:
    # driver.get("https://stadt-karlsruhe.saas.smartcjm.com/m/stadt-karlsruhe/extern/calendar/?uid=54f4114e-d167-437b-a0d6-594406f7a0ac")
    driver.get("https://stadt-karlsruhe.saas.smartcjm.com/m/stadt-karlsruhe-standesamt/extern/calendar/?uid=6385cdf9-0825-4d94-bff2-d4f1315f05f1&wsid=7c282f62-38cf-4b08-9694-6004583cd7b7&lang=de")
    # assert "Smart" in driver.title

    add_button = driver.find_element("xpath","/html/body/div[2]/div[2]/form/div[3]/div[3]/div/div[1]/div/div/div[2]/span[3]")
    add_button.click()

    weiter_button = driver.find_element("xpath","//*[@id='forward-service']")
    weiter_button.click()

    second_weiter_button = driver.find_element("xpath","/html/body/div[2]/div[2]/form/div[3]/div[4]/div/div[2]/button[2]")
    second_weiter_button.click()

    keineTermineText = "TERMIN FREI!!!"
    
    try:
        h3_element =driver.find_element("xpath","/html/body/div[2]/div[2]/form/div[3]/div[5]/div/div[1]/div/div/h3")
        keineTermineText = h3_element.text
    except:
        keineTermineText = "TERMIN FREI!!! (exc)"

    print(str(datetime.now()))
    sleep(60)

print("Termine FREI!!!")
while True:
    winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
    winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
    winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
    sleep(10)