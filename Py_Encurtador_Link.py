import pyshorteners

url = "https://github.com/RicardoHenriqueSantos"

s = pyshorteners.Shortener()

tiny_url = s.tinyurl.short(url)

print(f"URL Encurtada: {tiny_url}")
