import requests
r = requests.get("https://api.github.com/zen", timeout=10)
print(r.text)
print(f"Chars: {len(r.text)}")