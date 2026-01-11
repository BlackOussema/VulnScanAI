import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def make_request(url, method='GET', data=None, headers=None):
    try:
        if method.upper() == 'GET':
            response = requests.get(url, headers=headers, timeout=10)
        elif method.upper() == 'POST':
            response = requests.post(url, data=data, headers=headers, timeout=10)
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        return response
    except requests.exceptions.RequestException as e:
        print(f"[!] Request failed: {e}")
        return None

def scan_xss(url):
    vulnerabilities = []
    test_payloads = ["<script>alert('XSS')</script>", "<img src=x onerror=alert('XSS')>"]

    print(f"    [*] Checking for XSS on {url}")
    response = make_request(url)
    if response:
        soup = BeautifulSoup(response.text, 'html.parser')
        forms = soup.find_all('form')

        for form in forms:
            action = form.get('action')
            method = form.get('method', 'get').upper()
            target_url = urljoin(url, action) if action else url

            for payload in test_payloads:
                data = {}
                for input_tag in form.find_all('input'):
                    input_name = input_tag.get('name')
                    input_type = input_tag.get('type')
                    if input_name:
                        if input_type == 'text' or input_type == 'search':
                            data[input_name] = payload
                        else:
                            data[input_name] = input_tag.get('value', '')
                
                if method == 'POST':
                    test_response = make_request(target_url, method='POST', data=data)
                else:
                    test_response = make_request(target_url, method='GET', params=data)

                if test_response and payload in test_response.text:
                    vulnerabilities.append(f"Potential XSS found in form on {target_url} with payload: {payload}")
    return vulnerabilities

def scan_sql_injection(url):
    vulnerabilities = []
    test_payloads = ["' OR 1=1 --", "' OR '1'='1"] # Basic SQLi payloads

    print(f"    [*] Checking for SQL Injection on {url}")
    response = make_request(url)
    if response:
        soup = BeautifulSoup(response.text, 'html.parser')
        forms = soup.find_all('form')

        for form in forms:
            action = form.get('action')
            method = form.get('method', 'get').upper()
            target_url = urljoin(url, action) if action else url

            for payload in test_payloads:
                data = {}
                for input_tag in form.find_all('input'):
                    input_name = input_tag.get('name')
                    input_type = input_tag.get('type')
                    if input_name:
                        if input_type == 'text' or input_type == 'search':
                            data[input_name] = payload
                        else:
                            data[input_name] = input_tag.get('value', '')
                
                # For simplicity, we'll just check if the page content changes significantly or shows SQL errors
                # A real SQLi scanner would need a more robust detection mechanism
                if method == 'POST':
                    test_response = make_request(target_url, method='POST', data=data)
                else:
                    test_response = make_request(target_url, method='GET', params=data)

                if test_response and ("SQL syntax" in test_response.text or "mysql_fetch_array" in test_response.text):
                    vulnerabilities.append(f"Potential SQL Injection found in form on {target_url} with payload: {payload}")
    return vulnerabilities

def scan_url(url):
    all_vulnerabilities = {}

    xss_vulns = scan_xss(url)
    if xss_vulns:
        all_vulnerabilities['XSS'] = xss_vulns

    sql_vulns = scan_sql_injection(url)
    if sql_vulns:
        all_vulnerabilities['SQL Injection'] = sql_vulns

    return all_vulnerabilities
