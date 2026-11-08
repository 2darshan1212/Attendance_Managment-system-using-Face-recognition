import streamlit as st


def footer_home():
    st.markdown(
        """
        <div class="app-footer">
            Secure, simple attendance for every class.
        </div>
        """,
        unsafe_allow_html=True,
    )


def footer_dashboard():
    st.markdown(
        """
        <div class="app-footer">
            FRAS · Smart attendance
        </div>
        """,
        unsafe_allow_html=True,
    )
