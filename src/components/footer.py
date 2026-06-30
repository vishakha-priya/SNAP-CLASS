import streamlit as st

def footer_home():
    logo_url="https://media.npr.org/assets/img/2016/03/16/snapchat-school_custom-b66fe98325260055c30f021056889f64fd7fb144.jpg"

    st.markdown(f"""
            <div style=" margin-top:2rem; display:flex; gap:6px;justify-content:center; item-align:center">
                <p style="font-weight:bold; color:white">📷 Every Click Counts & Every Lesson Matters❤️</p>
               
            </div>
                """,unsafe_allow_html=True)