# XMRGlobal Swap Tool  

A **privacy-first** Monero swap tool designed exclusively for **Tor networks**. It interacts with the XMRGlobal.io API to fetch exchange rates, create swaps, check statuses, and manage transactions—ensuring full anonymity.  

## Features  
- **Tor-Only** – Built for **Whonix & Tails**, ensuring privacy by default.  
- **No KYC, No Logs** – No tracking, no data collection.  
- **Monero-Centric** – Anonymous, censorship-resistant swaps.  
- **Real-Time Exchange Rates** – Always up-to-date pricing.  
- **Multiple `.onion` Addresses** – Enhances security by randomizing access points.  

---

## Installation  

Clone the repository and install dependencies:  

```bash
git clone https://github.com/XMRGlobal/XMRGlobal-Swap-Tool.git
cd XMRGlobal-Swap-Tool
python3 XMRGlobal.py
```

---

## Usage  

### On **Whonix** (Tor native)  
Simply run:  
```bash
python3 XMRGlobal.py
```

### On **Tails** (Tor native)  
```bash
python3 XMRGlobal.py
```

### On **other systems** using `torsocks`  
```bash
torsocks python3 XMRGlobal.py
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

## Security & Privacy  
- **Tor-Only** – Works exclusively through multiple `.onion` addresses for maximum privacy and security.  
- **No JavaScript** – Fully functional in a secure, minimal environment.  
- **Hosted on XMRGlobal `.onion` Services** – No self-hosting required.  
- **Encrypted Communication** – All transactions are secured with PGP and Tor.  

---

## Error Handling  
- If an error occurs, `XMRGlobal.py` will **return to the main menu** instead of exiting.  
- If a swap is in a **waiting state**, it will **display full deposit details** instead of showing the amount as "sent."  
- Users can **delete all swap history** with confirmation (`yes/no`).  

---

## Privacy-Friendly CAPTCHA  
To prevent automated abuse, `XMRGlobal.py` includes a simple **CAPTCHA challenge** before creating a swap.  

---

## Disclaimer  
This software is provided **as-is** with no warranty. Users are responsible for their own privacy and security. Always verify `.onion` addresses before use.  

---
**Privacy is freedom. Freedom is XMRGlobal.**

