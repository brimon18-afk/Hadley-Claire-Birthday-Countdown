from __future__ import annotations

from datetime import date
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image


# =========================================================
# SETTINGS
# =========================================================

HER_NAME = "Hadley Claire"
BIRTHDAY = date(2026, 10, 2)
COUNTDOWN_START = date(2026, 7, 15)

PROJECT_FOLDER = Path(__file__).resolve().parent
PHOTOS_FOLDER = PROJECT_FOLDER / "photos"

BIRTHDAY_TIMESTAMP = "2026-10-02T00:00:00"


# =========================================================
# DAILY CONTENT
# Add or replace these whenever you want.
# The app cycles through them based on the current date.
# =========================================================

DAILY_MESSAGES = [
    "I made this little corner of the internet just for you. 💗",
    "You make ordinary days feel much more special.",
    "I hope something unexpectedly lovely happens to you today.",
    "You deserve every soft, sweet, beautiful thing.",
    "I feel so lucky that I get to love you.",
    "You make the world feel warmer and gentler.",
    "You are my favorite person to talk to.",
    "I love every little thing that makes you Hadley Claire.",
]

REASONS_I_LOVE_YOU = [
    "I love how deeply you care about the people and things you love.",
    "I love how easily you make me laugh.",
    "I love the comfort I feel when I am with you.",
    "I love how uniquely and completely yourself you are.",
    "I love the sweetness you bring into my life.",
    "I love how beautiful your mind is.",
    "I love your excitement over the things you adore.",
    "I love that life feels more fun with you in it.",
]

QUOTES = [
    "You are my favorite place to go when my mind searches for peace.",
    "Some people make the world feel softer just by being in it.",
    "Love is made of all the little moments we choose to remember.",
    "You deserve a life filled with things that make your heart feel light.",
    "The best parts of life are often the people who make us feel at home.",
]

SONGS = [
    {
        "title": "Today’s song",
        "artist": "Add one of Hadley’s favorite songs",
        "url": "",
    },
    {
        "title": "A song that reminds me of you",
        "artist": "Replace this with an artist and song",
        "url": "",
    },
]

MEMORIES = [
    "One of my favorite memories is any moment when we were laughing so hard that nothing else mattered.",
    "I love thinking about the small, ordinary moments that became special because they were with you.",
    "Some of my happiest memories are simply being beside you.",
    "I hope we keep collecting tiny memories that become our favorite stories.",
]

DAILY_PROMPTS = [
    "Find one tiny thing today that makes you happy.",
    "Give yourself the same kindness you so easily give other people.",
    "Take a picture of something pink today. 💗",
    "Pet a cat, admire a cat, or think fondly about a cat. 🐈",
    "Do one thing today purely because it makes you smile.",
]

BIRTHDAY_LETTER = """
Happy birthday, my love.

I hope today reminds you of how deeply loved, appreciated, and celebrated
you are. You bring so much warmth, sweetness, humor, and beauty into my
life, and I feel incredibly lucky that I get to know and love you.

I hope this next year brings you more happiness, confidence, adventure,
peace, cats, pink things, and every beautiful experience you deserve.

I love you so much.

Happy birthday, Hadley Claire. 💗
"""


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title=f"{HER_NAME}'s Birthday Countdown",
    page_icon="🐈",
    layout="centered",
    initial_sidebar_state="collapsed",
)


# =========================================================
# GLOBAL PAGE STYLING
# =========================================================

