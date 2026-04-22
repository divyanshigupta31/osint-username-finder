# osint-username-finder
A small python based tool to detect username presence across multiple platforms that utilises HTTP request handling for real time verification. This tool uses heuristic-based validation and may produce occasional false positives.

---

## Overview

This tool automates the process of identifying whether a username exists on various platforms by combining status code checks with content-based analysis. It is designed as a lightweight and extensible utility for basic OSINT tasks.

---

## Features

* Checks username availability across multiple platforms
* Uses HTTP requests with custom headers to improve reliability
* Implements content-based validation to reduce false positives
* Provides a structured summary of results
* Modular design for adding additional platforms

---

## Technologies Used

* Python
* requests
* colorama

---

## Supported Platforms

* GitHub
* Reddit
* Instagram
* Twitter (limited detection due to dynamic content)

---

## Limitations

* Some platforms return HTTP 200 responses even when a user does not exist
* Platforms such as Twitter rely on dynamic content, making detection via basic HTTP requests unreliable
* The tool uses heuristic-based validation and may produce occasional false positives

---

## Methodology

1. Accepts a username as input
2. Constructs platform-specific profile URLs
3. Sends HTTP requests with appropriate headers
4. Validates responses using:

   * HTTP status codes
   * Keyword-based content checks
5. Aggregates and displays results

---

## Installation and Usage

### 1. Clone the repository

```bash
git clone https://github.com/divyanshigupta31/osint-username-finder.git
cd osint-username-finder
```

### 2. Install dependencies

```bash
pip install requests colorama
```

### 3. Run the program

```bash
python main.py
```

---

## Example Output

```
Checking username: example

[+] Found on GitHub: https://github.com/example
[-] Not found on Reddit
[~] Cannot reliably verify Twitter

Summary:
Total platforms checked: 4
Profiles found: 1
```

---

## Future Work

* Extend support to additional platforms
* Improve detection accuracy using official APIs where available
* Add export functionality (JSON/CSV)
* Implement a command-line interface with arguments
* Integrate into a broader OSINT toolkit

---

## License

This project is intended for educational purposes.

---

## Author

Developed as part of an introductory exploration into cybersecurity and OSINT techniques.


