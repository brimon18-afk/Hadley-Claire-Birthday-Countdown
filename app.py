import streamlit as st
import streamlit.components.v1 as components


# ---------------------------------------------------------
# PAGE SETTINGS
# ---------------------------------------------------------

st.set_page_config(
    page_title="Birthday Countdown for Princess Hadley Claire",
    page_icon="💗",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ---------------------------------------------------------
# REMOVE STREAMLIT MENUS + PAGE BACKGROUND
# ---------------------------------------------------------

st.markdown(
    """
    <style>
        header,
        footer,
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        [data-testid="stStatusWidget"],
        [data-testid="collapsedControl"] {
            display: none !important;
        }

        .stApp {
            min-height: 100vh;
            background:
                radial-gradient(
                    circle at 50% 25%,
                    #fffafd 0%,
                    #ffe8f3 48%,
                    #ffcce4 100%
                );
            overflow: hidden;
        }

        .block-container {
            max-width: 1250px;
            padding-top: 7vh;
            padding-left: 6vw;
            padding-right: 6vw;
            padding-bottom: 0;
        }

        .title-card {
            position: relative;
            z-index: 5;
            background: rgba(255, 255, 255, 0.88);
            border: 3px solid rgba(225, 74, 147, 0.18);
            border-radius: 38px;
            padding: 42px 25px;
            text-align: center;
            box-shadow:
                0 20px 55px rgba(184, 50, 115, 0.17),
                inset 0 0 35px rgba(255, 186, 219, 0.18);
            margin-bottom: 34px;
        }

        .main-title {
            color: #b52e70;
            font-size: clamp(2.3rem, 5vw, 4.8rem);
            font-weight: 900;
            line-height: 1.12;
            letter-spacing: 0.01em;
            margin: 0;
        }

        @media (max-width: 650px) {
            .block-container {
                padding-top: 7vh;
                padding-left: 3rem;
                padding-right: 3rem;
            }

            .title-card {
                padding: 30px 16px;
                border-radius: 28px;
            }

            .main-title {
                font-size: clamp(2rem, 10vw, 3.3rem);
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

st.markdown(
    """
    <div class="title-card">
        <h1 class="main-title">
            BIRTHDAY COUNTDOWN FOR<br>
            PRINCESS HADLEY CLAIRE 💗
        </h1>
    </div>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# LIVE COUNTDOWN + FLOATING EMOJIS
# ---------------------------------------------------------

components.html(
    """
    <div class="emoji-layer" aria-hidden="true">
        <span class="emoji e1">💗</span>
        <span class="emoji e2">👑</span>
        <span class="emoji e3">🐈</span>
        <span class="emoji e4">💕</span>
        <span class="emoji e5">🐱</span>
        <span class="emoji e6">👑</span>
        <span class="emoji e7">💗</span>
        <span class="emoji e8">🐈</span>
        <span class="emoji e9">💕</span>
        <span class="emoji e10">👑</span>
        <span class="emoji e11">🐱</span>
        <span class="emoji e12">💗</span>
        <span class="emoji e13">👑</span>
        <span class="emoji e14">🐈</span>
        <span class="emoji e15">💕</span>
        <span class="emoji e16">🐱</span>
        <span class="emoji e17">💗</span>
        <span class="emoji e18">👑</span>
        <span class="emoji e19">🐈</span>
        <span class="emoji e20">💕</span>
    </div>

    <div class="countdown-container">
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

        <div id="birthday-message"></div>
    </div>

    <style>
        html,
        body {
            margin: 0;
            padding: 0;
            overflow: visible;
            background: transparent;
            font-family:
                -apple-system,
                BlinkMacSystemFont,
                "Segoe UI",
                sans-serif;
        }

        .countdown-container {
            position: relative;
            z-index: 5;
            background: rgba(255, 255, 255, 0.88);
            border: 3px solid rgba(225, 74, 147, 0.18);
            border-radius: 38px;
            padding: 48px 28px;
            box-shadow:
                0 20px 55px rgba(184, 50, 115, 0.17),
                inset 0 0 35px rgba(255, 186, 219, 0.18);
        }

        .countdown-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 18px;
        }

        .time-card {
            background: linear-gradient(
                180deg,
                #fffafd 0%,
                #ffe1ef 100%
            );
            border: 2px solid rgba(218, 66, 137, 0.18);
            border-radius: 26px;
            padding: 31px 10px;
            text-align: center;
        }

        .time-number {
            color: #b52e70;
            font-size: clamp(2.6rem, 7vw, 4.6rem);
            font-weight: 900;
            line-height: 1;
        }

        .time-label {
            color: #96516e;
            font-size: 0.95rem;
            font-weight: 800;
            letter-spacing: 0.11em;
            text-transform: uppercase;
            margin-top: 14px;
        }

        #birthday-message {
            color: #b52e70;
            text-align: center;
            font-size: 1.8rem;
            font-weight: 900;
            margin-top: 25px;
        }

        /* Covers the full browser screen */
        .emoji-layer {
            position: fixed;
            inset: 0;
            width: 100vw;
            height: 100vh;
            pointer-events: none;
            overflow: hidden;
            z-index: 999999;
        }

        .emoji {
            position: absolute;
            display: block;
            font-size: clamp(25px, 3vw, 45px);
            opacity: 0.82;
            filter: drop-shadow(
                0 4px 4px rgba(180, 45, 112, 0.16)
            );
            animation:
                float-around 7s ease-in-out infinite alternate,
                gentle-spin 12s linear infinite;
        }

        .e1  { top: 3%;  left: 3%;  animation-delay: 0s; }
        .e2  { top: 4%;  left: 17%; animation-delay: 1s; }
        .e3  { top: 3%;  left: 35%; animation-delay: 2s; }
        .e4  { top: 4%;  left: 53%; animation-delay: 3s; }
        .e5  { top: 3%;  left: 70%; animation-delay: 1.5s; }
        .e6  { top: 4%;  right: 4%; animation-delay: 0.5s; }

        .e7  { top: 23%; left: 1.2%; animation-delay: 2.5s; }
        .e8  { top: 44%; left: 1%; animation-delay: 1s; }
        .e9  { top: 66%; left: 1.5%; animation-delay: 4s; }
        .e10 { top: 86%; left: 3%; animation-delay: 0s; }

        .e11 { top: 22%; right: 1.2%; animation-delay: 3s; }
        .e12 { top: 43%; right: 1%; animation-delay: 1.3s; }
        .e13 { top: 65%; right: 1.4%; animation-delay: 4.3s; }
        .e14 { top: 85%; right: 3%; animation-delay: 2s; }

        .e15 { bottom: 3%; left: 14%; animation-delay: 1s; }
        .e16 { bottom: 2%; left: 30%; animation-delay: 2.7s; }
        .e17 { bottom: 3%; left: 47%; animation-delay: 0.6s; }
        .e18 { bottom: 2%; left: 64%; animation-delay: 3.4s; }
        .e19 { bottom: 3%; left: 80%; animation-delay: 1.8s; }
        .e20 { bottom: 4%; right: 3%; animation-delay: 4.5s; }

        @keyframes float-around {
            0% {
                transform: translate(0, 0) scale(0.95);
            }

            50% {
                transform: translate(10px, -9px) scale(1.08);
            }

            100% {
                transform: translate(-8px, 8px) scale(1);
            }
        }

        @keyframes gentle-spin {
            from {
                rotate: -5deg;
            }

            to {
                rotate: 355deg;
            }
        }

        @media (max-width: 650px) {
            .countdown-container {
                padding: 28px 14px;
                border-radius: 28px;
            }

            .countdown-grid {
                grid-template-columns: repeat(2, 1fr);
                gap: 12px;
            }

            .time-card {
                padding: 23px 7px;
                border-radius: 21px;
            }

            .emoji {
                font-size: 27px;
            }
        }
    </style>

    <script>
        const birthday =
            new Date("2026-10-02T00:00:00-04:00").getTime();

        function updateCountdown() {
            const now = new Date().getTime();
            const distance = birthday - now;

            if (distance <= 0) {
                document.getElementById("days").innerText = "0";
                document.getElementById("hours").innerText = "00";
                document.getElementById("minutes").innerText = "00";
                document.getElementById("seconds").innerText = "00";

                document.getElementById(
                    "birthday-message"
                ).innerText =
                    "HAPPY BIRTHDAY, PRINCESS HADLEY CLAIRE! 💗👑";

                return;
            }

            const days = Math.floor(
                distance / (1000 * 60 * 60 * 24)
            );

            const hours = Math.floor(
                (
                    distance %
                    (1000 * 60 * 60 * 24)
                ) /
                (1000 * 60 * 60)
            );

            const minutes = Math.floor(
                (
                    distance %
                    (1000 * 60 * 60)
                ) /
                (1000 * 60)
            );

            const seconds = Math.floor(
                (
                    distance %
                    (1000 * 60)
                ) /
                1000
            );

            document.getElementById("days").innerText =
                days;

            document.getElementById("hours").innerText =
                String(hours).padStart(2, "0");

            document.getElementById("minutes").innerText =
                String(minutes).padStart(2, "0");

            document.getElementById("seconds").innerText =
                String(seconds).padStart(2, "0");
        }

        updateCountdown();
        setInterval(updateCountdown, 1000);
    </script>
    """,
    height=480,
    scrolling=False,
)