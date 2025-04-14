from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
from urllib.parse import urljoin

# --- Set up browser ---
options = Options()
options.add_argument("--start-maximized")
# options.add_argument("--headless=new")  # Optional for headless mode

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# --- Target tweet URL (fxtwitter) ---
url = "https://fxtwitter.com/whyyoutouzhele/status/1911468731433427144"
driver.get(url)
time.sleep(5)  # wait for full JS load

# --- Step 1: Find the main tweet block by data-testid ---
try:
    tweet_div = driver.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetText"]')

    # --- Step 2: Extract all span text inside ---
    spans = tweet_div.find_elements(By.TAG_NAME, "span")
    tweet_text = " ".join(span.text for span in spans if span.text.strip())
    print("📝 Tweet Text:", tweet_text)
except Exception as e:
    print("❌ Could not extract tweet text:", e)

# --- Step 3: Find any <img> under the tweet block or nearby ---
try:
    image_elements = driver.find_elements(By.CSS_SELECTOR, 'img')
    img_count = 0
    for img in image_elements:
        src = img.get_attribute("src")
        # Optional: only keep Twitter-hosted images
        if src and "twimg.com" in src:
            img_count += 1
            filename = f"tweet_image_{img_count}.jpg"
            img_data = requests.get(src).content
            with open(filename, "wb") as f:
                f.write(img_data)
            print(f"✅ Downloaded {filename}: {src}")
    if img_count == 0:
        print("⚠️ No Twitter-hosted images found.")
except Exception as e:
    print("❌ Failed to download images:", e)

# --- Keep browser open (optional for inspection) ---
input("🔍 Press Enter to close browser...")
driver.quit()
