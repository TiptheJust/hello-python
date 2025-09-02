import requests


def get_zen():
    r = requests.get("https://api.github.com/zen", timeout=10)
    return r.text


def shout(msg: str) -> str:
    return msg.strip().upper()


if __name__ == "__main__":
    text = get_zen()
    print(text)
    print(f"Chars: {len(text)}")
