import urllib.request
import time

url = "https://beyondjobsuserpostsbackend.onrender.com/"

while True:
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            # Optionally, do something with the response like print(html) to see the content.
            print("Accessed the site successfully at:", time.strftime("%Y-%m-%d %H:%M:%S"))
    except urllib.error.URLError as e:
        print("Error accessing the site:", e)
    time.sleep(120)  # Wait for 120 seconds before accessing again
