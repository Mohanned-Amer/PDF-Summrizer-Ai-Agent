import streamlit as st
import LogicPage

from UiPage import (
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
    st.session_state.logged_in = True

if "user_id" not in st.session_state:
    st.session_state.user_id = "local_user"

if "username" not in st.session_state:
    st.session_state.username = "User"

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
# Login has been removed.
# This button is intentionally ignored.

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
            "🧠 أنا أفكر الآن ..."
        ):

            response = (
                LogicPage.study_agent(
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
        LogicPage.save_conversation(
            st.session_state.user_id,
            st.session_state.conversation_id,
            st.session_state.chat_history
        )
    )
