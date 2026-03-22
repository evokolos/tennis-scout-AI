import os

print("\n--- 🛰️ Tennis Scout AI: GPS Check ---")

# 1. Where is the computer standing?
current_dir = os.getcwd()
print(f"📍 Current Folder: {current_dir}")

# 2. What files are in this folder?
files = os.listdir(current_dir)
print(f"📂 Files found: {files}")

# 3. Is the data file here?
if 'players.csv' in files:
    print("✅ SUCCESS: 'players.csv' is in the right place.")
    print("🚀 You are ready to run the Mirror Match!")
else:
    print("❌ MISSING: I don't see 'players.csv' here.")
    print(f"💡 Fix: Move your CSV file into the '{os.path.basename(current_dir)}' folder.")

print("--------------------------------------\n")