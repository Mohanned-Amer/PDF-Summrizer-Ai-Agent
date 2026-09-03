import streamlit as st


# =========================================================
# Global Styles
# =========================================================

def load_styles():

    st.markdown(
        """
        <style>

        /* =================================================
           Main Page
           ================================================= */

        .main {
            padding-top: 2rem;
        }


        /* =================================================
           Sidebar
           ================================================= */

        .sidebar-title {
            text-align: center;
            font-size: 21px;
            font-weight: 700;
            padding: 10px 0 20px 0;
        }


        /* =================================================
           Conversation Title
           ================================================= */

        .conversation-title {
            font-size: 22px;
            font-weight: 600;
            padding: 15px 0;
            margin-bottom: 10px;
        }


        /* =================================================
           Chat Messages
           ================================================= */

        .stChatMessage {
            border-radius: 12px;
        }


        /* =================================================
           Buttons
           ================================================= */

        .stButton button {
            border-radius: 10px;
            min-height: 42px;
            font-weight: 600;
        }


        /* =================================================
           File Uploader
           ================================================= */

        [data-testid="stFileUploader"] {
            border-radius: 12px;
        }


        /* =================================================
           Chat Input
           ================================================= */

        [data-testid="stChatInput"] {
            border-radius: 12px;
        }


        /* =================================================
           Footer
           ================================================= */

        .footer {
            text-align: center;
            margin-top: 40px;
            padding: 15px;
            opacity: 0.65;
            font-size: 13px;
        }


        /* =================================================
           Success Messages
           ================================================= */

        .stAlert {
            border-radius: 10px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )