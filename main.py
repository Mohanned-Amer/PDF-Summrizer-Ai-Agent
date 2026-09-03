import streamlit as st
import lang_helper

from ui import (
    setup_page,
    show_header,
    show_sidebar,
    show_selected_review,
    show_chat_history,
    show_chat_input,
    show_study_interface
)


# =========================================================
# Page Setup
# =========================================================

setup_page()


# =========================================================
# Session State
# =========================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_id" not in st.session_state:
    st.session_state.user_id = None

if "username" not in st.session_state:
    st.session_state.username = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "conversation_id" not in st.session_state:
    st.session_state.conversation_id = None

if "selected_review" not in st.session_state:
    st.session_state.selected_review = None

if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = None

if "pdf_name" not in st.session_state:
    st.session_state.pdf_name = None

if "last_result" not in st.session_state:
    st.session_state.last_result = None

if "result_type" not in st.session_state:
    st.session_state.result_type = None


# =========================================================
# Restore Login After Refresh
# =========================================================

if not st.session_state.logged_in:

    session_token = st.query_params.get(
        "session"
    )

    if session_token:

        user_id = (
            lang_helper.login_with_session_token(
                session_token
            )
        )

        if user_id:

            username = (
                lang_helper.get_username(
                    user_id
                )
            )

            if username:

                st.session_state.logged_in = True
                st.session_state.user_id = user_id
                st.session_state.username = username


# =========================================================
# Login / Sign Up Page
# =========================================================

