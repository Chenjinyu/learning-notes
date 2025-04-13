from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# --- Setup browser ---
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("--headless")  # Optional if you want headless mode

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# --- Navigate to Twitter profile ---
url = "https://twitter.com/whyyoutouzhele"
driver.get(url)

# --- Wait for user to login manually if needed ---
print("🔐 Please login to Twitter in the browser. Press Enter here when done.")
input()

# --- Scroll to load tweets ---
for _ in range(3):  # Adjust to load more
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

# --- Parse the page ---
soup = BeautifulSoup(driver.page_source, "lxml")
tweets = soup.find_all("article")

print(f"✅ Found {len(tweets)} tweets")

for i, tweet in enumerate(tweets[:5], 1):  # Limit to first 5 tweets
    print(f"\n🧾 Tweet {i}")

    # --- Extract text ---
    content = tweet.get_text(separator=" ").strip()
    print("📜 Text:", content[:300], "...")  # Limit output length

    # --- Check for video ---
    video_tag = tweet.find("video")
    if video_tag:
        video_url = video_tag.get("src") or "[Video tag found but no src]"
        print("🎥 Video URL:", video_url)
    else:
        print("🎥 No video")

# --- Close browser ---
driver.quit()
