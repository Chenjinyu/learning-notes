from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urljoin
import requests
import subprocess
import time

# === CONFIG ===
tweet_url = "https://x.com/whyyoutouzhele/status/1911486790827122714"
tweet_id = tweet_url.split("/")[-1]

# === SETUP SELENIUM ===
options = Options()
options.add_argument("--start-maximized")
# options.add_argument("--headless=new")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get(tweet_url)
time.sleep(5)

# === Step 1: Find article[data-testid="tweet"] ===
articles = driver.find_elements(By.CSS_SELECTOR, 'article[data-testid="tweet"]')
print(f"Found {len(articles)} article(s) with data-testid='tweet'")

for i, article in enumerate(articles, 1):
    try:
        print(f"\n🔍 Processing tweet block {i}")

        # Step 2: Drill down the nested divs
        outer_div = article.find_element(By.XPATH, './div')
        nested_div = outer_div.find_element(By.XPATH, './div')
        target_divs = nested_div.find_elements(By.XPATH, './div')

        if len(target_divs) < 3:
            print("⚠️ Tweet structure does not match expected layout.")
            continue

        content_div = target_divs[2]  # The 3rd div

        # === Extract text ===
        spans = content_div.find_elements(By.TAG_NAME, "span")
        tweet_text = " ".join(span.text.strip() for span in spans if span.text.strip())
        print("📝 Tweet text:", tweet_text)

        # === Extract images ===
        images = content_div.find_elements(By.TAG_NAME, "img")
        img_count = 0
        for img in images:
            src = img.get_attribute("src")
            if "twimg.com" in src and "profile_images" not in src:
                img_count += 1
                filename = f"{tweet_id}_block{i}_image{img_count}.jpg"
                img_data = requests.get(src).content
                with open(filename, "wb") as f:
                    f.write(img_data)
                print(f"🖼️ Downloaded image: {filename}")

    except Exception as e:
        print(f"❌ Error while processing tweet {i}:", e)

# === Step 3: Use yt-dlp to download video(s) ===
print("\n🎥 Using yt-dlp to download video(s) (if any)...")
output_filename = "tweet_video_with_audio.mp4"

subprocess.run([
    "yt-dlp",
    "-f", "bestvideo+bestaudio",
    "--merge-output-format", "mp4",
    "-o", output_filename,
    tweet_url
]) 

driver.quit()
