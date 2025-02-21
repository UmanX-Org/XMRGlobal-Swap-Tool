XMRGlobal Swap Tool

A privacy-first Monero swap tool designed exclusively for Tor networks. It interacts with the XMRGlobal.io API to fetch exchange rates, create swaps, check statuses, and manage transactions—all while ensuring full anonymity.
Features

    🕵️ Tor-Only – Built for Whonix & Tails, ensuring privacy by default.
    🔒 No KYC, No Logs – No tracking, no data collection, no compromises.
    ⚡ Monero-Centric – Anonymous, censorship-resistant swaps.
    📊 Real-Time Exchange Rates – Fetch up-to-date swap pricing.
    🛡️ Multiple .onion Addresses – Enhances security by rotating access points.
    🔑 PGP & Tor Security – End-to-end encrypted communication.

Installation

Clone the repository and run the tool:

git clone https://github.com/XMRGlobal/XMRGlobal-Swap-Tool.git
cd XMRGlobal-Swap-Tool
python3 XMRGlobal.py

Usage
On Whonix (Tor Native)

Simply run:

python3 XMRGlobal.py

On Tails (Tor Native)

python3 XMRGlobal.py

On Other Systems Using torsocks

torsocks python3 XMRGlobal.py

This ensures all network requests go through Tor, preserving anonymity.
How It Works

    Fetch Exchange Rates – Retrieve real-time rates for available swap pairs.
    Initiate a Swap – Enter details and create a swap privately.
    Send Payment – Transfer the required Monero (XMR) to complete the swap.
    Monitor Swap Status – Check the progress of your transaction.
    View Swap History – Securely access past transactions.
    Delete Swap History – Option to wipe all saved swaps with confirmation.

Security & Privacy

    Tor-Only – Operates exclusively through .onion services for privacy.
    No JavaScript – Fully functional in a minimal, secure environment.
    Anonymous Transactions – No user data is collected or stored.
    Privacy-Friendly CAPTCHA – Prevents automated abuse while preserving anonymity.

Error Handling & Improvements

    If an error occurs, XMRGlobal.py will return to the main menu instead of exiting.
    When a swap is in a waiting state, it will display full deposit details instead of incorrectly marking the amount as "sent."
    Swap History Management – Users can delete all saved swap records with a simple confirmation prompt (yes/no).

Verifying .onion Addresses

This repository includes .onion addresses signed with GPG for authenticity.

To verify:
https://xmrglobal.io/pgp 

or 

    Import the GPG key:

gpg --keyserver hkps://keys.openpgp.org --recv-key 4246552B722D7F51738032B22AD42655BD5227F5

Verify the signature:

    gpg --verify onions.txt.asc onions.txt

This message was signed at Monero block number [3352777] to ensure authenticity.
Disclaimer

This software is provided as-is with no warranty. Users are responsible for their own privacy and security. Always verify .onion addresses before use.

🔑 Privacy is freedom. Freedom is XMRGlobal. 🚀
