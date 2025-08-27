import streamlit as st
st.set_page_config(page_title="Synthetic NOTAM Reinforcing Pipeline", layout="wide")

import pandas as pd
import os
import re
import gdown
from notam_tags_rel_levels import notam_general_relevance  # importa il dizionario

# password check
password = st.text_input("🔑 Enter access password:", type="password")

if not password:  # se il campo è vuoto
    st.stop()

if password != st.secrets["APP_PASSWORD"]:
    st.error("❌ Wrong password")
    st.stop()

# scarico db.csv da Google Drive se non presente
CSV_PATH = "notam_db_extract.csv"
url = "https://drive.google.com/uc?id=1jdzan1EDwd4c-foEM3tZtCHqIE0T0J4X"   # sostituisci con l’ID del file definitivo su Drive

if not os.path.exists(CSV_PATH):
    with st.spinner("Downloading NOTAM database (first run)..."):
        gdown.download(url, CSV_PATH, quiet=False)

# carica il database congelato
df = pd.read_csv(CSV_PATH)

st.title("🛫 Synthetic NOTAM Reinforcing Pipeline")

# user login
username = st.text_input("Enter your username (use lowercase, no spaces):").strip().lower()
if not username:
    st.warning("Please enter your username to continue.")
    st.stop()

USER_CSV = f"feedback_{username}.csv"

# load or initialize user progress
if os.path.exists(USER_CSV):
    df_user = pd.read_csv(USER_CSV)
else:
    df_user = df.copy()

# ensure feedback columns exist
for col in ["fb_style", "fb_category", "fb_corrected_category",
            "fb_realism", "fb_impact_med", "fb_impact_tech", "fb_impact_land", "fb_notes"]:
    if col not in df_user.columns:
        df_user[col] = ""

# track current index
if "index" not in st.session_state:
    st.session_state.index = 0

current_idx = st.session_state.index
if current_idx >= len(df_user):
    st.success(f"✅ {username}, you have completed all NOTAMs. Thank you! 🎉")
    st.stop()

row = df_user.iloc[current_idx]

# progress bar
progress = (current_idx+1)/len(df_user)
st.progress(progress)
st.caption(f"NOTAM {current_idx+1} of {len(df_user)} for user: {username}")

# --- extract Context & NOTAM text ---
full_text = row["e_line"]

purpose_match = re.search(r"<Purpose>(.*?)</Purpose>", full_text)
topic_match = re.search(r"<Topic>(.*?)</Topic>", full_text)

purpose_text = purpose_match.group(1).strip() if purpose_match else ""
topic_text = topic_match.group(1).strip() if topic_match else ""

notam_match = re.split(r"</Topic>", full_text, maxsplit=1)
notam_text = notam_match[1].strip() if len(notam_match) > 1 else full_text.strip()

