import time
import requests

from selene import browser, query
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": r"D:\py_projects\lesson7_qaa\tmp",
    "download.prompt_for_download": False
}
options.add_experimental_option("prefs", prefs)

driver =webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)
browser.config.driver = driver

browser.open("https://github.com/qa-guru/qa_guru_python_9_7_files/blob/master/tmp/Python%20Testing%20with%20Pytest%20(Brian%20Okken).pdf")
browser.element("[data-testid='download-raw-button'").click()
time.sleep(5)

browser.open("https://github.com/qa-guru/qa_guru_python_9_7_files/blob/master/tmp/file_example_XLSX_50.xlsx")
browser.element("[data-testid='download-raw-button'").click()
time.sleep(5)

browser.open("https://github.com/alicceea/qa_guru-NewProject/blob/main/username.csv")
browser.element("[data-testid='download-raw-button'").click()
time.sleep(5)

browser.open("https://support.staffbase.com/hc/en-us/articles/360007108391-CSV-File-Examples")
download_url = browser.element("[id='csv-example-username']").get(query.attribute("href"))
content = requests.get(url=download_url).content

with open("tmp/csv_f.csv", 'wb') as file:
    file.write(content)

