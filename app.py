import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.student_screen import student_screen
from src.screens.teacher_screen import teacher_screen



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


def main():

    st.set_page_config(page_title="Student Attendance System", page_icon=_LOGO, layout="wide")

    # making temporoary memory  which stores states
    if "login_type" not in st.session_state:
        st.session_state["login_type"]=None

    # rendering screen based on login type 
    match st.session_state['login_type']:
        case "teacher":
            teacher_screen()

        case "student":
            student_screen()

        case None:
            home_screen()

main()