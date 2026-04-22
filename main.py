import requests
sites = {
    "GitHub": "https://github.com/{}",
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://www.instagram.com/{}/",
    "Reddit": "https://www.reddit.com/user/{}"
}

def check_username(username):
    print(f"\nChecking username: {username}\n")
    
    found_sites = []

    for site, url in sites.items():
        full_url = url.format(username)
        
        try:
            response = requests.get(full_url, timeout=5)
            
            if response.status_code == 200:
                text = response.text.lower()

                if any(keyword in text for keyword in [
                    "sorry",
                    "doesn’t exist",
                    "doesn't exist",
                    "not found",
                    "page not found"
                ]):
                    print(f"[-] Not found on {site}")
                else:
                    print(f"[+] Found on {site}: {full_url}")
                    found_sites.append(site)
            else:
                print(f"[-] Not found on {site}")
            
        except requests.exceptions.RequestException:
            print(f"[!] Error connecting to {site}")
    
    print("\nSummary:")
    print(f"Total platforms checked: {len(sites)}")
    print(f"Profiles found: {len(found_sites)}")

    if found_sites:
        print("Found on:", ", ".join(found_sites))

    from colorama import Fore, init
    init()

    print(Fore.GREEN + "[+] Found on:", ", ".join(found_sites))
    print(Fore.RED + "[-] Not found")

if __name__ == "__main__":
    username = input("Enter username: ")
    check_username(username)

