from urllib.request import urlopen

def get_html():
    print("Downloading an image of a puppy")
    response = urlopen("http://httpbin.org/html")
    return response.read().decode('utf-8')

if __name__ == "__main__":
    html = get_html()
    print(html)