import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# ---------- Load data ----------
conn = sqlite3.connect("steam.db")
df = pd.read_sql_query("SELECT * FROM games", conn)

df["hours_forever"] = df["playtime_forever"] / 60
df["hours_2weeks"] = df["playtime_2weeks"] / 60

# ---------- KPIs ----------
total_games = len(df)
total_hours = df["hours_forever"].sum()
active_games = (df["hours_2weeks"] > 0).sum()
active_pct = (active_games / total_games * 100) if total_games else 0

st.title("Steam Game Analytics Dashboard")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Games Owned", total_games)
c2.metric("Total Hours Played", f"{total_hours:.1f}")
c3.metric("Active Games (2w)", active_games)
c4.metric("Active Library %", f"{active_pct:.1f}%")

st.divider()

# ---------- Top 10 Games ----------
st.subheader("Top 10 Most Played Games")

top10 = df.sort_values("hours_forever", ascending=False).head(10)

fig, ax = plt.subplots()
ax.barh(top10["name"], top10["hours_forever"])
ax.invert_yaxis()
ax.set_xlabel("Hours Played")

st.pyplot(fig)

# ---------- Recent Activity ----------
st.subheader("Recently Played Games")

recent = df[df["hours_2weeks"] > 0].sort_values("hours_2weeks", ascending=False, ignore_index=True)

st.dataframe(
    recent[["name", "hours_2weeks", "hours_forever"]].rename(columns={"name": "Game", "hours_2weeks": "Hours past 2 weeks", "hours_forever": "Total Hours"})
)

# ---------- Concentration ----------
st.subheader("Playtime Concentration")

top3_hours = df.sort_values("hours_forever", ascending=False).head(3)["hours_forever"].sum()
concentration = (top3_hours / total_hours * 100) if total_hours else 0

st.metric("Top 3 Games Share of Total Time", f"{concentration:.1f}%")

# ---------- Distribution ----------
st.subheader("Playtime Distribution")

fig2, ax2 = plt.subplots()
ax2.hist(df["hours_forever"], bins=20)
ax2.set_xlabel("Hours Played")
ax2.set_ylabel("Number of Games")

st.pyplot(fig2)
