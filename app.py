from datetime import date
from pathlib import Path

import streamlit as st
from PIL import Image

# -----------------------------
# SETTINGS
# -----------------------------

HER_NAME = "Hadley Claire"
BIRTHDAY = date(2026, 10, 2)

PROJECT_FOLDER = Path(__file__).parent
PHOTO_FOLDER = PROJECT_FOLDER / "photos"

MESSAGES = [
    "I can't wait to celebrate you. 💗",
    "Every day with you is my favorite day.",
    "You make my world brighter.",
    "I hope today makes you smile.",
    "I love every little thing about you.",
]

# -----------------------------
# PAGE SETTINGS
# -----------------------------

st.set_page_config(
    page_title=f"{HER_NAME}'s Birthday Countdown",
    page_icon="💗",
    layout="centered",
)

st.markdown("""
<style>
.stApp{
    background: linear-gradient(#fff7fa,#fde9f0);
}

.main{
    text-align:center;
}

.title{
    font-size:55px;
    font-weight:bold;
    color:#d63384;
}

.subtitle{
    font-size:22px;
    color:#7a4a60;
}

.count{
    font-size:95px;
    font-weight:800;
    color:#e83e8c;
}

.card{
    background:white;
    padding:25px;
    border-radius:20px;
    box-shadow:0px 10px 25px rgba(0,0,0,.08);
    margin-top:20px;
}
</style>
""", unsafe_allow_html=True)

today = date.today()
days_left = (BIRTHDAY - today).days

st.markdown(
    f"""
<div class="main">

<div class="title">
💗 {HER_NAME}
</div>

<div class="subtitle">
Birthday Countdown
</div>

<div class="count">
{days_left}
</div>

<div class="subtitle">
days to go ❤️
</div>

</div>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# DAILY MESSAGE
# -----------------------------

message = MESSAGES[days_left % len(MESSAGES)]

st.markdown(
    f"""
<div class="card">
<h2>💌 Today's Note</h2>

{message}

</div>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# PHOTO
# -----------------------------

photos = []

if PHOTO_FOLDER.exists():
    photos = sorted(
        [
            p
            for p in PHOTO_FOLDER.iterdir()
            if p.suffix.lower() in [".jpg", ".jpeg", ".png", ".webp"]
        ]
    )

if photos:
    photo = photos[days_left % len(photos)]

    st.image(
        Image.open(photo),
        use_container_width=True,
    )

else:
    st.info("Add pictures to the photos folder ❤️")

# -----------------------------
# PROGRESS BAR
# -----------------------------

COUNTDOWN_START = date(2026, 7, 15)

total = (BIRTHDAY - COUNTDOWN_START).days
completed = (today - COUNTDOWN_START).days

progress = max(0, min(completed / total, 1))

st.write("### Countdown Progress")

st.progress(progress)

if days_left == 0:
    st.balloons()
    st.success("🎉 Happy Birthday Hadley!! ❤️")
    