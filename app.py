import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from scipy.spatial import distance

# --- 1. DATA LOADING ---
# Ensure 'players.csv' is in the same folder as this script!
df = pd.read_csv('players.csv')

st.title("🎾 Tennis Scout AI: DNA Comparison")

# --- 2. SIDEBAR INPUTS ---
st.sidebar.header("Scouting Profile")
s_speed = st.sidebar.slider("Serve Speed (mph)", 80, 140, 112)
s_net = st.sidebar.slider("Net Points %", 5, 80, 32)
s_rally = st.sidebar.slider("Avg Rally Length", 1.0, 12.0, 4.8)
s_ratio = st.sidebar.slider("Winner/UE Ratio", 0.5, 3.0, 1.4)

user_stats = [s_speed, s_net, s_rally, s_ratio]

# --- 3. THE AI ENGINE ---
# Calculating Euclidean Distance: $d = \sqrt{\sum (p_i - q_i)^2}$
def get_similarity(row):
    pro_stats = [row['avg_serve_speed'], row['net_points_pct'], 
                 row['avg_rally_length'], row['winner_ue_ratio']]
    return distance.euclidean(user_stats, pro_stats)

df['distance'] = df.apply(get_similarity, axis=1)
winner = df.loc[df['distance'].idxmin()]

# --- 4. DATA NORMALIZATION (For the Chart) ---
categories = ['Serve', 'Net', 'Rally', 'Efficiency']
user_norm = [((s_speed-80)/60)*100, ((s_net-5)/75)*100, ((s_rally-1)/11)*100, ((s_ratio-0.5)/2.5)*100]
pro_norm = [
    ((winner['avg_serve_speed']-80)/60)*100, 
    ((winner['net_points_pct']-5)/75)*100, 
    ((winner['avg_rally_length']-1)/11)*100, 
    ((winner['winner_ue_ratio']-0.5)/2.5)*100
]

# --- 5. RADAR CHART ---
fig = go.Figure()
fig.add_trace(go.Scatterpolar(r=user_norm, theta=categories, fill='toself', name='You'))
fig.add_trace(go.Scatterpolar(r=pro_norm, theta=categories, fill='toself', name=winner['player_name']))
fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])))

# --- 6. DISPLAY ---
st.header(f"Your Pro Mirror: {winner['player_name']}")
st.plotly_chart(fig)