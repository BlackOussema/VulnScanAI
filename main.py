import argparse
from scanner import scan_url

def main():
    parser = argparse.ArgumentParser(description="VulnScanAI: Automated Vulnerability Scanner")
    parser.add_argument("url", help="URL to scan for vulnerabilities")
    args = parser.parse_args()

    print(f"[*] Scanning {args.url}...")
    results = scan_url(args.url)

    if results:
        print("[+] Vulnerabilities found:")
        for vuln_type, details in results.items():
            print(f"  - {vuln_type}:")
            for detail in details:
                print(f"    {detail}")
    else:
        print("[-] No vulnerabilities found.")

if __name__ == "__main__":
    main()
