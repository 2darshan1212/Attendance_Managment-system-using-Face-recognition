import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.student_screen import student_screen
from src.screens.teacher_screen import teacher_screen


def main():
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