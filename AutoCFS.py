import time
import urllib2
import csv
import ctypes
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

with open("test.csv", "rb") as data:
    reader = csv.DictReader(data, delimiter=',')
    Domain = []
    for row in reader:
        Domain.append(row['Domain'])

headers = "Domain,HTTP,HTTPS,CategoryID1,CategoryName1,CategoryID2,CategoryName2,CategoryID3,CategoryName3,CategoryID4,CategoryName4"

try:
    b = open('file1.csv')
    b.close()
except IOError:
    createfile = open("file1.csv", "w")
    createfile.write(headers)
    createfile.close()

driver = webdriver.Edge("C:\\Users\\brd65\\Downloads\\MicrosoftWebDriver.exe")

driver.set_page_load_timeout(30)
driver.get("http://cfssupport.sonicwall.com")
driver.implicitly_wait(20)
driver.find_element_by_id("url").send_keys("vk.com")
driver.find_element_by_name("kaptcha").click()
MessageBox = ctypes.windll.user32.MessageBoxA
MessageBox(None, 'Click OK after Completing Kaptcha', 'Attention', 0)
driver.find_element_by_name("button").click()

for k in driver.find_elements_by_xpath('/html/body/div/form/div[3]/div/table/tbody'):
    k2 = k.get_attribute('innerHTML')
    k3 = "".join(k2.split())
    k4 = k3.replace("&nbsp;", "").replace("<tr><td><b>", "").replace("</b><b>", "")
    k5 = k4.replace("</b><br></td></tr>", "").replace("Category", ":").replace(":", ",")
    update = open("file1.csv", "a")
    update.write("\n" + "vk.com" + k5 + ",\n")
time.sleep(3)

for a in Domain:
    driver.find_element_by_id("url").send_keys(Keys.CONTROL+"a")
    driver.find_element_by_id("url").send_keys(Keys.BACKSPACE)
    driver.find_element_by_id("url").send_keys(a)
    driver.find_element_by_name("button").click()
    time.sleep(1)
    for i in driver.find_elements_by_xpath('/html/body/div/form/div[3]/div/table/tbody'):
        i2 = i.get_attribute('innerHTML')
        i3 = "".join(i2.split())
        i4 = i3.replace("&nbsp;", "").replace("<tr><td><b>", "").replace("</b><b>", "")
        i5 = i4.replace("</b><br></td></tr>", "").replace("Category", ":").replace(":", ",")
        update = open("file1.csv", "a")
        update.write(a + i5 + ",\n")

driver.quit()