# --- horizontal Layout ---
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### 🗂️ Context")
    st.markdown(
        f"""
        <div style="
            background-color: #eef5ff;
            padding: 12px;
            border-radius: 8px;
            border: 1px solid #cce;
            font-size: 16px;
            font-weight: 500;
            line-height: 1.5;
            color: #000;
            ">
            <b>Purpose:</b> {purpose_text}<br>
            <b>Topic:</b> {topic_text}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("#### 📄 NOTAM Text")
    st.markdown(
        f"""
        <div style="
            background-color: #f9f9f9;
            padding: 18px 14px 22px 14px;  /* top, right, bottom, left */
            border-radius: 10px;
            border: 1px solid #ddd;
            font-family: monospace;
            font-size: 18px;
            line-height: 1.7;
            white-space: pre-wrap;
            word-wrap: break-word;
            color: #000;
            ">
            {notam_text}
        </div>
        """,
        unsafe_allow_html=True
    )

    # ---category info box ---
    category = row['tag_type']
    st.markdown("#### 🏷️ Category Information")

    custom_colors = {
        "yellow": "#f1c40f",
        "red": "#e74c3c",
        "green": "#2ecc71",
        "blue": "#3498db",
        "orange": "#e67e22"
    }

    if category in notam_general_relevance:
        cat_info = notam_general_relevance[category]
        # prendo il colore nativo e lo sostituisco con il mio
        base_color = cat_info["color"].lower()
        color = custom_colors.get(base_color, "#7f8c8d")  # default = grigio
        relevance = cat_info["relevance"]
        desc = cat_info["description"]

        # mapping relevance -> badge color
        badge_colors = {
            "Low": "#2ecc71",       # green
            "Medium": "#f1c40f",    # yellow
            "High": "#e67e22",      # orange
            "Critical": "#e74c3c"   # red
        }
        badge_color = badge_colors.get(relevance, "#95a5a6")

        # --- mini badge subito sotto titolo pagina ---
        st.markdown(
            f"""
            <div style='font-size:18px; margin-bottom:15px;'>
                <b>Category:</b> 
                <span style='background-color:{color}; color:#fff; 
                             padding:4px 10px; border-radius:10px;'><b>{category}</b></span>
                <span style='background-color:{badge_color}; color:#fff; 
                             padding:4px 10px; border-radius:10px; margin-left:8px;'><b>{relevance}</b></span>
            </div>
            """,
            unsafe_allow_html=True
        )

        # --- info card ---
        st.markdown(f"""
        <div style="border: 1px solid #ccc; border-radius: 10px; overflow: hidden;">

        <div style="background-color:{color}; color:#fff; padding:14px 18px; 
                    font-weight:bold; font-size:22px;">
            {category}
        </div>

        <div style="padding:20px; font-size:18px; line-height:1.8; color:#000; background-color:#fafafa;">
            <b style="font-size:19px;">Relevance:</b> 
            <span style="background-color:{badge_color}; color:#fff; 
                        padding:6px 14px; border-radius:14px; 
                        font-size:16px; font-weight:bold;">
            {relevance}
            </span>
            <br><br>
            <b style="font-size:19px;">Description:</b><br>
            <span style="font-size:17px;">{desc}</span>
        </div>
        </div>
        """, unsafe_allow_html=True)

        # --- impact classes with badges ---
        impact_map = {
            "Low": "#2ecc71",       # green
            "Medium": "#f1c40f",    # yellow
            "High": "#e67e22",      # orange
            "Critical": "#e74c3c"   # red
        }

        def badge(label, value):
            return f"""
        <div style='margin:2px 0; font-size:16px;'>
        <span style='font-weight:bold; color:#000;'>{label}:</span>
        <span style="background-color:{impact_map.get(value,'#95a5a6')}; color:#fff;
                    padding:4px 12px; border-radius:12px; font-weight:bold; margin-left:8px;">
            {value}
        </span>
        </div>
        """

        impact_html = (
            badge("MEDICAL EMERGENCY", row['class_impact_med']) +
            badge("TECHNICAL ISSUE", row['class_impact_tech']) +
            badge("LAND ASAP", row['class_impact_land'])
        )

        st.markdown(f"""
        <div style="margin-top:12px; margin-bottom:12px;
                    padding:12px 8px 20px 8px;  /* top, right, bottom, left */
                    border:1px solid #ddd; border-radius:8px; 
                    background-color:#fdfdfd; font-size:16px;">
        <b style="font-size:18px;">Impact Classes:</b>
        {impact_html}
        </div>
        """, unsafe_allow_html=True)
                
with col2:
    st.subheader("📋 Feedback Evaluation")

    # icao style
    style_labels = {1: "❌ Disagree", 2: "✅ Agree"}
    st.markdown("**ICAO Style Correct?**")
    style = st.radio(
        "",
        options=[1, 2],
        format_func=lambda x: style_labels[x],
        index=1,
        horizontal=True,
        key="style"
    )

    # correct category
    st.markdown("**Correct Category?**")
    correct_cat = st.radio(
        "",
        options=["Yes", "No"],
        index=0,
        horizontal=True,
        key="correct_cat"
    )

    chosen_cat = None
    if correct_cat == "No":
        categories = list(notam_general_relevance.keys())
        chosen_cat = st.selectbox("Select the correct category:", categories, key="chosen_cat")

    # operational realism
    realism_labels = {1: "🔴 Low ", 2: "🟢 High"}
    st.markdown("**Operational Realism?**")
    realism = st.radio(
        "",
        options=[1, 2],
        format_func=lambda x: realism_labels[x],
        index=1,
        horizontal=True,
        key="realism"
    )

    # perceived impact (override MED/TECH/LAND)
    st.markdown("**Perceived Impact?**")
    impact_levels = ["Low", "Medium", "High", "Critical"]

    impact_med = st.selectbox("🩺 Medical Emergency:", impact_levels, index=impact_levels.index(row['class_impact_med']))
    impact_tech = st.selectbox("⚙️ Technical Issue:", impact_levels, index=impact_levels.index(row['class_impact_tech']))
    impact_land = st.selectbox("🛬 Land ASAP:", impact_levels, index=impact_levels.index(row['class_impact_land']))

    # notes
    notes = st.text_area("📝 Notes (optional)", placeholder="Write a comment...", height=120)

    st.markdown("---")

    # save buttons
    colb1, colb2, colb3 = st.columns(3)

    if colb1.button("⬅️ Previous", disabled=(current_idx == 0)):
        st.session_state.index -= 1
        st.rerun()

    if colb2.button("💾 Save Feedback"):
        # salva dati
        df_user.at[current_idx, "fb_style"] = style
        df_user.at[current_idx, "fb_category"] = 1 if correct_cat == "Yes" else 0
        df_user.at[current_idx, "fb_corrected_category"] = chosen_cat if correct_cat == "No" and chosen_cat else ""
        df_user.at[current_idx, "fb_realism"] = realism
        df_user.at[current_idx, "fb_impact_med"] = impact_med
        df_user.at[current_idx, "fb_impact_tech"] = impact_tech
        df_user.at[current_idx, "fb_impact_land"] = impact_land
        df_user.at[current_idx, "fb_notes"] = notes

        df_user.to_csv(USER_CSV, index=False)
        st.success("✅ Feedback saved. Now click NEXT to continue.")

    if colb3.button("Next ➡️"):
        st.session_state.index += 1
        st.rerun()

    # --- keep only selected columns for saving ---
    cols_keep = [
        "e_line", "tag_type", "relevance_level",
        "class_impact_med", "class_impact_tech", "class_impact_land",
        "fb_style", "fb_category", "fb_corrected_category", "fb_realism",
        "fb_impact_med", "fb_impact_tech", "fb_impact_land", "fb_notes"
    ]

    # se qualche colonna di feedback non esiste ancora, la aggiungo vuota
    for col in cols_keep:
        if col not in df_user.columns:
            df_user[col] = ""

    df_user[cols_keep].to_csv(USER_CSV, index=False)
