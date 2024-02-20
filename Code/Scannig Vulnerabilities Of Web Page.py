import requests
from bs4 import BeautifulSoup
import time

class WebSecurityScanner:
    def __init__(self, target_url):
        self.target_url = target_url
        self.vulnerabilities = []

    def scan_sql_injection(self):
        #SQL injection is used to manipulate data in the backend (SQL injection is a code injection technique that might destroy your database).
        # Implement SQL injection detection logic here
        # Example: Check for SQL errors in response content
        payload = "' OR 1=1 --"
        url = f"{self.target_url}?param={payload}"
        response = requests.get(url)

        if "error in your SQL syntax" in response.text:
            self.vulnerabilities.append("SQL Injection detected")

    def scan_xss(self):
        #The Cross Site Scripting (XSS) scan checks how your service handles potentially harmful injections into web pages
        # Implement XSS detection logic here
        # Example: Check for script tags in response content
        payload = "<script>alert('XSS')</script>"
        url = f"{self.target_url}?param={payload}"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")
        if soup.find("script"):
            self.vulnerabilities.append("XSS detected")

    def scan_csrf(self):
        #Cross-site Request Forgery(The attacker forces a non-authenticated user to log in to an account the attacker controls. If the victim does not realize this, they may add personal data—such as credit card information—to the account) 
        # Implement CSRF detection logic here
        # Example: Check for anti-CSRF token in HTML form
        response = requests.get(self.target_url)
        soup = BeautifulSoup(response.text, "html.parser")
        csrf_token = soup.find("input", {"name": "csrf_token"})

        if csrf_token is None:
            self.vulnerabilities.append("CSRF detected")

    def run_scan(self):
        print("Scanning vulnerabilities. Please wait.")
        for _ in range(15):  # Simulating a 5-second scan with a simple animation
            time.sleep(1)
            print(".", end="", flush=True)

        self.scan_sql_injection()
        self.scan_xss()
        self.scan_csrf()

        print("\nScan complete.")
        if not self.vulnerabilities:
            print("No vulnerabilities detected.")
        else:
            print("Vulnerabilities detected:")
            for vulnerability in self.vulnerabilities:
                print(f"- {vulnerability}")


if __name__ == "__main__":
    target_url = input("Enter the target web page URL: ")
    scanner = WebSecurityScanner(target_url)
    scanner.run_scan()
