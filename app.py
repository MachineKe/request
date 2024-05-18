import urllib.request
import time

url = "https://portal.sasakonnect.net/?interface_mode=true&pagetype=remote&wired_auth=true&interface=vlan2004&staIp=10.4.13.201&staMac=30:D1:6B:E4:A8:0B&url=http:%2F%2Fwww.msftconnecttest.com%2Fredirect"

while True:
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            # Optionally, do something with the response like print(html) to see the content.
            print("Accessed the site successfully at:", time.strftime("%Y-%m-%d %H:%M:%S"))
    except urllib.error.URLError as e:
        print("Error accessing the site:", e)
    time.sleep(2)  # Wait for 2 seconds before accessing again