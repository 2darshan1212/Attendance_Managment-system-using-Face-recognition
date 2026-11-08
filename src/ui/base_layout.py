import streamlit as st


def _is_dark_mode():
    return bool(st.session_state.get("dark_mode", False))


def style_background_home():
    background = (
        "radial-gradient(ellipse at 10% 5%, rgba(129, 140, 248, 0.18), transparent 34rem), "
        "linear-gradient(145deg, #202a42 0%, #111827 100%)"
        if _is_dark_mode()
        else "radial-gradient(ellipse at 10% 5%, rgba(99, 102, 241, 0.13), transparent 34rem), "
        "linear-gradient(145deg, #f3f5ff 0%, #e8edfb 100%)"
    )
    st.markdown(
        f"<style>.stApp {{ background: {background} !important; }}</style>",
        unsafe_allow_html=True,
    )


def style_background_dashboard():
    background = (
        "radial-gradient(ellipse at 90% 0%, rgba(129, 140, 248, 0.14), transparent 32rem), #111827"
        if _is_dark_mode()
        else "radial-gradient(ellipse at 90% 0%, rgba(99, 102, 241, 0.10), transparent 32rem), #f1f3fc"
    )
    st.markdown(
        f"<style>.stApp {{ background: {background} !important; }}</style>",
        unsafe_allow_html=True,
    )