st.markdown(
    """
    <style>
        .stApp {
            background:
                radial-gradient(circle at 10% 20%, rgba(255,255,255,0.7), transparent 25%),
                radial-gradient(circle at 90% 15%, rgba(255,205,230,0.55), transparent 24%),
                linear-gradient(180deg, #fff4fa 0%, #ffdced 48%, #fbcbe2 100%);
            color: #6f3150;
        }

        .block-container {
            max-width: 820px;
            padding-top: 1.5rem;
            padding-bottom: 6rem;
        }

        header {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        .hero-card {
            background: rgba(255,255,255,0.83);
            border: 2px solid rgba(235, 106, 167, 0.20);
            border-radius: 32px;
            padding: 30px 22px;
            box-shadow: 0 18px 45px rgba(180, 73, 125, 0.16);
            text-align: center;
            backdrop-filter: blur(10px);
            margin-bottom: 20px;
        }

        .eyebrow {
            text-transform: uppercase;
            letter-spacing: 0.18em;
            font-size: 0.74rem;
            font-weight: 700;
            color: #c95b91;
            margin-bottom: 8px;
        }

        .hero-title {
            font-size: clamp(2.4rem, 7vw, 4.6rem);
            font-weight: 900;
            color: #a93670;
            line-height: 1.02;
            margin: 0;
        }

        .hero-subtitle {
            color: #925673;
            font-size: 1.05rem;
            margin-top: 12px;
        }

        .content-card {
            background: rgba(255,255,255,0.79);
            border: 1px solid rgba(222, 89, 150, 0.18);
            border-radius: 25px;
            padding: 24px;
            margin-top: 18px;
            box-shadow: 0 12px 32px rgba(174, 70, 120, 0.11);
        }

        .section-title {
            font-size: 1.35rem;
            font-weight: 850;
            color: #9f376a;
            text-align: center;
            margin-bottom: 12px;
        }

        .center-copy {
            text-align: center;
            line-height: 1.75;
            font-size: 1.03rem;
            color: #71415a;
        }

        .tiny-copy {
            text-align: center;
            color: #a06b84;
            font-size: 0.88rem;
            margin-top: 12px;
        }

        .paw-divider {
            text-align: center;
            letter-spacing: 0.7rem;
            color: #d75e98;
            margin: 24px 0 8px;
            font-size: 1.25rem;
        }

        .birthday-letter {
            white-space: pre-line;
            text-align: left;
            line-height: 1.9;
            color: #704257;
            font-size: 1.02rem;
        }

        .stButton > button {
            display: block;
            margin: 0 auto;
            background: linear-gradient(135deg, #ee75ae, #ca4f8d);
            color: white;
            border: none;
            border-radius: 999px;
            padding: 0.85rem 1.5rem;
            font-size: 1.02rem;
            font-weight: 800;
            box-shadow: 0 10px 25px rgba(197, 64, 132, 0.24);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .stButton > button:hover {
            transform: translateY(-2px) scale(1.02);
            box-shadow: 0 14px 32px rgba(197, 64, 132, 0.31);
            color: white;
        }

        [data-testid="stImage"] img {
            border-radius: 25px;
            border: 6px solid white;
            box-shadow: 0 15px 34px rgba(130, 48, 92, 0.17);
        }

        [data-testid="stProgressBar"] > div > div {
            background: linear-gradient(90deg, #f086b9, #c94d8b);
        }

        @media (max-width: 600px) {
            .block-container {
                padding-left: 0.9rem;
                padding-right: 0.9rem;
            }

            .hero-card {
                border-radius: 24px;
                padding: 25px 16px;
            }

            .content-card {
                border-radius: 21px;
                padding: 20px;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# ANIMATED BACKGROUND
# =========================================================

components.html(
    """
    <div class="animation-layer">
        <span class="floating-item item-1">💗</span>
        <span class="floating-item item-2">🐾</span>
        <span class="floating-item item-3">💕</span>
        <span class="floating-item item-4">🐾</span>
        <span class="floating-item item-5">💗</span>

        <div class="peek-cat">
            <div class="ear ear-left"></div>
            <div class="ear ear-right"></div>
            <div class="cat-head">
                <div class="eye eye-left"></div>
                <div class="eye eye-right"></div>
                <div class="nose"></div>
                <div class="mouth"></div>
            </div>
            <div class="paw paw-left"></div>
            <div class="paw paw-right"></div>
        </div>

        <div class="walking-cat">
            <div class="walk-tail"></div>
            <div class="walk-body"></div>
            <div class="walk-head">
                <div class="walk-ear left"></div>
                <div class="walk-ear right"></div>
                <div class="walk-eye left"></div>
                <div class="walk-eye right"></div>
                <div class="walk-nose"></div>
            </div>
            <div class="leg leg-one"></div>
            <div class="leg leg-two"></div>
        </div>
    </div>

    <style>
        html, body {
            margin: 0;
            overflow: hidden;
            background: transparent;
        }

        .animation-layer {
            position: fixed;
            inset: 0;
            pointer-events: none;
            overflow: hidden;
            z-index: 999;
        }

        .floating-item {
            position: absolute;
            bottom: -40px;
            font-size: 24px;
            opacity: 0;
            animation: floatUp 11s infinite ease-in;
        }

        .item-1 { left: 7%; animation-delay: 0s; }
        .item-2 { left: 26%; animation-delay: 2s; }
        .item-3 { left: 52%; animation-delay: 5s; }
        .item-4 { left: 72%; animation-delay: 1s; }
        .item-5 { left: 89%; animation-delay: 7s; }

        @keyframes floatUp {
            0% {
                transform: translateY(0) rotate(0deg) scale(0.8);
                opacity: 0;
            }
            15% {
                opacity: 0.55;
            }
            75% {
                opacity: 0.35;
            }
            100% {
                transform: translateY(-110vh) rotate(24deg) scale(1.2);
                opacity: 0;
            }
        }

        .peek-cat {
            position: fixed;
            right: 18px;
            top: 18%;
            width: 95px;
            height: 100px;
            transform: translateX(76px);
            animation: peek 8s infinite ease-in-out;
        }

        @keyframes peek {
            0%, 25%, 100% { transform: translateX(76px); }
            35%, 65% { transform: translateX(15px); }
            72% { transform: translateX(35px); }
        }

        .cat-head {
            position: absolute;
            top: 23px;
            left: 12px;
            width: 70px;
            height: 62px;
            background: #ff9fc9;
            border: 3px solid #c84c87;
            border-radius: 48% 48% 44% 44%;
        }

        .ear {
            position: absolute;
            top: 7px;
            width: 30px;
            height: 34px;
            background: #ff9fc9;
            border: 3px solid #c84c87;
            transform: rotate(45deg);
            border-radius: 7px;
        }

        .ear-left { left: 10px; }
        .ear-right { right: 12px; }

        .eye {
            position: absolute;
            top: 22px;
            width: 8px;
            height: 11px;
            background: #713047;
            border-radius: 50%;
            animation: blink 4s infinite;
        }

        .eye-left { left: 17px; }
        .eye-right { right: 17px; }

        @keyframes blink {
            0%, 44%, 48%, 100% { transform: scaleY(1); }
            46% { transform: scaleY(0.15); }
        }

        .nose {
            position: absolute;
            left: 31px;
            top: 34px;
            width: 9px;
            height: 7px;
            background: #d84f86;
            border-radius: 60% 60% 80% 80%;
        }

        .mouth {
            position: absolute;
            left: 27px;
            top: 41px;
            width: 17px;
            height: 8px;
            border-bottom: 2px solid #8d3a5d;
            border-radius: 50%;
        }

        .paw {
            position: absolute;
            bottom: 2px;
            width: 29px;
            height: 22px;
            background: #ffafd2;
            border: 3px solid #c84c87;
            border-radius: 50%;
        }

        .paw-left { left: 15px; }
        .paw-right { right: 14px; }

        .walking-cat {
            position: fixed;
            bottom: 6px;
            left: -140px;
            width: 125px;
            height: 80px;
            animation: walkAcross 20s infinite linear;
        }

        @keyframes walkAcross {
            0% { transform: translateX(-160px); }
            100% { transform: translateX(calc(100vw + 210px)); }
        }

        .walk-body {
            position: absolute;
            left: 32px;
            top: 31px;
            width: 65px;
            height: 38px;
            background: #f88fbd;
            border: 3px solid #bd447d;
            border-radius: 50%;
        }

        .walk-head {
            position: absolute;
            left: 8px;
            top: 21px;
            width: 43px;
            height: 40px;
            background: #ff9fc9;
            border: 3px solid #bd447d;
            border-radius: 48%;
        }

        .walk-ear {
            position: absolute;
            top: -9px;
            width: 18px;
            height: 21px;
            background: #ff9fc9;
            border: 3px solid #bd447d;
            border-radius: 5px;
            transform: rotate(45deg);
        }

        .walk-ear.left { left: 2px; }
        .walk-ear.right { right: 2px; }

        .walk-eye {
            position: absolute;
            top: 13px;
            width: 5px;
            height: 7px;
            background: #6e2946;
            border-radius: 50%;
        }

        .walk-eye.left { left: 10px; }
        .walk-eye.right { right: 10px; }

        .walk-nose {
            position: absolute;
            left: 18px;
            top: 23px;
            width: 6px;
            height: 5px;
            background: #ce477e;
            border-radius: 50%;
        }

        .walk-tail {
            position: absolute;
            right: 9px;
            top: 18px;
            width: 44px;
            height: 16px;
            border-top: 7px solid #bd447d;
            border-radius: 50%;
            transform: rotate(-25deg);
            animation: tailWag 1.2s infinite ease-in-out;
        }

        @keyframes tailWag {
            0%, 100% { transform: rotate(-25deg); }
            50% { transform: rotate(2deg); }
        }

        .leg {
            position: absolute;
            bottom: 4px;
            width: 10px;
            height: 24px;
            background: #f88fbd;
            border: 3px solid #bd447d;
            border-radius: 8px;
            transform-origin: top;
            animation: legWalk 0.6s infinite alternate;
        }

        .leg-one { left: 45px; }
        .leg-two {
            left: 78px;
            animation-delay: 0.3s;
        }

        @keyframes legWalk {
            from { transform: rotate(-18deg); }
            to { transform: rotate(18deg); }
        }
    </style>
    """,
    height=1,
)


# =========================================================
# HELPERS
# =========================================================

def get_photo_files() -> list[Path]:
    if not PHOTOS_FOLDER.exists():
        return []

    return sorted(
        path
        for path in PHOTOS_FOLDER.iterdir()
        if path.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}
    )


def daily_index(items: list[object]) -> int:
    if not items:
        return 0

    days_since_start = max((date.today() - COUNTDOWN_START).days, 0)
    return days_since_start % len(items)


def render_card(title: str, body: str, icon: str) -> None:
    st.markdown(
        f"""
        <div class="content-card">
            <div class="section-title">{icon} {title}</div>
            <div class="center-copy">{body}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def show_pink_confetti() -> None:
    components.html(
        """
        <canvas id="confetti-canvas"></canvas>

        <style>
            html, body {
                margin: 0;
                overflow: hidden;
                background: transparent;
            }

            #confetti-canvas {
                position: fixed;
                inset: 0;
                width: 100%;
                height: 100%;
                pointer-events: none;
            }
        </style>

        <script>
            const canvas = document.getElementById("confetti-canvas");
            const ctx = canvas.getContext("2d");

            function resizeCanvas() {
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
            }

            resizeCanvas();
            window.addEventListener("resize", resizeCanvas);

            const pieces = [];
            const symbols = ["💗", "💕", "🐾", "🐈"];

            for (let i = 0; i < 160; i++) {
                pieces.push({
                    x: Math.random() * canvas.width,
                    y: Math.random() * -canvas.height,
                    size: 10 + Math.random() * 17,
                    speed: 1.2 + Math.random() * 3.5,
                    drift: -1.3 + Math.random() * 2.6,
                    rotation: Math.random() * Math.PI * 2,
                    rotationSpeed: -0.05 + Math.random() * 0.1,
                    color: [
                        "#ff78b4",
                        "#ff9aca",
                        "#f35c9c",
                        "#ffd2e6",
                        "#d94f90"
                    ][Math.floor(Math.random() * 5)],
                    symbol: Math.random() > 0.78
                        ? symbols[Math.floor(Math.random() * symbols.length)]
                        : null
                });
            }

            function draw() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);

                pieces.forEach((piece) => {
                    piece.y += piece.speed;
                    piece.x += piece.drift;
                    piece.rotation += piece.rotationSpeed;

                    if (piece.y > canvas.height + 30) {
                        piece.y = -30;
                        piece.x = Math.random() * canvas.width;
                    }

                    ctx.save();
                    ctx.translate(piece.x, piece.y);
                    ctx.rotate(piece.rotation);

                    if (piece.symbol) {
                        ctx.font = `${piece.size}px Arial`;
                        ctx.fillText(piece.symbol, 0, 0);
                    } else {
                        ctx.fillStyle = piece.color;
                        ctx.fillRect(
                            -piece.size / 2,
                            -piece.size / 4,
                            piece.size,
                            piece.size / 2
                        );
                    }

                    ctx.restore();
                });

                requestAnimationFrame(draw);
            }

            draw();
        </script>
        """,
        height=1,
    )


# =========================================================
# COUNTDOWN
# =========================================================

today = date.today()
days_left = (BIRTHDAY - today).days
photo_files = get_photo_files()

countdown_html = f"""
<div class="countdown-shell">
    <div class="cat-ears">
        <span class="cat-ear left-ear"></span>
        <span class="cat-ear right-ear"></span>
    </div>

    <div class="countdown-grid">
        <div class="time-card">
            <div id="days" class="time-number">0</div>
            <div class="time-label">Days</div>
        </div>

        <div class="time-card">
            <div id="hours" class="time-number">00</div>
            <div class="time-label">Hours</div>
        </div>

        <div class="time-card">
            <div id="minutes" class="time-number">00</div>
            <div class="time-label">Minutes</div>
        </div>

        <div class="time-card">
            <div id="seconds" class="time-number">00</div>
            <div class="time-label">Seconds</div>
        </div>
    </div>

    <div id="birthday-message" class="birthday-message"></div>
</div>

<style>
    html, body {{
        margin: 0;
        background: transparent;
        font-family: Arial, sans-serif;
    }}

    .countdown-shell {{
        position: relative;
        background: rgba(255,255,255,0.84);
        border: 2px solid rgba(221, 77, 147, 0.18);
        border-radius: 30px;
        padding: 35px 18px 23px;
        box-shadow: 0 15px 40px rgba(172, 57, 117, 0.14);
    }}

    .cat-ears {{
        position: absolute;
        top: -24px;
        left: 50%;
        width: 150px;
        transform: translateX(-50%);
    }}

    .cat-ear {{
        position: absolute;
        width: 52px;
        height: 52px;
        background: #ff9dc8;
        border: 4px solid #c54783;
        border-radius: 9px;
        transform: rotate(45deg);
    }}

    .left-ear {{
        left: 12px;
    }}

    .right-ear {{
        right: 12px;
    }}

    .countdown-grid {{
        position: relative;
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 12px;
        z-index: 2;
    }}

    .time-card {{
        background: linear-gradient(180deg, #fff5fa, #ffe2ef);
        border: 1px solid rgba(213, 76, 140, 0.17);
        border-radius: 20px;
        padding: 20px 7px;
        text-align: center;
    }}

    .time-number {{
        color: #b13b76;
        font-size: clamp(1.9rem, 6vw, 3.1rem);
        line-height: 1;
        font-weight: 900;
    }}

    .time-label {{
        color: #92546f;
        font-size: 0.82rem;
        font-weight: 750;
        margin-top: 8px;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }}

    .birthday-message {{
        color: #b13b76;
        text-align: center;
        font-weight: 850;
        font-size: 1.35rem;
        margin-top: 20px;
    }}

    @media (max-width: 540px) {{
        .countdown-grid {{
            grid-template-columns: repeat(2, 1fr);
        }}
    }}
</style>

<script>
    const birthday = new Date("{BIRTHDAY_TIMESTAMP}").getTime();

    function updateCountdown() {{
        const now = new Date().getTime();
        const distance = birthday - now;

        if (distance <= 0) {{
            document.getElementById("days").innerText = "0";
            document.getElementById("hours").innerText = "00";
            document.getElementById("minutes").innerText = "00";
            document.getElementById("seconds").innerText = "00";
            document.getElementById("birthday-message").innerText =
                "Happy birthday, Hadley Claire! 🐈💗";
            return;
        }}

        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor(
            (distance % (1000 * 60 * 60 * 24)) /
            (1000 * 60 * 60)
        );
        const minutes = Math.floor(
            (distance % (1000 * 60 * 60)) /
            (1000 * 60)
        );
        const seconds = Math.floor(
            (distance % (1000 * 60)) /
            1000
        );

        document.getElementById("days").innerText = days;
        document.getElementById("hours").innerText =
            String(hours).padStart(2, "0");
        document.getElementById("minutes").innerText =
            String(minutes).padStart(2, "0");
        document.getElementById("seconds").innerText =
            String(seconds).padStart(2, "0");
    }}

    updateCountdown();
    setInterval(updateCountdown, 1000);
</script>
"""


# =========================================================
# BIRTHDAY PAGE
# =========================================================

if days_left <= 0:
    show_pink_confetti()

    st.markdown(
        f"""
        <div class="hero-card">
            <div class="eyebrow">The day is finally here</div>
            <div class="hero-title">Happy Birthday,<br>{HER_NAME}! 🐈💗</div>
            <div class="hero-subtitle">
                Today is entirely about celebrating you.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    components.html(countdown_html, height=360)

    st.markdown(
        """
        <div class="paw-divider">🐾 🐾 🐾</div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="content-card">
            <div class="section-title">💌 Your Birthday Letter</div>
            <div class="birthday-letter">{BIRTHDAY_LETTER}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if photo_files:
        st.markdown(
            """
            <div class="section-title" style="margin-top:28px;">
                📸 A Few Little Memories
            </div>
            """,
            unsafe_allow_html=True,
        )

        for photo_path in photo_files[:8]:
            try:
                st.image(
                    Image.open(photo_path),
                    use_container_width=True,
                )
            except Exception:
                continue

    st.markdown(
        """
        <div class="content-card">
            <div class="section-title">🐈 Birthday Cat Message</div>
            <div class="center-copy">
                The official council of pink birthday cats has declared
                today Hadley Claire Day.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# COUNTDOWN PAGE
# =========================================================

else:
    st.markdown(
        f"""
        <div class="hero-card">
            <div class="eyebrow">A little corner of the internet for</div>
            <div class="hero-title">{HER_NAME} 🐈💗</div>
            <div class="hero-subtitle">
                A new little surprise is waiting for you every day.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    components.html(countdown_html, height=385)

    total_countdown_days = max(
        (BIRTHDAY - COUNTDOWN_START).days,
        1,
    )

    elapsed_days = max(
        (today - COUNTDOWN_START).days,
        0,
    )

    countdown_progress = min(
        elapsed_days / total_countdown_days,
        1.0,
    )

    st.markdown(
        """
        <div class="section-title" style="margin-top:18px;">
            Countdown Progress
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.progress(countdown_progress)

    st.markdown(
        f"""
        <div class="tiny-copy">
            {days_left} days until October 2 💗
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="paw-divider">🐾 🐾 🐾</div>
        """,
        unsafe_allow_html=True,
    )

    if "surprise_open" not in st.session_state:
        st.session_state.surprise_open = False

    if st.button("🐾 Open Today’s Surprise"):
        st.session_state.surprise_open = True

    if st.session_state.surprise_open:
        today_message = DAILY_MESSAGES[daily_index(DAILY_MESSAGES)]
        today_reason = REASONS_I_LOVE_YOU[
            daily_index(REASONS_I_LOVE_YOU)
        ]
        today_quote = QUOTES[daily_index(QUOTES)]
        today_memory = MEMORIES[daily_index(MEMORIES)]
        today_prompt = DAILY_PROMPTS[daily_index(DAILY_PROMPTS)]
        today_song = SONGS[daily_index(SONGS)]

        render_card(
            "Today’s Note",
            today_message,
            "💌",
        )

        if photo_files:
            chosen_photo = photo_files[daily_index(photo_files)]

            st.markdown(
                """
                <div class="section-title" style="margin-top:28px;">
                    📸 Today’s Picture
                </div>
                """,
                unsafe_allow_html=True,
            )

            try:
                st.image(
                    Image.open(chosen_photo),
                    use_container_width=True,
                    caption="A little picture chosen for today 💗",
                )
            except Exception:
                st.warning(
                    "This photo could not be displayed. Try a JPG or PNG."
                )
        else:
            st.info(
                "Add JPG or PNG files to the photos folder "
                "and one will appear here each day."
            )

        render_card(
            "A Reason I Love You",
            today_reason,
            "🐾",
        )

        render_card(
            "Today’s Little Memory",
            today_memory,
            "📖",
        )

        render_card(
            "A Tiny Quote",
            f"“{today_quote}”",
            "✨",
        )

        render_card(
            "Today’s Mission",
            today_prompt,
            "🌸",
        )

        if today_song["url"]:
            st.markdown(
                f"""
                <div class="content-card">
                    <div class="section-title">🎵 Today’s Song</div>
                    <div class="center-copy">
                        <strong>{today_song["title"]}</strong><br>
                        {today_song["artist"]}<br><br>
                        <a href="{today_song["url"]}" target="_blank">
                            Listen here 💗
                        </a>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            render_card(
                "Today’s Song",
                (
                    f"{today_song['title']}<br>"
                    f"<em>{today_song['artist']}</em>"
                ),
                "🎵",
            )

        st.markdown(
            """
            <div class="content-card">
                <div class="section-title">🐈 A Message From the Pink Cats</div>
                <div class="center-copy">
                    You are required to remember that you are adorable,
                    deeply loved, and officially approved by every kawaii
                    pink cat on this website.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    else:
        st.markdown(
            """
            <div class="content-card">
                <div class="section-title">🐈 Today’s Surprise Is Waiting</div>
                <div class="center-copy">
                    Press the pink button to unlock today’s message,
                    picture, memory, and tiny cat-approved surprise.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="tiny-copy" style="margin-top:30px;">
            Made with an unreasonable amount of love, pink, and cats. 💗
        </div>
        """,
        unsafe_allow_html=True,
    )
    