def show_login_page():

    # =====================================================
    # Login Page CSS
    # =====================================================

    st.markdown(
        """
        <style>

        /* Login page background */

        .stApp {
            background-color: #f5f7fb;
        }


        /* Main content width */

        .block-container {
            max-width: 1050px;
            padding-top: 45px;
            padding-bottom: 30px;
        }


        /* Hide sidebar on login */

        [data-testid="stSidebar"] {
            display: none;
        }


        /* Logo */

        .login-logo-box {
            text-align: center;
            font-size: 55px;
            margin-bottom: 5px;
        }


        /* Title */

        .login-main-title {
            text-align: center;
            font-size: 38px;
            font-weight: 800;
            margin-bottom: 4px;
        }


        /* Subtitle */

        .login-main-subtitle {
            text-align: center;
            color: #687386;
            font-size: 14px;
            margin-bottom: 35px;
        }


        /* Authentication card */

        .auth-title {
            font-size: 25px;
            font-weight: 750;
            margin-bottom: 3px;
        }


        .auth-description {
            color: #7b8494;
            font-size: 13px;
            margin-bottom: 20px;
        }


        /* Feature title */

        .feature-title {
            font-size: 22px;
            font-weight: 750;
            margin-bottom: 8px;
        }


        .feature-description {
            color: #687386;
            line-height: 1.7;
            font-size: 14px;
            margin-bottom: 20px;
        }


        /* Text inputs */

        div[data-testid="stTextInput"] input {

            height: 50px !important;

            border-radius: 10px !important;

            border: 1px solid #d9dee8 !important;

            background-color: #ffffff !important;

            padding-left: 15px !important;

            font-size: 14px !important;

        }


        div[data-testid="stTextInput"] input:focus {

            border-color: #6366f1 !important;

            box-shadow:
                0 0 0 1px #6366f1 !important;

        }


        /* Input labels */

        div[data-testid="stTextInput"] label {

            font-size: 13px !important;

            font-weight: 650 !important;

        }


        /* Buttons */

        div.stButton > button {

            height: 50px !important;

            border-radius: 10px !important;

            border: none !important;

            font-weight: 700 !important;

            font-size: 14px !important;

            margin-top: 8px;

        }


        div.stButton > button:hover {

            transform: translateY(-1px);

        }


        /* Tabs */

        div[data-baseweb="tab-list"] {

            gap: 0px;

            border-bottom: 1px solid #e2e6ed;

            margin-bottom: 25px;

        }


        button[data-baseweb="tab"] {

            font-weight: 650 !important;

            font-size: 14px !important;

        }


        /* Divider */

        .simple-line {

            height: 1px;

            background: #e3e7ee;

            margin: 25px 0;

        }


        /* Feature boxes */

        .feature-box {

            padding: 17px;

            background: #ffffff;

            border: 1px solid #e3e7ee;

            border-radius: 12px;

            margin-bottom: 12px;

        }


        .feature-box strong {

            font-size: 14px;

        }


        .feature-box span {

            display: block;

            color: #737d8e;

            font-size: 12px;

            margin-top: 5px;

            line-height: 1.5;

        }


        /* Footer */

        .login-footer {

            text-align: center;

            color: #929aaa;

            font-size: 11px;

            margin-top: 30px;

        }


        /* Mobile */

        @media (max-width: 700px) {

            .block-container {

                padding-top: 25px;

            }

            .login-main-title {

                font-size: 31px;

            }

            .feature-title {

                font-size: 20px;

            }

        }

        </style>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # Header
    # =====================================================

    st.markdown(
        '<div class="login-logo-box">📚</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="login-main-title">PDF summrizer and analyzer Ai Agent</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="login-main-subtitle">'
        'Your intelligent assistant for studying PDF materials'
        '</div>',
        unsafe_allow_html=True
    )


    # =====================================================
    # Two Main Columns
    # =====================================================

    info_column, auth_column = st.columns(
        [0.9, 1.1],
        gap="large"
    )


    # =====================================================
    # Information Column
    # =====================================================

    with info_column:

        st.markdown(
            '<div class="feature-title">'
            'Study in a smarter way 🧠'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="feature-description">'
            'Study AI helps you understand your PDF materials, '
            'summarize important information and ask questions '
            'about your study content.'
            '</div>',
            unsafe_allow_html=True
        )


        st.markdown(
            """
            <div class="feature-box">
                <strong>📄 PDF Summarization</strong>
                <span>
                    Convert long study materials into
                    understandable summaries.
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )


        st.markdown(
            """
            <div class="feature-box">
                <strong>💬 Ask Questions</strong>
                <span>
                    Ask your AI assistant about the
                    content of your study materials.
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )


        st.markdown(
            """
            <div class="feature-box">
                <strong>🎯 Focus on What Matters</strong>
                <span>
                    Find important concepts and make
                    your study sessions more efficient.
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )


    # =====================================================
    # Authentication Column
    # =====================================================

    with auth_column:

        login_tab, signup_tab = st.tabs(
            [
                "🔐 Login",
                "📝 Create Account"
            ]
        )


        # =================================================
        # Login
        # =================================================

        with login_tab:

            st.markdown(
                '<div class="auth-title">'
                'Welcome back'
                '</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<div class="auth-description">'
                'Enter your account information to continue.'
                '</div>',
                unsafe_allow_html=True
            )


            username = st.text_input(
                "Username",
                key="login_username",
                placeholder="Enter your username"
            )


            password = st.text_input(
                "Password",
                type="password",
                key="login_password",
                placeholder="Enter your password"
            )


            if st.button(
                "Login →",
                use_container_width=True,
                key="login_button"
            ):

                if (
                    not username.strip()
                    or not password
                ):

                    st.warning(
                        "Please Enter username and Password."
                    )

                else:

                    user_id, session_token = (
                        lang_helper.login_user(
                            username,
                            password
                        )
                    )

                    if user_id:

                        st.session_state.logged_in = True

                        st.session_state.user_id = user_id

                        st.session_state.username = (
                            lang_helper.get_username(
                                user_id
                            )
                        )

                        st.query_params[
                            "session"
                        ] = session_token

                        st.rerun()

                    else:

                        st.error(
                            "Invalid Username or Password."
                        )


        # =================================================
        # Sign Up
        # =================================================

        with signup_tab:

            st.markdown(
                '<div class="auth-title">'
                'Create your account'
                '</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<div class="auth-description">'
                'Create an account to start using Study AI.'
                '</div>',
                unsafe_allow_html=True
            )


            new_username = st.text_input(
                "Username",
                key="signup_username",
                placeholder="Choose a username"
            )


            new_password = st.text_input(
                "Password",
                type="password",
                key="signup_password",
                placeholder="Create a password"
            )


            confirm_password = st.text_input(
                "Confirm Password",
                type="password",
                key="signup_confirm_password",
                placeholder="Repeat your password"
            )


            if st.button(
                "Create Account →",
                use_container_width=True,
                key="signup_button"
            ):

                if (
                    not new_username.strip()
                    or not new_password
                    or not confirm_password
                ):

                    st.warning(
                        "Please fill in all fields."
                    )

                elif new_password != confirm_password:

                    st.error(
                        "Passwords do not match."
                    )

                elif lang_helper.username_exists(
                    new_username
                ):

                    st.error(
                        "Username already exists."
                    )

                else:

                    created = (
                        lang_helper.create_user(
                            new_username,
                            new_password
                        )
                    )

                    if created:

                        st.success(
                            "Account created successfully! "
                            "You can now login."
                        )

                    else:

                        st.error(
                            "Could not create the account."
                        )


    # =====================================================
    # Footer
    # =====================================================

    st.markdown(
        '<div class="login-footer">'
        'Study AI • Learn • Understand • Succeed'
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# Authentication Check
# =========================================================

if not st.session_state.logged_in:

    show_login_page()

    st.stop()


# =========================================================
# Header
# =========================================================

show_header()


# =========================================================
# Sidebar
# =========================================================

response_language, new_conversation, logout = (
    show_sidebar()
)


# =========================================================
# Logout
# =========================================================

if logout:

    lang_helper.logout_user(
        st.session_state.user_id
    )

    st.query_params.clear()

    st.session_state.logged_in = False
    st.session_state.user_id = None
    st.session_state.username = None

    st.session_state.chat_history = []
    st.session_state.conversation_id = None
    st.session_state.selected_review = None

    st.session_state.pdf_text = None
    st.session_state.pdf_name = None
    st.session_state.last_result = None
    st.session_state.result_type = None

    st.rerun()


# =========================================================
# New Conversation
# =========================================================

if new_conversation:

    st.session_state.chat_history = []
    st.session_state.conversation_id = None
    st.session_state.selected_review = None

    st.session_state.pdf_text = None
    st.session_state.pdf_name = None
    st.session_state.last_result = None
    st.session_state.result_type = None

    st.rerun()


# =========================================================
# Previous Conversation
# =========================================================

show_selected_review()


# =========================================================
# Current Chat History
# =========================================================

show_chat_history()


# =========================================================
# Study AI Interface
# =========================================================

show_study_interface(
    response_language
)


# =========================================================
# Chat Input
# =========================================================

user_input = show_chat_input()


# =========================================================
# Process User Message
# =========================================================

if user_input:

    # -----------------------------------------------------
    # Add User Message
    # -----------------------------------------------------

    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": user_input
        }
    )


    # -----------------------------------------------------
    # Display User Message
    # -----------------------------------------------------

    with st.chat_message("user"):

        st.markdown(
            user_input
        )


    # -----------------------------------------------------
    # Generate AI Response
    # -----------------------------------------------------

    with st.chat_message("assistant"):

        with st.spinner(
            "🧠 Study AI is thinking..."
        ):

            response = (
                lang_helper.study_agent(
                    user_input,
                    st.session_state.get(
                        "pdf_text"
                    ),
                    response_language
                )
            )

        st.markdown(
            response
        )


    # -----------------------------------------------------
    # Add AI Response
    # -----------------------------------------------------

    st.session_state.chat_history.append(
        {
            "role": "assistant",
            "content": response
        }
    )


    # -----------------------------------------------------
    # Save Conversation
    # -----------------------------------------------------

    st.session_state.conversation_id = (
        lang_helper.save_conversation(
            st.session_state.user_id,
            st.session_state.conversation_id,
            st.session_state.chat_history
        )
    )
