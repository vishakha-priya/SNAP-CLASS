import streamlit as st

def header_home():
    logo_url="https://media.npr.org/assets/img/2016/03/16/snapchat-school_custom-b66fe98325260055c30f021056889f64fd7fb144.jpg"

    st.markdown(f"""
            <div style="display:flex; flex-direction:row; align-item:center;justify-content:center;margin-bottom:30px">
                <img src='{logo_url}' style='height:100px;'/>
                <h1 style='text-align:center; color:#E0E3FF'>&nbspSNAP CLASS</h1>
            </div>
                """,unsafe_allow_html=True)
    
def header_dashboard():
    logo_url="https://media.npr.org/assets/img/2016/03/16/snapchat-school_custom-b66fe98325260055c30f021056889f64fd7fb144.jpg"

    st.markdown(f"""
            <div style="display:flex; align-item:center;justify-content:center;gap:10px">
                <img src='{logo_url}' style='height:85px;'/>
                <h2 style='text-align:left; color:white'>SNAP CLASS</h2>
            </div>
                """,unsafe_allow_html=True)
    