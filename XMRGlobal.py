import requests
import json
import os
import random
from datetime import datetime

import random
import string

def generate_captcha():
    """Generates a simple CAPTCHA challenge."""
    if random.choice([True, False]):
        # Math CAPTCHA
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        solution = str(num1 + num2)
        challenge = f"{num1} + {num2} = "
    else:
        # Random string CAPTCHA
        solution = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        challenge = f"Enter the following: {solution}"
    return challenge, solution

def verify_captcha():
    """Verifies user input against the CAPTCHA challenge."""
    challenge, solution = generate_captcha()
    user_input = input(f"🔐 CAPTCHA: {challenge} ").strip()
    if user_input != solution:
        print("❌ Incorrect CAPTCHA! Swap canceled.")
        return False
    return True


# List of Tor .onion addresses for redundancy
ONION_ADDRESSES = [
    "cqy2caejjpclixkumyvb24agvyth67znr7koee5264i6ucjxno3rcaid.onion",
    "5a2k6b3ov6w2ryl5th3jnsrujqj4x4micvxz75pbeama47fzonnwwcyd.onion",
    "2syzexutltau2n455oryarrervet36fzj2sksxbkpmg5anzustojsvid.onion",
    "5arhxqhg6sbken6qfnlnb4ozw3m7kzhjafqhzt5fcgdpy5s7qcjfciad.onion",
    "xdbokl4gkghiruj66q2vdlamx76rdza6mojv4iizdoc7tvwut2ssf5id.onion",
    "n4qqn4b4j5xnzzarikgtujm3atg3l5ld7snfvrwejgwmpb3k3zqxduqd.onion",
    "lfxzeipdedi5ybxy7azm3rh5lzwberpsugevdcddg7x2uqivjffy3zad.onion",
    "qiwntfdosxsoeuty2jqzcazhiwwvyrv77hejxf5fakvochnkge2e6eid.onion",
    "wdqbafeegcfwgbs46xcvbcl3o2k336bp7s3sacp33sfxzp5kv4uprjad.onion"

]

# API Configuration
SWAP_LOG_DIR = "/tmp/swap-id"
os.makedirs(SWAP_LOG_DIR, exist_ok=True)

# Select a working .onion address by checking `/ping`
def get_api_url():
    """Select a working .onion address by checking `/ping` and return the URL and onion address."""
    for onion in random.sample(ONION_ADDRESSES, len(ONION_ADDRESSES)):
        api_url = f"http://{onion}:8000"
        try:
            response = requests.get(f"{api_url}/ping", timeout=10)
            if response.status_code == 200:
                print(f"✅ Using onion: {onion}")
                return api_url, onion
        except requests.RequestException:
            continue
    print("❌ No available onions. Exiting.")
    exit(1)

API_URL, SELECTED_ONION = get_api_url()

def print_header():
    """Prints a user-friendly header with major XMR pairs."""
    major_pairs = [
        ("BTC", "XMR"),
        ("ETH", "XMR"),
        ("LTC", "XMR"),
        ("XMR", "DOGE"),
        ("XMR", "ADA"),
        ("XMR", "BCH"),
        ("XMR", "SOL"),
        ("XMR", "DOT"),
        ("XMR", "TRX"),
        ("XMR", "XLM"),
        ("XMR", "DOGE"),
    ]
    
    print("\n====================================")
    print("🔹 XMRGlobal Swap CLI 🔹")
    print(f"🌍 Connected via: {SELECTED_ONION}")
    print("====================================\n")
    
    print("📊 Major XMR Pairs:")
    
    # Split the pairs into chunks of 5 for better readability
    for i in range(0, len(major_pairs), 5):
        row = major_pairs[i:i+5]
        print("   " + "   ".join([f"{pair[0]} → {pair[1]}" for pair in row]))

    print("====================================\n")

def save_swap(transaction_id, swap_data):
    """Save swap details to a file."""
    swap_file = os.path.join(SWAP_LOG_DIR, f"{transaction_id}.json")
    with open(swap_file, "w") as file:
        json.dump(swap_data, file, indent=4)
    print(f"\n✅ Your Swap ID is: {transaction_id}")
    print(f"📂 Your swap has been saved in: {swap_file}")

def get_input(prompt):
    """Helper function to get user input."""
    return input(prompt).strip()

