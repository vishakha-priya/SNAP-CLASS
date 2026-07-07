import streamlit as st
def style_background_home():
    st.markdown("""
            <style>
                .stApp{
                   background: linear-gradient(135deg, #F5F3FF, #C4B5FD);!important;
                }
                .stApp div[data-testid="stColumn"]{
                        background-color:#E0E3Ff !important;
                        padding:1rem !important;
                        border-radius:2rem!important;
                        border: 7px solid #A78BFA!important;
                    
                        
                 }
  
            </style>
                """
                ,unsafe_allow_html=True)
    
def style_background_dashboard():
    st.markdown("""
            <style>
                .stApp{
                    background:  linear-gradient(135deg, #EEF2FF, #C7D2FE)!important;
                }
            </style>
                """
                ,unsafe_allow_html=True)

    

    st.markdown("""
<style>

/* Password input container */
div[data-testid="stTextInput"]{
    border-radius:12px;
}

/* Input field */
div[data-testid="stTextInput"] input{
    background:#FAFCFF !important;
    color:black !important;
}

/* Container around input and eye icon */
div[data-testid="stTextInput"] div[data-baseweb="input"]{
    background:#FAFCFF !important;
    border:1px solid #3B82F6 !important;
    border-radius:12px !important;
}

/* Eye button */
div[data-testid="stTextInput"] div[data-baseweb="input"] button{
    background:#FAFCFF !important;
    border:none !important;
}

/* Hover */
div[data-testid="stTextInput"] div[data-baseweb="input"] button:hover{
    background:#7DB7FF !important;
}
.stTextInput input::placeholder {
    color: gray;
    opacity: 1;
}
/* Eye icon */
div[data-testid="stTextInput"] div[data-baseweb="input"] svg{
    fill:#1E3A8A !important;
}
/* Change the label color to black */
div[data-testid="stTextInput"] label {
    color: black !important;

</style>
""", unsafe_allow_html=True)
def style_base_layout():
    st.markdown("""
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
                
                @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&display=swap');

                /*Hide Top Bar of streamlit*/
                MainMenu , footer,header{
                        visibility:hidden;
                 }

                .block-container{
                padding-top:1.5rem !important;
                 }

                
                h1{
                font-family: "Climate Crisis",sans-serif !important;
                font-size: 3.5rem !important;
                line-height:1.1 !important;
                margin-bottom:0rem !important;
                color:#3730A3!important;
               
                }

                h2{
                font-family: "Climate Crisis",sans-serif !important;
                font-size: 1.5rem !important;
                line-height:1.1 !important;
                margin-bottom:0rem !important;
                color:black !important;
                text-aligment:center !important;
                }

                h3,h4,p{
                    font-family:"outfit",sans-serif;
                }

                div[data-testid="stHeading"] h3 {
                    color: black !important;
                }
    

            /* Make alert text black */
                div[data-testid="stAlert"] p {
                    color: black !important;
                }

            /* Make bold text inside alerts black */
                 div[data-testid="stAlert"] strong {
                    color: black !important;
                 }

             /* Dialog background */
                div[role="dialog"] {
                    background-color:#C8D9FF  !important;
                    color:black!important;
                    border-radius: 12px;
                 }
                
                div[data-testid="stSelectbox"] label {
                    color: black !important;
                }

             /* Dialog content */
                div[role="dialog"] > div {
                     background-color: #C8D9FF !important;
                     color:black!important;
                }
                
                div[data-testid="stCameraInput"] label,
                div[data-testid="stAudioInput"] label {
                    color: black !important;
                    font-weight: 600;
                }

                button[kind="primary"]{
                    background: #1D4ED8  !important;
                   
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
                    background: white !important;
                    border-radius: 1.5rem !important;
                    color: black !important;
                    padding: 10px 20px !impotant;
                    border: 1px solid #3B82F6  !important;
                    transition: transform 0.25s ease-in-out !important;
                    
                }

                button:hover{
                    transform:scale(1.05)
                }
            </style>
                """
                ,unsafe_allow_html=True)