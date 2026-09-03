import streamlit as st
import lang_helper

from style import load_styles


# =========================================================
# Page Configuration
# =========================================================

def setup_page():

    st.set_page_config(
        page_title="PDF Summrizer AI Agent",
        page_icon="📚",
        layout="centered"
    )

    load_styles()


# =========================================================
# Header
# =========================================================

def show_header():

    username = st.session_state.get(
        "username",
        ""
    )

    st.title("📚 PDF Summrizer AI Agent")

    st.markdown(
        f"### Welcome, {username} 👋"
    )


# =========================================================
# Footer
# =========================================================

def show_footer():

    st.markdown(
        """
        <div class="footer">
           Devloper : Eng Mohanned Amer
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# Sidebar
# =========================================================

def show_sidebar():

    st.sidebar.markdown(
        """
        <div class="sidebar-title">
            📚 PDF Summrizer AI Agent
        </div>
        """,
        unsafe_allow_html=True
    )

    # =====================================================
    # User Information
    # =====================================================

    username = st.session_state.get(
        "username",
        ""
    )

    st.sidebar.markdown(
        f"👤 **{username}**"
    )

    st.sidebar.markdown("---")

    # =====================================================
    # Response Language
    # =====================================================

    st.sidebar.markdown(
        "### 🌐 Response Language"
    )

    response_language = st.sidebar.selectbox(
        "Choose language",
        (
            "Auto Detect",
            "Arabic",
            "English"
        ),
        label_visibility="collapsed"
    )

    st.sidebar.markdown("---")

    # =====================================================
    # New Conversation
    # =====================================================

    new_conversation = st.sidebar.button(
        "➕ New Conversation",
        use_container_width=True
    )

    st.sidebar.markdown("---")

    # =====================================================
    # Past Conversations
    # =====================================================

    st.sidebar.markdown(
        "### 💬 Past Conversations"
    )

    user_id = st.session_state.get(
        "user_id"
    )

    conversations = lang_helper.load_conversations(
        user_id
    )

    if not conversations:

        st.sidebar.info(
            "No past conversations yet."
        )

    else:

        for conversation_id, conversation in reversed(
            list(conversations.items())
        ):

            title = conversation.get(
                "title",
                "Untitled Conversation"
            )

            if st.sidebar.button(
                title,
                key=f"conversation_{conversation_id}",
                use_container_width=True
            ):

                st.session_state.selected_review = (
                    conversation
                )

                st.session_state.chat_history = (
                    conversation.get(
                        "messages",
                        []
                    )
                )

                st.session_state.conversation_id = (
                    conversation_id
                )

                st.rerun()

    # =====================================================
    # Logout
    # =====================================================

    st.sidebar.markdown("---")

    logout = st.sidebar.button(
        "🚪 Logout",
        use_container_width=True
    )

    return (
        response_language,
        new_conversation,
        logout
    )


# =========================================================
# PDF Upload Section
# =========================================================

def show_pdf_section(response_language):

    st.markdown(
        "## 📄 Study Material"
    )

    uploaded_file = st.file_uploader(
        "Upload your PDF",
        type=["pdf"],
        help="Upload a PDF file containing your study material."
    )

    if not uploaded_file:
        return None

    st.success(
        f"📄 {uploaded_file.name} uploaded successfully."
    )

    # =====================================================
    # Extract PDF Text
    # =====================================================

    if st.button(
        "📖 Read PDF",
        use_container_width=True
    ):

        with st.spinner(
            "📖 Reading PDF..."
        ):

            pdf_text = lang_helper.extract_pdf_text(
                uploaded_file
            )

        if pdf_text:

            st.session_state.pdf_text = pdf_text
            st.session_state.pdf_name = (
                uploaded_file.name
            )

            st.success(
                "PDF text extracted successfully."
            )

        else:

            st.error(
                "Could not extract text from this PDF."
            )

    # =====================================================
    # Use Previously Extracted PDF
    # =====================================================

    pdf_text = st.session_state.get(
        "pdf_text"
    )

    if not pdf_text:
        return None

    st.markdown("---")

    st.markdown(
        "### 🧠 What would you like to do?"
    )

    # =====================================================
    # Summary
    # =====================================================

    if st.button(
        "🧠 Summarize PDF",
        use_container_width=True
    ):

        with st.spinner(
            "🧠 Creating summary..."
        ):

            summary = lang_helper.summarize_pdf(
                pdf_text,
                response_language
            )

        st.session_state.last_result = summary
        st.session_state.result_type = "summary"

    # =====================================================
    # Quiz
    # =====================================================

    st.markdown(
        "### ❓ Generate Quiz"
    )

    number_of_questions = st.selectbox(
        "Number of questions",
        (
            5,
            10,
            15
        )
    )

    if st.button(
        "❓ Generate Questions",
        use_container_width=True
    ):

        with st.spinner(
            "🧠 Generating questions..."
        ):

            quiz = lang_helper.generate_quiz(
                pdf_text,
                number_of_questions,
                response_language
            )

        st.session_state.last_result = quiz
        st.session_state.result_type = "quiz"

    # =====================================================
    # Display Result
    # =====================================================

    result = st.session_state.get(
        "last_result"
    )

    result_type = st.session_state.get(
        "result_type"
    )

    if result:

        st.markdown("---")

        if result_type == "summary":

            st.markdown(
                "## 🧠 PDF Summary"
            )

        elif result_type == "quiz":

            st.markdown(
                "## ❓ Generated Quiz"
            )

        st.markdown(result)

    return pdf_text


# =========================================================
# Selected Previous Conversation
# =========================================================

def show_selected_review():

    selected_review = st.session_state.get(
        "selected_review"
    )

    if not selected_review:
        return

    title = selected_review.get(
        "title",
        "Previous Conversation"
    )

    st.markdown(
        f"""
        <div class="conversation-title">
            💬 {title}
        </div>
        """,
        unsafe_allow_html=True
    )

    messages = selected_review.get(
        "messages",
        []
    )

    for message in messages:

        role = message.get(
            "role"
        )

        content = message.get(
            "content",
            ""
        )

        if role == "user":

            with st.chat_message("user"):
                st.markdown(content)

        elif role == "assistant":

            with st.chat_message("assistant"):
                st.markdown(content)

    st.markdown("---")


# =========================================================
# Current Chat History
# =========================================================

def show_chat_history():

    history = st.session_state.get(
        "chat_history",
        []
    )

    if st.session_state.get(
        "selected_review"
    ):

        return

    for message in history:

        role = message.get(
            "role"
        )

        content = message.get(
            "content",
            ""
        )

        if role == "user":

            with st.chat_message("user"):
                st.markdown(content)

        elif role == "assistant":

            with st.chat_message("assistant"):
                st.markdown(content)


# =========================================================
# Chat Input
# =========================================================

def show_chat_input():

    user_input = st.chat_input(
        "💬 Ask me about your study material..."
    )

    return user_input


# =========================================================
# Main Study Interface
# =========================================================

def show_study_interface(response_language):

    show_pdf_section(
        response_language
    )