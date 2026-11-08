import streamlit as st
def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background:var(--surface); border:1px solid var(--line); border-top:4px solid var(--brand); box-shadow:0 10px 24px rgba(32,43,82,.06); padding:22px; border-radius:18px; margin:12px 0;">
        <h3 style="margin:0; color:var(--ink); font-size:1.35rem; font-weight:700;">{name}</h3>
        <p style="color:var(--muted); margin:10px 0 14px;">Code: <span style="background:var(--soft-brand); color:var(--soft-brand-text); padding:3px 9px; border-radius:7px; font-weight:600;">{code}</span> <span style="padding-left:6px;">Section: {section}</span></p>
        
        """
    
    if stats:
        html+= """
        <div style="display:flex; gap:8px; flex-wrap:wrap; color:var(--muted);">
        """
        for icon, label, value in stats:
            html+= f'<div style="background:var(--surface-alt); padding:7px 12px; border-radius:10px; font-size:.9rem">{icon} <b>{value}</b> {label}</div>'
        
        html+= "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
