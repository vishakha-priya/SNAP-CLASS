import streamlit as st
def style_background_home():
    st.markdown("""
            <style>
                .stApp{
                   background: linear-gradient(135deg, #0F172A, #1E3A8A);!important;
                }
                .stApp div[data-testid="stColumn"]{
                        background-color:#E0E3Ff !important;
                        padding:1rem !important;
                        border-radius:2rem!important;
                        
                 }
  
            </style>
                """
                ,unsafe_allow_html=True)
    
def style_background_dashboard():
    st.markdown("""
            <style>
                .stApp{
                    background:#E0E3FF !important;
                }
            </style>
                """
                ,unsafe_allow_html=True)
    
def style_base_layout():
    st.markdown("""
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
                @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&display=swap');

                /*Hide Top Bar of streamlit*/
                #MainMenu , footer,header{
                       visibility:hidden;
                }

                .block-container{
                padding-top:1.5rem !important;
                }

                
                h1{
                font-family: "climate Crisis",sans-serif !important;
                font-size: 3.5rem !important;
                line-height:1.1 !important;
                margin-bottom:0rem !important;
               
                }

                h2{
                font-family: "climate Crisis",sans-serif !important;
                font-size: 1.5rem !important;
                line-height:1.1 !important;
                margin-bottom:0rem !important;
                color:black !important;
                text-aligment:center !important;
                }

                h3,h4,p{
                    font-family:"outfit",sans-serif;
                }

                button[kind="primary"]{
                    background:  #EB459E  !important;
                    border-radius: 1.5rem !important;
                    color: white !important;
                    padding: 10px 20px !impotant;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }

                button[kind="secondary"]{
                    background: #8B5CF6!important;
                    border-radius: 1.5rem !important;
                    color: white !important;
                    padding: 10px 20px !impotant;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }

                button[kind="tertiary"]{
                    background: black !important;
                    border-radius: 1.5rem !important;
                    color: white !important;
                    padding: 10px 20px !impotant;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }

                button:hover{
                    transform:scale(1.05)
                }
            </style>
                """
                ,unsafe_allow_html=True)