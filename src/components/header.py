import streamlit as st


_LOGO = """
<svg class="brand-header__logo" viewBox="0 0 64 64" role="img" aria-label="Attendance System logo">
  <defs>
    <linearGradient id="fras-logo-gradient" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#7380ff"/>
      <stop offset="1" stop-color="#4653db"/>
    </linearGradient>
  </defs>
  <rect x="2" y="2" width="60" height="60" rx="19" fill="url(#fras-logo-gradient)"/>
  <rect x="16" y="15" width="32" height="37" rx="7" fill="#fff"/>
  <path d="M25 15.5h14a3 3 0 0 1 3 3V23H22v-4.5a3 3 0 0 1 3-3Z" fill="#dfe3ff"/>
  <path d="m25 36 5 5 10-11" fill="none" stroke="#5865f2" stroke-linecap="round" stroke-linejoin="round" stroke-width="4"/>
</svg>
"""


def header_home():
    st.markdown(
        f"""
<div class="brand-hero">
{_LOGO}
<p class="brand-hero__eyebrow">FRAS · SMART ATTENDANCE</p>
<h1 class="brand-hero__title">Attendance, made simple.</h1>
<p class="brand-hero__subtitle">Fast, accurate attendance for your classroom.</p>
</div>
        """,
        unsafe_allow_html=True,
    )


def header_dashboard():
    st.markdown(
        f"""
<div class="brand-header">
{_LOGO}
<div class="brand-header__title">Attendance<br/>System</div>
</div>
        """,
        unsafe_allow_html=True,
    )
