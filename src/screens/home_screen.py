import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_background_home,style_base_layout

def home_screen():
    header_home()
    style_background_home()
    style_base_layout()

    col1,col2= st.columns(2,gap="large")
    with col1:
        st.header("  I ' m Teacher")
        st.image("Images/Teacher logo.png",width=100)
        if st.button("Teacher Portal", icon=":material/arrow_outward:",icon_position="right"):
            st.session_state["login_type"]="teacher"
            st.rerun()

    with col2:
        st.header("  I ' m Student")
        st.image("Images/student logo.png",width=100)
        if st.button("Student Portal", icon=":material/arrow_outward:",icon_position="right"):
            st.session_state["login_type"]="student"
            st.rerun()
    footer_home()
