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

    st.title(
        "📚 PDF Summrizer AI Agent"
    )

    st.caption(
        "Your AI assistant for studying and understanding PDF materials."
    )

    # =====================================================
    # Login / Sign Up Tabs
    # =====================================================

    login_tab, signup_tab = st.tabs(
        [
            "🔑 Login",
            "📝 Sign Up"
        ]
        
        
        
    )


    # =====================================================
    # Login Tab
    # =====================================================

    with login_tab:

        st.subheader(
            "Welcome Back 👋"
        )

        username = st.text_input(
            "Username",
            key="login_username"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_password"
        )

        if st.button(
            "Login",
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


    # =====================================================
    # Sign Up Tab
    # =====================================================

    with signup_tab:

        st.subheader(
            "Create Your Account 🚀"
        )

        new_username = st.text_input(
            "Username",
            key="signup_username"
        )

        new_password = st.text_input(
            "Password",
            type="password",
            key="signup_password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password",
            key="signup_confirm_password"
        )

        if st.button(
            "Create Account",
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