from time import sleep
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys

import winsound

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
voll = "Die Terminkapazität ist vorübergehend ausgebucht. Wir sind darum bemüht, zeitnah weitere Termine für Ihr Anliegen freizugeben. Bitte versuchen Sie es zu einem späteren Zeitpunkt erneut."
keineTermineText = voll
while keineTermineText == voll:
    driver.get("https://stadt-karlsruhe.saas.smartcjm.com/m/stadt-karlsruhe/extern/calendar/?uid=54f4114e-d167-437b-a0d6-594406f7a0ac")
    assert "Smart" in driver.title

    add_button = driver.find_element_by_xpath("/html/body/div[2]/div[2]/form/div[3]/div[3]/div/div[1]/div[3]/div/div[2]/span[3]")
    add_button.click()

    weiter_button = driver.find_element_by_xpath("//*[@id='forward-service']")
    weiter_button.click()

    keineTermineText = "TERMIN FREI!!!"
    try:
        h3_element =driver.find_element_by_xpath("/html/body/div[2]/div[2]/form/div[3]/div[5]/div/div[1]/div/div/h3")
        keineTermineText = h3_element.text
    except:
        keineTermineText = "TERMIN FREI!!! (exc)"

    print(keineTermineText)
    winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
    #sleep(20)

