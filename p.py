import pyshorteners


def create_short_url(url):
    shortener = pyshorteners.Shortener()
    return shortener.tinyurl.short(url)

if __name__ == "__main__":
    long_url = input("Enter a URL to shorten: ")
    short_url = create_short_url(long_url)
    print(f"Here is your shortened URL: {short_url}")