import requests
import json

apk_urls = []

apps = json.loads(requests.get("https://apps.grapheneos.org/metadata.1.0.sjson").text.split("\n")[0])

for package in apps["packages"]:
  version_code = tuple(apps["packages"][package]["variants"].keys())[0]
  apk_filename = apps["packages"][package]["variants"][version_code]["apks"][0]
  apk_urls.append(f"https://apps.grapheneos.org/packages/{package}/{version_code}/{apk_filename}")

session = requests.Session()
for apk_url in apk_urls:
  print(f"Downloading {apk_url}")
  filename = apk_url.split("/")
  filename = f"{filename[-3]}_{filename[-2]}.apk"
  with open(filename, "wb") as file:
    file.write(session.get(apk_url).content)
