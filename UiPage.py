import streamlit as st
import LogicPage

from StylePage import load_styles

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

    st.html("""
        <div class="app-header">
            <div class="header-icon">📄</div>

            <div class="header-content">
                <div class="header-title">
                    وكيل تلخيص وتحليل الملفات
                </div>

                <div class="header-subtitle">
                    قراءة - تحليل - تلخيص
                </div>
            </div>
        </div>
    """)

    st.html("""
        <div class="welcome-card">

            <div class="welcome-icon">
                👋
            </div>

            <div>
                <div class="welcome-title">
                    أهلاً بك
                </div>

                <div class="welcome-text">
                    قم بتحميل الملف واستمتع بأفضل الملخصات.
                </div>
            </div>

        </div>
    """)

# =========================================================
# Footer
# =========================================================

def show_footer():

    st.html("""
        <div class="footer">

            <div class="footer-line"></div>

            <div class="footer-text">
                PDF Summarizer AI
            </div>

            <div class="footer-author">
                Developed by Eng Mohanned Amer
            </div>

        </div>
    """)

# =========================================================
# Sidebar
# =========================================================

def show_sidebar():

    # -----------------------------------------------------
    # Brand
    # -----------------------------------------------------

    st.sidebar.html("""
        <div class="sidebar-brand">

            <div class="sidebar-logo">
                📄
            </div>

            <div>

                <div class="sidebar-brand-title">
                    محلل الملفات
                </div>

                <div class="sidebar-brand-subtitle">
                    مساعد ذكاء اصطناعي
                </div>

            </div>

        </div>
    """)

    # -----------------------------------------------------
    # Language
    # -----------------------------------------------------

    st.sidebar.html("""
        <div class="sidebar-section-title">
            🌐 تحويل اللغة
        </div>
    """)

    response_language = st.sidebar.selectbox(
        "Choose language",
        (
            "اللغة الافتراضية",
            "العربية",
            "الانجليزية"
        ),
        label_visibility="collapsed"
    )

    st.sidebar.html("""
        <div class="sidebar-divider"></div>
    """)

    # -----------------------------------------------------
    # New Conversation
    # -----------------------------------------------------

    new_conversation = st.sidebar.button(
        "＋  محادثة جديدة",
        use_container_width=True
    )

    st.sidebar.html("""
        <div class="sidebar-divider"></div>
    """)

    # -----------------------------------------------------
    # Previous Conversations
    # -----------------------------------------------------

    st.sidebar.html("""
        <div class="sidebar-section-title">
            💬 المحادثات السابقة
        </div>
    """)

    conversations = LogicPage.load_conversations(
        "local_user"
    )

    # -----------------------------------------------------
    # No Conversations
    # -----------------------------------------------------

    if not conversations:

        st.sidebar.html("""
            <div class="empty-conversations">

                <div class="empty-icon">
                    💭
                </div>

                <div class="empty-title">
                    لا توجد محادثات بعد
                </div>

                <div class="empty-text">
                    ابدأ بطرح الأسئلة عن محتوى الملف
                </div>

            </div>
        """)

    # -----------------------------------------------------
    # Existing Conversations
    # -----------------------------------------------------

    else:

        for conversation_id, conversation in reversed(
            list(conversations.items())
        ):

            title = conversation.get(
                "title",
                "محادثة بدون عنوان"
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

    return (
        response_language,
        new_conversation,
        False
    )

# =========================================================
# PDF Section
# =========================================================

def show_pdf_section(response_language):

    # -----------------------------------------------------
    # Heading
    # -----------------------------------------------------

    st.html("""
        <div class="section-heading">

            <div class="section-icon">
                📄
            </div>

            <div>

                <div class="section-title">
                    استمتع بأفضل الملخصات
                </div>

                <div class="section-description">
                    قم بتحميل ملفك وحوله إلى معلومات مفيدة
                </div>

            </div>

        </div>
    """)

    # -----------------------------------------------------
    # Upload
    # -----------------------------------------------------

    uploaded_file = st.file_uploader(
        "تحميل الملف",
        type=["pdf"],
        help="Upload a PDF file containing your study material."
    )

    if not uploaded_file:

        st.html("""
            <div class="upload-hint">

                <span>
                    📎
                </span>

                <span>
                    يدعم تنسيق PDF
                </span>

            </div>
        """)

        return None

    # -----------------------------------------------------
    # File Card
    # -----------------------------------------------------

    st.html(f"""
        <div class="file-card">

            <div class="file-icon">
                📕
            </div>

            <div class="file-details">

                <div class="file-name">
                    {uploaded_file.name}
                </div>

                <div class="file-status">
                    ✓ الملف جاهز للمعالجة
                </div>

            </div>

        </div>
    """)

    # -----------------------------------------------------
    # Read PDF
    # -----------------------------------------------------

    if st.button(
        "📖  قراءة الملف",
        use_container_width=True
    ):

        with st.spinner(
            "يتم قراءة الملف..."
        ):

            pdf_text = LogicPage.extract_pdf_text(
                uploaded_file
            )

        if pdf_text:

            st.session_state.pdf_text = pdf_text

            st.session_state.pdf_name = (
                uploaded_file.name
            )

            st.success(
                "تم قراءة النص بنجاح."
            )

        else:

            st.error(
                "فشل في قراءة النص"
            )

    # -----------------------------------------------------
    # Get PDF Text
    # -----------------------------------------------------

    pdf_text = st.session_state.get(
        "pdf_text"
    )

    if not pdf_text:

        return None

    # -----------------------------------------------------
    # Actions
    # -----------------------------------------------------

    st.html("""
        <div class="action-heading">

            <div class="action-heading-icon">
                ✨
            </div>

            <div>

                <div class="action-title">
                    ما الذي تريد القيام به؟
                </div>

                <div class="action-description">
                    قم باختيار أداة.
                </div>

            </div>

        </div>
    """)

    # =====================================================
    # Summary
    # =====================================================

    st.html("""
        <div class="tool-label">
            🧠 تلخيص
        </div>
    """)

    st.caption(
        "يتم إنشاء ملخص مفيد لمحتوى الملف"
    )

    if st.button(
        "إنشاء ملخص للملف",
        use_container_width=True
    ):

        with st.spinner(
            "يتم إنشاء الملخص..."
        ):

            summary = LogicPage.summarize_pdf(
                pdf_text,
                response_language
            )

        st.session_state.last_result = summary

        st.session_state.result_type = (
            "تلخيص"
        )

    # =====================================================
    # Quiz
    # =====================================================

    st.html("""
        <div class="tool-label quiz-label">
            ❓ إنشاء أسئلة
        </div>
    """)

    st.caption(
        "يتم إنشاء أسئلة لاختبار فهمك"
    )

    number_of_questions = st.selectbox(
        "عدد الأسئلة",
        (
            5,
            10,
            15
        )
    )

    if st.button(
        "إنشاء أسئلة",
        use_container_width=True
    ):

        with st.spinner(
            "يتم إنشاء الأسئلة..."
        ):

            quiz = LogicPage.generate_quiz(
                pdf_text,
                number_of_questions,
                response_language
            )

        st.session_state.last_result = quiz

        st.session_state.result_type = (
            "اختبار"
        )

    # =====================================================
    # Result
    # =====================================================

    result = st.session_state.get(
        "last_result"
    )

    result_type = st.session_state.get(
        "result_type"
    )

    if result:

        if result_type == "تلخيص":

            st.html("""
                <div class="result-header">

                    <span class="result-icon">
                        🧠
                    </span>

                    <span>
                        ملخص الملف
                    </span>

                </div>
            """)

        elif result_type == "اختبار":

            st.html("""
                <div class="result-header">

                    <span class="result-icon">
                        ❓
                    </span>

                    <span>
                        الأسئلة المستخرجة
                    </span>

                </div>
            """)

        # نتيجة الذكاء الاصطناعي
        st.markdown(
            result
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
        "المحادثات السابقة"
    )

    st.html(f"""
        <div class="conversation-header">

            <div class="conversation-icon">
                💬
            </div>

            <div>

                <div class="conversation-heading">
                    {title}
                </div>

                <div class="conversation-subtitle">
                    المحادثات السابقة
                </div>

            </div>

        </div>
    """)

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

                st.markdown(
                    content
                )

        elif role == "assistant":

            with st.chat_message("assistant"):

                st.markdown(
                    content
                )

    st.html("""
        <div class="section-divider"></div>
    """)

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

                st.markdown(
                    content
                )

        elif role == "assistant":

            with st.chat_message("assistant"):

                st.markdown(
                    content
                )

# =========================================================
# Chat Input
# =========================================================

def show_chat_input():

    return st.chat_input(
        "اسأل أي شيء"
    )

# =========================================================
# Main Study Interface
# =========================================================

def show_study_interface(
    response_language
):

    show_pdf_section(
        response_language
    )