def style_base_layout():
    dark_mode = _is_dark_mode()
    palette = {
        "scheme": "dark" if dark_mode else "light",
        "ink": "#eef2ff" if dark_mode else "#18213b",
        "muted": "#aab5cc" if dark_mode else "#64708b",
        "brand": "#5865f2",
        "brand_dark": "#4653db",
        "surface": "#1f293b" if dark_mode else "#ffffff",
        "surface_alt": "#28344a" if dark_mode else "#f3f5fb",
        "line": "#3b4860" if dark_mode else "#e1e6f2",
        "soft_brand": "#303a5a" if dark_mode else "#edf0ff",
        "soft_brand_hover": "#394568" if dark_mode else "#dfe4ff",
        "soft_brand_text": "#c5ccff" if dark_mode else "#3542b5",
        "soft_pink": "#482c43" if dark_mode else "#fce8f3",
        "soft_pink_hover": "#59324f" if dark_mode else "#f8d7e9",
        "soft_pink_text": "#ffd0e8" if dark_mode else "#92245c",
        "shadow": "rgba(0, 0, 0, 0.22)" if dark_mode else "rgba(32, 43, 82, 0.07)",
        "card_line": "#596985" if dark_mode else "#c6cee2",
        "card_shadow": "rgba(0, 0, 0, 0.32)" if dark_mode else "rgba(48, 62, 108, 0.12)",
        "student_accent": "#8290ff",
        "teacher_accent": "#ef8296",
    }

    _, theme_col2 = st.columns([5, 1], vertical_alignment="center")
    with theme_col2:
        st.toggle(
            "Dark mode",
            key="dark_mode",
            value=dark_mode,
            help="Switch between light and dark appearance.",
        )

    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&display=swap');

            .stApp {
                color-scheme: __SCHEME__;
                --ink: __INK__;
                --muted: __MUTED__;
                --brand: __BRAND__;
                --brand-dark: __BRAND_DARK__;
                --surface: __SURFACE__;
                --surface-alt: __SURFACE_ALT__;
                --line: __LINE__;
                --soft-brand: __SOFT_BRAND__;
                --soft-brand-hover: __SOFT_BRAND_HOVER__;
                --soft-brand-text: __SOFT_BRAND_TEXT__;
                --soft-pink: __SOFT_PINK__;
                --soft-pink-hover: __SOFT_PINK_HOVER__;
                --soft-pink-text: __SOFT_PINK_TEXT__;
                --card-line: __CARD_LINE__;
                --card-shadow: __CARD_SHADOW__;
                --student-accent: __STUDENT_ACCENT__;
                --teacher-accent: __TEACHER_ACCENT__;
            }

            #MainMenu, footer, header[data-testid="stHeader"] {
                visibility: hidden;
            }

            .stApp,
            .stApp [data-testid="stMarkdownContainer"],
            .stApp [data-testid="stWidgetLabel"],
            .stApp label,
            .stApp td,
            .stApp th {
                color: var(--ink);
                font-family: 'Outfit', sans-serif;
            }

            .block-container {
                max-width: 1120px;
                padding: 2rem 2rem 3rem !important;
            }

            .stApp [data-testid="stHeading"] h1,
            .stApp [data-testid="stHeading"] h2,
            .stApp [data-testid="stHeading"] h3,
            .stApp [data-testid="stHeading"] h4,
            .stApp [data-testid="stHeading"] h5,
            .stApp [data-testid="stHeading"] h6 {
                color: var(--ink) !important;
                font-family: 'Outfit', sans-serif !important;
                font-weight: 700 !important;
                line-height: 1.2 !important;
                letter-spacing: -0.025em;
            }

            .stApp [data-testid="stHeading"] h1 {
                font-size: clamp(2rem, 5vw, 3rem) !important;
            }

            .stApp [data-testid="stHeading"] h2 {
                font-size: clamp(1.45rem, 3vw, 2rem) !important;
            }

            .stApp [data-testid="stWidgetLabel"] p,
            .stApp [data-testid="stMarkdownContainer"] p {
                line-height: 1.55;
            }

            .stApp [data-testid="stVerticalBlockBorderWrapper"] {
                background: var(--surface);
                border: 2px solid var(--card-line) !important;
                border-radius: 24px;
                box-shadow: 0 12px 32px __SHADOW__;
            }

            .stApp .st-key-student-portal-card,
            .stApp .st-key-teacher-portal-card {
                min-height: 100%;
                overflow: hidden;
                padding: 20px 20px 18px !important;
                border: 2px solid var(--card-line) !important;
                border-radius: 24px !important;
                background: var(--surface);
                box-shadow: 0 16px 38px var(--card-shadow);
                transition: border-color 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease;
            }

            .stApp .st-key-student-portal-card {
                border-top: 6px solid var(--student-accent) !important;
            }

            .stApp .st-key-teacher-portal-card {
                border-top: 6px solid var(--teacher-accent) !important;
            }

            .stApp .st-key-student-portal-card:hover,
            .stApp .st-key-teacher-portal-card:hover {
                box-shadow: 0 20px 46px var(--card-shadow);
                transform: translateY(-3px);
            }

            .portal-illustration {
                overflow: hidden;
                margin: 0.75rem 0 1.1rem;
                border: 1px solid var(--line);
                border-radius: 18px;
                line-height: 0;
            }

            .portal-illustration svg {
                display: block;
                width: 100%;
                height: auto;
            }

            .stApp .st-key-student-portal-card [data-testid="stImage"] img,
            .stApp .st-key-teacher-portal-card [data-testid="stImage"] img {
                display: block;
                width: 100%;
                height: clamp(200px, 25vw, 260px);
                border: 1px solid var(--line);
                border-radius: 16px;
                background: var(--surface-alt);
                object-fit: cover;
                object-position: center 14%;
            }

            .stApp .st-key-student-portal-card [data-testid="stImage"] figcaption,
            .stApp .st-key-teacher-portal-card [data-testid="stImage"] figcaption {
                display: flex;
                min-height: 2.8rem;
                align-items: center;
                justify-content: center;
                padding: 0.4rem 0.15rem 0;
                color: var(--muted);
                font-size: 0.85rem;
                line-height: 1.35;
            }

            .brand-hero {
                display: flex;
                flex-direction: column;
                align-items: center;
                padding: 1rem 0 2.4rem;
                text-align: center;
            }

            .brand-header__logo {
                display: block;
                width: 64px;
                height: 64px;
                flex: 0 0 auto;
            }

            .brand-hero .brand-header__logo {
                width: 82px;
                height: 82px;
                margin-bottom: 1rem;
                filter: drop-shadow(0 10px 12px rgba(70, 83, 219, 0.2));
            }

            .brand-hero__eyebrow {
                margin: 0 0 0.5rem;
                color: var(--brand) !important;
                font-size: 0.78rem;
                font-weight: 800;
                letter-spacing: 0.16em;
            }

            .brand-hero__title {
                margin: 0;
                color: var(--ink);
                font-size: clamp(2.2rem, 6vw, 3.65rem);
                font-weight: 800;
                letter-spacing: -0.055em;
                line-height: 1.08;
            }

            .brand-hero__subtitle {
                margin: 0.65rem 0 0;
                color: var(--muted) !important;
                font-size: clamp(1rem, 2vw, 1.15rem);
            }

            .brand-header {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 0.8rem;
                min-height: 72px;
            }

            .brand-header__title {
                color: var(--ink);
                font-family: 'Outfit', sans-serif;
                font-size: 1.5rem;
                font-weight: 700;
                letter-spacing: -0.035em;
                line-height: 1.05;
            }

            .app-footer {
                padding: 1.5rem 0 0.25rem;
                color: var(--muted);
                font-family: 'Outfit', sans-serif;
                font-size: 0.88rem;
                text-align: center;
            }

            .stApp [data-testid="stButton"] > button {
                min-height: 44px;
                border: 1px solid transparent !important;
                border-radius: 14px !important;
                background: var(--brand) !important;
                color: #fff !important;
                font-family: 'Outfit', sans-serif !important;
                font-weight: 600 !important;
                transition: background-color 0.18s ease, box-shadow 0.18s ease, transform 0.18s ease !important;
            }

            .stApp [data-testid="stButton"] > button[kind="secondary"] {
                background: var(--soft-pink) !important;
                border-color: var(--line) !important;
                color: var(--soft-pink-text) !important;
            }

            .stApp [data-testid="stButton"] > button[kind="tertiary"] {
                background: var(--soft-brand) !important;
                border-color: var(--line) !important;
                color: var(--soft-brand-text) !important;
            }

            .stApp [data-testid="stButton"] > button[kind="primary"] *,
            .stApp [data-testid="stButton"] > button[kind="primary"] svg {
                color: #fff !important;
                fill: currentColor;
            }

            .stApp [data-testid="stButton"] > button[kind="secondary"] *,
            .stApp [data-testid="stButton"] > button[kind="secondary"] svg {
                color: var(--soft-pink-text) !important;
                fill: currentColor;
            }

            .stApp [data-testid="stButton"] > button[kind="tertiary"] *,
            .stApp [data-testid="stButton"] > button[kind="tertiary"] svg {
                color: var(--soft-brand-text) !important;
                fill: currentColor;
            }

            .stApp [data-testid="stButton"] > button:hover {
                background: var(--brand-dark) !important;
                box-shadow: 0 6px 16px rgba(70, 83, 219, 0.2);
                transform: translateY(-1px);
            }

            .stApp [data-testid="stButton"] > button[kind="secondary"]:hover {
                background: var(--soft-pink-hover) !important;
            }

            .stApp [data-testid="stButton"] > button[kind="tertiary"]:hover {
                background: var(--soft-brand-hover) !important;
            }

            .stApp [data-testid="stTextInput"] input,
            .stApp [data-testid="stNumberInput"] input,
            .stApp [data-testid="stSelectbox"] [data-baseweb="select"] > div,
            .stApp [data-testid="stTextArea"] textarea {
                border-radius: 12px;
                border-color: var(--line);
                background: var(--surface);
                color: var(--ink) !important;
                -webkit-text-fill-color: var(--ink);
            }

            .stApp [data-testid="stTextInput"] input::placeholder,
            .stApp [data-testid="stNumberInput"] input::placeholder,
            .stApp [data-testid="stTextArea"] textarea::placeholder {
                color: var(--muted) !important;
                -webkit-text-fill-color: var(--muted);
                opacity: 1;
            }

            .stApp [data-testid="stDataFrame"],
            .stApp [data-testid="stTable"] {
                border-radius: 14px;
                overflow: hidden;
            }

            .stApp [data-testid="stImage"] img {
                max-width: 100%;
                height: auto;
                object-fit: contain;
            }

            @media (max-width: 900px) {
                .block-container {
                    max-width: 100%;
                    padding: 1.5rem 1.25rem 2.5rem !important;
                }

                div[data-testid="stHorizontalBlock"] {
                    flex-wrap: wrap;
                    gap: 1rem;
                }

                div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] {
                    min-width: min(220px, 100%);
                }
            }

            @media (max-width: 640px) {
                .block-container {
                    padding: 1.1rem 1rem 2rem !important;
                }

                div[data-testid="stHorizontalBlock"] {
                    flex-direction: column;
                    gap: 0.8rem;
                }

                div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] {
                    width: 100% !important;
                    min-width: 100% !important;
                    flex: 1 1 100% !important;
                }

                .stApp [data-testid="stVerticalBlockBorderWrapper"],
                .stApp .st-key-student-portal-card,
                .stApp .st-key-teacher-portal-card {
                    border-radius: 18px;
                }

                div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]:has([data-testid="stToggle"]) {
                    min-width: 100% !important;
                    width: 100% !important;
                    flex-basis: 100% !important;
                }

                .stApp [data-testid="stButton"] > button {
                    min-height: 46px;
                }

                .stApp .st-key-student-portal-card [data-testid="stImage"] img,
                .stApp .st-key-teacher-portal-card [data-testid="stImage"] img {
                    height: 210px;
                    object-position: center 14%;
                }

                .brand-header {
                    justify-content: flex-start !important;
                }

                .brand-hero {
                    padding: 0.4rem 0 1.5rem;
                }

                .brand-hero .brand-header__logo {
                    width: 70px;
                    height: 70px;
                }

                .brand-header__title {
                    font-size: 1.35rem !important;
                }
            }

            @media (prefers-reduced-motion: reduce) {
                *, *::before, *::after {
                    scroll-behavior: auto !important;
                    transition-duration: 0.01ms !important;
                }
            }
        </style>
        """
        .replace("__SCHEME__", palette["scheme"])
        .replace("__INK__", palette["ink"])
        .replace("__MUTED__", palette["muted"])
        .replace("__BRAND_DARK__", palette["brand_dark"])
        .replace("__BRAND__", palette["brand"])
        .replace("__SURFACE_ALT__", palette["surface_alt"])
        .replace("__SURFACE__", palette["surface"])
        .replace("__LINE__", palette["line"])
        .replace("__SOFT_BRAND_HOVER__", palette["soft_brand_hover"])
        .replace("__SOFT_BRAND_TEXT__", palette["soft_brand_text"])
        .replace("__SOFT_BRAND__", palette["soft_brand"])
        .replace("__SOFT_PINK_HOVER__", palette["soft_pink_hover"])
        .replace("__SOFT_PINK_TEXT__", palette["soft_pink_text"])
        .replace("__SOFT_PINK__", palette["soft_pink"])
        .replace("__CARD_LINE__", palette["card_line"])
        .replace("__CARD_SHADOW__", palette["card_shadow"])
        .replace("__STUDENT_ACCENT__", palette["student_accent"])
        .replace("__TEACHER_ACCENT__", palette["teacher_accent"])
        .replace("__SHADOW__", palette["shadow"]),
        unsafe_allow_html=True,
    )
