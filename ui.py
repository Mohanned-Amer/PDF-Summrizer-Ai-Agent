import streamlit as st
import lang_helper

from style import load_styles

# =========================================================
# Page Configuration
# =========================================================

def setup_page():

    st.set_page_config(
        page_title="PDF Summarizer AI",
        page_icon="📄",
        layout="centered",
        initial_sidebar_state="expanded"
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

    st.markdown(
        """
        <div class="app-header">
            <div class="header-icon">📄</div>
            <div class="header-content">
                <div class="header-title">
                    PDF Summarizer AI
                </div>
                <div class="header-subtitle">
                    Read • Summarize • Learn
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if username:

        st.markdown(
            f"""
            <div class="welcome-card">
                <div class="welcome-icon">👋</div>
                <div>
                    <div class="welcome-title">
                        Welcome back, {username}
                    </div>
                    <div class="welcome-text">
                        Upload your PDF and let AI help you understand it.
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================================================
# Footer
# =========================================================

def show_footer():

    st.markdown(
        """
        <div class="footer">
            <div class="footer-line"></div>
            <div class="footer-text">
                PDF Summarizer AI
            </div>
            <div class="footer-author">
                Developed by Eng Mohanned Amer
            </div>
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
        <div class="sidebar-brand">
            <div class="sidebar-logo">📄</div>
            <div>
                <div class="sidebar-brand-title">
                    PDF Summarizer
                </div>
                <div class="sidebar-brand-subtitle">
                    AI Learning Assistant
                </div>
            </div>
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
        f"""
        <div class="user-card">
            <div class="user-avatar">👤</div>
            <div>
                <div class="user-label">Signed in as</div>
                <div class="user-name">{username}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.markdown(
        '<div class="sidebar-divider"></div>',
        unsafe_allow_html=True
    )

    # =====================================================
    # Response Language
    # =====================================================

    st.sidebar.markdown(
        """
        <div class="sidebar-section-title">
            🌐 Response Language
        </div>
        """,
        unsafe_allow_html=True
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

    st.sidebar.markdown(
        '<div class="sidebar-divider"></div>',
        unsafe_allow_html=True
    )

    # =====================================================
    # New Conversation
    # =====================================================

    new_conversation = st.sidebar.button(
        "＋  New Conversation",
        use_container_width=True
    )

    st.sidebar.markdown(
        '<div class="sidebar-divider"></div>',
        unsafe_allow_html=True
    )

    # =====================================================
    # Past Conversations
    # =====================================================

    st.sidebar.markdown(
        """
        <div class="sidebar-section-title">
            💬 Recent Conversations
        </div>
        """,
        unsafe_allow_html=True
    )

    user_id = st.session_state.get(
        "user_id"
    )

    conversations = lang_helper.load_conversations(
        user_id
    )

    if not conversations:

        st.sidebar.markdown(
            """
            <div class="empty-conversations">
                <div class="empty-icon">💭</div>
                <div class="empty-title">
                    No conversations yet
                </div>
                <div class="empty-text">
                    Start asking questions about your PDF.
                </div>
            </div>
            """,
            unsafe_allow_html=True
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
                f"💬  {title}",
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

    st.sidebar.markdown(
        '<div class="sidebar-bottom-divider"></div>',
        unsafe_allow_html=True
    )

    logout = st.sidebar.button(
        "↪  Logout",
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
        """
        <div class="section-heading">
            <div class="section-icon">📄</div>
            <div>
                <div class="section-title">
                    Study Material
                </div>
                <div class="section-description">
                    Upload a PDF and turn it into useful study content.
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader(
        "Upload your PDF",
        type=["pdf"],
        help="Upload a PDF file containing your study material."
    )

    if not uploaded_file:

        st.markdown(
            """
            <div class="upload-hint">
                <span>📎</span>
                <span>
                    Supported format: PDF
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )

        return None

    # =====================================================
    # Uploaded File Card
    # =====================================================

    st.markdown(
        f"""
        <div class="file-card">
            <div class="file-icon">📕</div>
            <div class="file-details">
                <div class="file-name">
                    {uploaded_file.name}
                </div>
                <div class="file-status">
                    ✓ PDF ready to process
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # =====================================================
    # Extract PDF Text
    # =====================================================

    if st.button(
        "📖  Read PDF",
        use_container_width=True
    ):

        with st.spinner(
            "Reading your PDF..."
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

    # =====================================================
    # Actions
    # =====================================================

    st.markdown(
        """
        <div class="action-heading">
            <div class="action-heading-icon">✨</div>
            <div>
                <div class="action-title">
                    What would you like to do?
                </div>
                <div class="action-description">
                    Choose an AI tool for your study material.
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # =====================================================
    # Summary
    # =====================================================

    st.markdown(
        """
        <div class="tool-label">
            🧠 Summarize
        </div>
        """,
        unsafe_allow_html=True
    )

    st.caption(
        "Create a clear and useful summary from your PDF."
    )

    if st.button(
        "Create PDF Summary",
        use_container_width=True
    ):

        with st.spinner(
            "Creating your summary..."
        ):

            summary = lang_helper.summarize_pdf(
                pdf_text,
                response_language
            )

        st.session_state.last_result = summary

        st.session_state.result_type = (
            "summary"
        )

    # =====================================================
    # Quiz
    # =====================================================

    st.markdown(
        """
        <div class="tool-label quiz-label">
            ❓ Generate Quiz
        </div>
        """,
        unsafe_allow_html=True
    )

    st.caption(
        "Generate questions to test your understanding."
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
        "Generate Questions",
        use_container_width=True
    ):

        with st.spinner(
            "Generating questions..."
        ):

            quiz = lang_helper.generate_quiz(
                pdf_text,
                number_of_questions,
                response_language
            )

        st.session_state.last_result = quiz

        st.session_state.result_type = (
            "quiz"
        )

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

        if result_type == "summary":

            st.markdown(
                """
                <div class="result-header">
                    <span class="result-icon">🧠</span>
                    <span>PDF Summary</span>
                </div>
                """,
                unsafe_allow_html=True
            )

        elif result_type == "quiz":

            st.markdown(
                """
                <div class="result-header">
                    <span class="result-icon">❓</span>
                    <span>Generated Quiz</span>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown(
            f"""
            <div class="result-card">
                {result}
            </div>
            """,
            unsafe_allow_html=True
        )

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
        <div class="conversation-header">
            <div class="conversation-icon">💬</div>
            <div>
                <div class="conversation-heading">
                    {title}
                </div>
                <div class="conversation-subtitle">
                    Previous conversation
                </div>
            </div>
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

            with st.chat_message(
                "user"
            ):

                st.markdown(
                    content
                )

        elif role == "assistant":

            with st.chat_message(
                "assistant"
            ):

                st.markdown(
                    content
                )

    st.markdown(
        '<div class="section-divider"></div>',
        unsafe_allow_html=True
    )

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

            with st.chat_message(
                "user"
            ):

                st.markdown(
                    content
                )

        elif role == "assistant":

            with st.chat_message(
                "assistant"
            ):

                st.markdown(
                    content
                )

# =========================================================
# Chat Input
# =========================================================

def show_chat_input():

    user_input = st.chat_input(
        "Ask anything about your study material..."
    )

    return user_input

# =========================================================
# Main Study Interface
# =========================================================

def show_study_interface(response_language):

    show_pdf_section(
        response_language
    )
