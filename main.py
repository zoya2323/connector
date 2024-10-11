import requests

def check_website(url):
    try:
        response = requests.get(url)
        # If the response status code is 200, the site is reachable
        if response.status_code == 200:
            print(f"The website {url} is reachable.")
        else:
            print(f"The website {url} returned status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to {url}: {e}")

def main():
    url = input("Enter the URL of the website to check (e.g., https://www.example.com): ")
    check_website(url)

if __name__ == "__main__":
    main()

