# XMRGlobal Swap Tool  

A **privacy-first** Monero swap tool designed exclusively for **Tor networks**. It interacts with the XMRGlobal.io API to fetch exchange rates, create swaps, check statuses, and manage transactions—ensuring full anonymity.  

## Features  
- **Tor-Only** – Built for **Whonix & Tails**, ensuring privacy by default.  
- **No KYC, No Logs** – No tracking, no data collection.  
- **Monero-Centric** – Anonymous, censorship-resistant swaps.  
- **Real-Time Exchange Rates** – Always up-to-date pricing.  
- **`.onion` Support** – Uses hidden services for added security.  

---

## Installation  

Clone the repository and install dependencies:  

```bash
git clone https://github.com/XMRGlobal/XMRGlobal-Swap-Tool.git
cd XMRGlobal-Swap-Tool
python3 client.py
```

---

## Usage  

### On **Whonix** (Tor native)  
Simply run:  
```bash
python3 client.py
```

### On **Tails** (Tor native)  
```bash
python3 client.py
```

### On **other systems** using `torsocks`  
```bash
torsocks python3 client.py
```

This setup ensures **all network requests go through Tor**, preserving your privacy.  

---

## How It Works  
1. **Fetch Exchange Rates** – Retrieve real-time rates for available swap pairs.  
2. **Create a Swap** – Enter the details and initiate a swap anonymously.  
3. **Confirm Payment** – Send the required Monero (XMR) to complete the swap.  
4. **Check Swap Status** – Monitor the progress of your swap until completion.  
5. **View Saved Swaps** – Keep track of your past transactions securely.  

---

## Command-Line Version (`cli_cmd.py`)  
For users who prefer a **fully command-line** experience, `cli_cmd.py` allows sending commands in one line. Example:  

```bash
python3 cli_cmd.py fetch_rates
python3 cli_cmd.py create_swap XMR BTC 0.5 mybtcaddress
python3 cli_cmd.py check_swap SWAP_ID
```

This version **does not** require CAPTCHA verification.  

---

## Security & Privacy  
- **Tor-Only** – Works exclusively through `.onion` addresses for maximum privacy.  
- **No JavaScript** – Fully functional in a secure, minimal environment.  
- **Self-Hosted Option** – Run your own instance for additional control.  
- **Encrypted Communication** – All transactions are secured with PGP and Tor.  

---

## Error Handling  
- If an error occurs, `cli.py` will **return to the main menu** instead of exiting.  
- If a swap is in a **waiting state**, it will **display full deposit details** instead of showing the amount as "sent."  
- Users can **delete all swap history** with confirmation (`yes/no`).  

---

## Privacy-Friendly CAPTCHA  
To prevent automated abuse, `cli.py` includes a simple **CAPTCHA challenge** before creating a swap.  
The command-line version (`cli_cmd.py`) **does not** require this verification.  

---

## Disclaimer  
This software is provided **as-is** with no warranty. Users are responsible for their own privacy and security. Always verify `.onion` addresses before use.  

---
**Privacy is freedom. Freedom is XMRGlobal.**

