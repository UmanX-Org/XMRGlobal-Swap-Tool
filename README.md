
# **XMRGlobal Swap Tool**  

A **privacy-first** Monero swap tool designed exclusively for **Tor networks**. It interacts with the **XMRGlobal.io** API to fetch exchange rates, create swaps, check statuses, and manage transactions—all while ensuring full anonymity.  

## **Features**  
- 🕵️ **Tor-Only** – Built for **Whonix & Tails**, ensuring privacy by default.  
- 🔒 **No KYC, No Logs** – No tracking, no data collection, no compromises.  
- ⚡ **Monero-Centric** – Anonymous, censorship-resistant swaps.  
- 📊 **Real-Time Exchange Rates** – Fetch up-to-date swap pricing.  
- 🛡️ **Multiple `.onion` Addresses** – Enhances security by rotating access points.  
- 🔑 **PGP & Tor Security** – End-to-end encrypted communication.  

---

## **Installation**  

Clone the repository and run the tool:  

```bash
git clone https://github.com/XMRGlobal/XMRGlobal-Swap-Tool.git
cd XMRGlobal-Swap-Tool
python3 XMRGlobal.py
```

---

## **Usage**  

https://youtu.be/7clOOMlZ0uE   Video - Tutorial 

### **On Whonix (Tor Native)**  
Simply run:  
```bash
python3 XMRGlobal.py
```

### **On Tails (Tor Native)**  
```bash
python3 XMRGlobal.py
```

### **On Other Systems Using `torsocks`**  
```bash
torsocks python3 XMRGlobal.py
```

### **🔹 Steps to Install & Run in Termux (Android, GrapheneOS, CalyxOS) **
1️⃣ **Install Python in Termux** (if not installed)  
```sh
pkg update && pkg upgrade
pkg install python
```

2️⃣ **Install Required Python Modules**  
```sh
pip install requests
```

3️⃣ **Run the Swap Tool with Orbot’s SOCKS5 Proxy**  
Start **Orbot** → Enable **SOCKS5 Proxy** (127.0.0.1:9050)  

```sh
export ALL_PROXY=socks5h://127.0.0.1:9050
python3 XMRGlobal.py
```

### **🛠 Running XMRGlobal Swap Tool on macOS with Tor**  

Since macOS supports Python natively, you can run the **XMRGlobal Swap Tool** using **Tor's SOCKS5 proxy**.

---

## **🔹 Step 1: Install Python (If Not Installed)**  
Check if Python is installed:  
```sh
python3 --version
```
If not, install it using Homebrew:  
```sh
brew install python
```

---

## **🔹 Step 2: Install Required Python Dependencies**  
```sh
pip3 install requests
```

---

## **🔹 Step 3: Install & Run Tor**  
1️⃣ Install **Tor** using Homebrew:  
```sh
brew install tor
```

2️⃣ Start Tor in a new terminal window:  
```sh
tor
```
💡 **Tor runs a SOCKS5 proxy at `127.0.0.1:9050`**  

---

## **🔹 Step 4: Set Up SOCKS5 Proxy & Run the Swap Tool**  
1️⃣ Open a new terminal window and export the proxy:  
```sh
export ALL_PROXY=socks5h://127.0.0.1:9050
```

2️⃣ Run the swap tool through Tor:  
```sh
python3 XMRGlobal.py
```



## **How It Works**  
1. **Fetch Exchange Rates** – Retrieve real-time rates for available swap pairs.  
2. **Initiate a Swap** – Enter details and create a swap **privately**.  
3. **Send Payment** – Transfer the required Monero (XMR) to complete the swap.  
4. **Monitor Swap Status** – Check the progress of your transaction.  
5. **View Swap History** – Securely access past transactions.  
6. **Delete Swap History** – Option to wipe all saved swaps with confirmation.  

---

## **Security & Privacy**  
- **Tor-Only** – Operates exclusively through `.onion` services for privacy.  
- **No JavaScript** – Fully functional in a minimal, secure environment.  
- **Anonymous Transactions** – No user data is collected or stored.  
- **Privacy-Friendly CAPTCHA** – Prevents automated abuse while preserving anonymity.  

---


## **Verifying `.onion` Addresses**  
This repository includes `.onion` addresses signed with **GPG** for authenticity.  

To verify:  

1. **Import the GPG key**:  

from https://XMRglobal.io/pgp

from https://github.com/XMRGlobal/XMRGlobal-Swap-Tool/blob/main/XMRGlobal%20PGP%20key


   ```bash
   gpg --keyserver hkps://keys.openpgp.org --recv-key 4246552B722D7F51738032B22AD42655BD5227F5
   ```  
   
2. **Verify the signature**:  
   ```bash
   gpg --verify onions.txt.asc onions.txt
   ```

This message was signed at **Monero block number [3352777]** to ensure authenticity.  

---

## **Disclaimer**  
This software is provided **as-is** with no warranty. Users are responsible for their own privacy and security. Always verify `.onion` addresses before use.  

---

**🔑 Privacy is freedom. Freedom is XMRGlobal.** 🚀  

---
