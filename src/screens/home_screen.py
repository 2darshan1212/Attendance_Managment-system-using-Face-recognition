from pathlib import Path

import streamlit as st

from src.components.footer import footer_home
from src.components.header import header_home
from src.ui.base_layout import style_background_home, style_base_layout


_ASSET_DIR = Path(__file__).resolve().parents[1] / "assets"


def home_screen():
    style_background_home()
    style_base_layout()
    header_home()

    col1, col2 = st.columns(2, gap="large", vertical_alignment="top")

    with col1:
        with st.container(border=True, key="student-portal-card"):
            st.header("Student")
            st.caption("Your classes and attendance, all in one place.")
            st.image(
                str(_ASSET_DIR / "student.png"),
                caption="Learn, grow, and keep track of every class.",
                width="stretch",
            )
            if st.button(
                "Continue as student",
                type="primary",
                icon=":material/person:",
                icon_position="right",
                width="stretch",
                key="student-portal-button",
            ):
                st.session_state["login_type"] = "student"
                st.rerun()

    with col2:
        with st.container(border=True, key="teacher-portal-card"):
            st.header("Teacher")
            st.caption("Take attendance and organize your classes.")
            st.image(
                str(_ASSET_DIR / "teacher.png"),
                caption="Inspire your class and make every lesson count.",
                width="stretch",
            )
            if st.button(
                "Continue as teacher",
                type="primary",
                icon=":material/arrow_outward:",
                icon_position="right",
                width="stretch",
                key="teacher-portal-button",
            ):
                st.session_state["login_type"] = "teacher"
                st.rerun()

    footer_home()