def delete_all_swap_history():
    """Deletes all swap history after user confirmation."""
    print_header()
    swaps = os.listdir(SWAP_LOG_DIR)
    
    if not swaps:
        print("❌ No swap history found.")
        return
    
    confirm = get_input("⚠️ Are you sure you want to delete all swap history? (yes/no): ").lower()
    if confirm == "yes":
        for file in swaps:
            os.remove(os.path.join(SWAP_LOG_DIR, file))
        print("✅ All swap history has been deleted.")
    else:
        print("❌ Swap history deletion canceled.")




def check_swap_status():
    """Check the status of an ongoing swap and display estimated receiving amount if applicable."""
    print_header()
    transaction_id = get_input("Enter your Transaction ID: ")

    swap_file = os.path.join(SWAP_LOG_DIR, f"{transaction_id}.json")
    if not os.path.exists(swap_file):
        print("❌ Swap ID not found.")
        return

    try:
        with open(swap_file, "r") as file:
            data = json.load(file)

        created_at = data.get("created_at", "Unknown time")
        status = data["status"].upper()
        deposit = data.get("deposit", {})
        withdrawal = data.get("withdrawal", {})
        estimated_amount = withdrawal.get("expected_amount", "Unknown")

        print("\n📊 **Swap Status**")
        print(f"🔹 Transaction ID: {transaction_id}")
        print(f"📅 Created At: {created_at}")
        print(f"🔹 Status: {status}")

        print(f"\n🔹 **Swap Pair:** {deposit.get('symbol', '').upper()} → {withdrawal.get('symbol', '').upper()}")

        if status == "WAITING":
            print("\n⚠️ **Action Required!**")
            print(f"   - Please send {deposit.get('expected_amount', 'N/A')} {deposit.get('symbol', '').upper()} to:")
            print(f"   - Address: {deposit.get('address', 'N/A')}")
            if deposit.get("address_explorer_url"):
                print(f"   - Explorer: {deposit['address_explorer_url']}")
            print("\n💡 Your swap will proceed once the deposit is received.")
            print(f"💱 Estimated Amount to Receive: {estimated_amount} {withdrawal.get('symbol', '').upper()}")

        elif status in ["CONFIRMING", "EXCHANGING", "SENDING"]:
            print("\n⏳ **Swap is in progress...**")
            print("   - Your deposit has been received and is being processed.")
            print(f"💱 Estimated Amount to Receive: {estimated_amount} {withdrawal.get('symbol', '').upper()}")

        elif status == "VERIFYING":
            print("\n🔍 **Swap is being verified...**")

        elif status == "FINISHED":
            print("\n✅ **Swap Completed Successfully!**")
            print(f"   - Amount Received: {withdrawal.get('amount', 'N/A')} {withdrawal.get('symbol', '').upper()}")
            print(f"   - Received At: {withdrawal.get('address', 'N/A')}")
            if withdrawal.get("address_explorer_url"):
                print(f"   - Explorer: {withdrawal['address_explorer_url']}")

        elif status == "FAILED":
            print("\n❌ **Swap Failed.**")
            print("   - Please check with support if needed.")

        elif status == "REFUNDED":
            print("\n💰 **Swap Refunded.**")
            print(f"   - Your deposit has been refunded to: {data.get('refund_address', 'N/A')}")

        elif status == "EXPIRED":
            print("\n⏳ **Swap Expired.**")
            print("   - Your deposit was not received in time.")

    except (json.JSONDecodeError, FileNotFoundError):
        print("❌ Error reading swap data.")

def view_my_swaps():
    """Lists all saved swaps with their date and time from 'created_at' field."""
    print_header()
    swaps = os.listdir(SWAP_LOG_DIR)
    
    if not swaps:
        print("❌ No saved swaps found.")
        return

    print("📂 **Your Saved Swaps:**\n")
    for swap in swaps:
        swap_file = os.path.join(SWAP_LOG_DIR, swap)
        try:
            with open(swap_file, "r") as file:
                swap_data = json.load(file)
                created_at = swap_data.get("created_at", "Unknown time")
                swap_id = swap.replace('.json', '')
                print(f"🔹 Swap ID: {swap_id} | 📅 Date: {created_at}")
        except json.JSONDecodeError:
            print(f"⚠️ Error reading swap file: {swap}")

