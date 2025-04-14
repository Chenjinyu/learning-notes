from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# --- Your X (Twitter) credentials ---
USERNAME = "doublecheck0924"
PASSWORD = "4Better+Upgrade=JC"
TARGET_PROFILE = "whyyoutouzhele"  # 李老师不是你老师

# --- Setup Chrome ---
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# --- Step 1: Go to login page ---
driver.get("https://x.com/login")
time.sleep(3)

# --- Click "Sign up"  Button ---
try:
    signup_btn = driver.find_element(By.CSS_SELECTOR, '[data-testid="loginButton"]')
    signup_btn.click()
except NoSuchElementException:
    print("No 'Sign up' button found. Proceeding to login...")
    login_btn = driver.find_element(By.XPATH, '//a[@data-testid="loginButton"]')

login_btn.click()
time.sleep(3)


# --- Step 2: Enter username ---
usr_input = driver.find_element(By.XPATH, "//input[@name='text']")
usr_input.send_keys(USERNAME)
usr_input.send_keys(Keys.ENTER)
time.sleep(3)

# --- Step 3: Enter password ---
pwd_input = driver.find_element(By.XPATH, "//input[@name='password']")
pwd_input.send_keys(PASSWORD)
pwd_input.send_keys(Keys.ENTER)
time.sleep(5)

# --- Step 4: Go to target profile ---
driver.get(f"https://x.com/{TARGET_PROFILE}")
time.sleep(5)

# --- Step 5: Scroll to load tweets ---
for _ in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# --- Step 6: Parse tweets ---
soup = BeautifulSoup(driver.page_source, "lxml")
tweets = soup.find_all("article")

print(f"✅ Found {len(tweets)} tweets")

for i, tweet in enumerate(tweets[:5]):
    print(f"\n🧾 Tweet {i+1}:\n{text := tweet.get_text(separator=' ').strip()[:500]}")
    
driver.quit()
