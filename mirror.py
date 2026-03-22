import pandas as pd
import os
from scipy.spatial import distance

# --- STEP 1: LOCATE THE DATA ---
file_name = 'players.csv'

if os.path.exists(file_name):
    print(f"✅ Success: Found '{file_name}' in this folder.")
    df = pd.read_csv(file_name)
else:
    print(f"❌ Error: Cannot find '{file_name}'.")
    print(f"📍 I am currently looking in: {os.getcwd()}")
    print("💡 Fix: Make sure this script and the CSV are in the same folder.")
    exit()

# --- STEP 2: YOUR STATS ---
# [Serve Speed, Net %, Rally Length, Winner/UE Ratio]
user_stats = [112, 30, 4.8, 1.3] 

print(f"\nScanning the library for your Pro Mirror...")

# --- STEP 3: THE MATH ---
def find_distance(row):
    pro_stats = [
        row['avg_serve_speed'], 
        row['net_points_pct'], 
        row['avg_rally_length'], 
        row['winner_ue_ratio']
    ]
    # Calculating Euclidean Distance: $d = \sqrt{\sum (p_i - q_i)^2}$
    return distance.euclidean(user_stats, pro_stats)

# Calculate distance for every player and find the closest one
df['match_score'] = df.apply(find_distance, axis=1)
winner = df.loc[df['match_score'].idxmin()]

# --- STEP 4: THE REVEAL ---
print(f"--------------------------------------")
print(f"🏆 MATCH FOUND: {winner['player_name']}")
print(f"✨ STYLE: {winner['style_label']}")
print(f"--------------------------------------\n")