def get_rate():
    """Fetch exchange rate and check min/max limits before proceeding."""
    print_header()
    from_coin = get_input("Enter the coin you want to swap from: ").lower()
    to_coin = get_input("Enter the coin you want to swap to (must be XMR or from XMR): ").lower()

    if from_coin != "xmr" and to_coin != "xmr":
        print("❌ One of the currencies must be XMR!")
        return

    amount = float(get_input(f"Enter the amount of {from_coin.upper()} to swap: "))

    print(f"📡 Fetching estimated amount for {amount} {from_coin.upper()} → {to_coin.upper()}...\n")
    url = f"{API_URL}/rate/{from_coin}/{to_coin}/{amount}"

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        data = response.json()

        min_amount = data.get("min_amount", None)
        max_amount = data.get("max_amount", None)
        estimated_amount = data.get("rate_with_commission", None)

        # ✅ **Unified messaging for minimum required swap amount**
        required_minimum = min_amount if estimated_amount is not None else amount + min_amount if min_amount else "Unknown"
        print(f"🔹 The **minimum required swap amount** is: **{required_minimum} {from_coin.upper()}**")

        if max_amount:
            print(f"🔹 Max Amount Allowed: {max_amount} {from_coin.upper()}")

        if min_amount and amount < min_amount:
            print(f"⚠️ The amount you entered ({amount} {from_coin.upper()}) is **below the minimum required.**")
            print(f"🔹 You must send at least: **{required_minimum} {from_coin.upper()}**")
            print("Returning to main menu...\n")
            return

        # ❌ **If estimated amount is missing, warn user**
        if estimated_amount is None:
            print(f"⚠️ **Error:** Estimated amount is not available.")
            return

        print(f"💱 Estimated Amount to Receive: {estimated_amount} {to_coin.upper()}")
        proceed = get_input("Do you want to proceed with this swap? (yes/no): ").lower()
        if proceed == "yes":
            initiate_swap(from_coin, to_coin, amount)

    except requests.RequestException as e:
        print(f"❌ Error fetching rate: {e}")





def initiate_swap(from_coin, to_coin, amount):
    """Initiates a swap process with CAPTCHA verification."""
    print_header()

    # Verify CAPTCHA before proceeding
    if not verify_captcha():
        return

    receiving_address = get_input(f"Enter your receiving address for {to_coin.upper()}: ")
    refund_address = get_input(f"Enter your refund address for {from_coin.upper()} (in case of failure): ")

    print(f"\n📡 Fetching estimated amount for {amount} {from_coin.upper()} → {to_coin.upper()}...\n")
    rate_url = f"{API_URL}/rate/{from_coin}/{to_coin}/{amount}"

    try:
        rate_response = requests.get(rate_url, timeout=15)
        rate_response.raise_for_status()
        rate_data = rate_response.json()
        estimated_amount = rate_data.get('rate_with_commission', 'Unknown')

        print(f"\n🔹 Swap Details:")
        print(f"   - Sending Amount: {amount} {from_coin.upper()}")
        print(f"   - Receiving Amount: {estimated_amount} {to_coin.upper()}")
        print(f"   - Receiving: {to_coin.upper()} at {receiving_address}")
        print(f"   - Refund Address: {refund_address}")

        confirm_swap = get_input("✅ Confirm swap? (yes/no): ").lower()
        if confirm_swap != "yes":
            print("❌ Swap canceled.")
            return

        print(f"📡 Initiating swap: {amount} {from_coin.upper()} → {to_coin.upper()}...\n")
        swap_url = f"{API_URL}/swap"
        payload = {
            "from_coin": from_coin,
            "to_coin": to_coin,
            "amount": amount,
            "receiving_address": receiving_address,
            "refund_address": refund_address
        }

        swap_response = requests.post(swap_url, json=payload, timeout=15)
        swap_response.raise_for_status()
        swap_data = swap_response.json()

        print("\n✅ **Swap Created Successfully!**")
        print(f"🔹 Please send {swap_data['expected_amount']} {from_coin.upper()} to: {swap_data['send_to']} to complete your swap.\n")
        print(f"💱 Estimated Amount to Receive: {estimated_amount} {to_coin.upper()}")
        print(f"   - Your receiving address: {receiving_address}")

        save_swap(swap_data["transaction_id"], swap_data)

    except requests.RequestException as e:
        print(f"❌ Error: {e}")

def main():
    while True:
        print_header()
        print("1. Get Rate\n2. Initiate Swap\n3. Check Swap Status\n4. My Swaps\n5. Delete All Swap History\n6. Exit")
        choice = get_input("Choose an option (1-6): ")
        if choice == "1":
            get_rate()
        elif choice == "2":
            get_rate()
        elif choice == "3":
            check_swap_status()
        elif choice == "4":
            view_my_swaps()
        elif choice == "5":
            delete_all_swap_history()
        elif choice == "6":
            print("Goodbye!")
            exit(0)
        else:
            print("❌ Invalid choice! Returning to main menu.")

if __name__ == "__main__":
    main()
