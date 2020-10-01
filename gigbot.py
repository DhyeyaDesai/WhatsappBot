from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from twilio.rest import Client
from time import sleep

twilio_sid = "AC39f1e47ce52ba8a7dd3d8338a6f0cf04"
auth_token = "5739009e86c871617ba74a581d3c345e"
EXECUTABLE_PATH = "C:\\Python38\\geckodriver.exe"

# options = Options()
# options.headless = True
# options.binary_location = "/app/.apt/usr/bin/google-chrome-stable"
# driver = webdriver.Chrome(chrome_options=options)

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path = EXECUTABLE_PATH)

with open("state.txt", "r") as f:
    state1, state2 = f.read().split(",")
    state1 = int(state1)
    state2 = int(state2)

for i in range(1,5):
    url = f"https://www.fiverr.com/search/gigs?query=web%20scraping&source=main_banner&search_in=everywhere&search-autocomplete-original-term=web%20scraping&page={i}&offset=-2"
    driver.get(url)
    if "dhyeya" in str(driver.page_source):
        break

for j in range(1,5):

    url2 = "https://www.fiverr.com/categories/programming-tech/data-analysis-services/data-mining-scraping?page={j}&offset=-1"
    driver.get(url2)
    if "dhyeya" in str(driver.page_source):
        break

print(i, j)

if (state1 != i or state2 != j):
    if state1 != i:
        msg = "Web scraping one went to " + i
        whatsapp_client = Client(twilio_sid, auth_token)
        contact = {"Dhyeya":"+917600665380"}

        for key, value in contact.items():
            msg_sent = whatsapp_client.messages.create(
                    body = msg,
                    from_= 'whatsapp:+14155238886',
                    to='whatsapp:' + value,
                )

    if state2 != j:
        msg = "Main category one went to " + j
        for key, value in contact.items():
            msg_sent = whatsapp_client.messages.create(
                    body = msg,
                    from_= 'whatsapp:+14155238886',
                    to='whatsapp:' + value,
                )