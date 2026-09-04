import streamlit as st

# =========================================================
# Global Styles
# =========================================================

def load_styles():

    st.markdown(
        """
        <style>

        /* =================================================
           Main Application
           ================================================= */

        .main {
            padding-top: 1rem;
        }

        .block-container {
            max-width: 900px;
            padding-top: 2rem;
            padding-bottom: 4rem;
        }

        /* =================================================
           Header
           ================================================= */

        .app-header {
            display: flex;
            align-items: center;
            gap: 18px;
            padding: 22px 24px;
            margin-bottom: 18px;
            border-radius: 20px;
            background: linear-gradient(
                135deg,
                #eef4ff 0%,
                #f8fbff 100%
            );
            border: 1px solid #dce7f7;
        }

        .header-icon {
            width: 58px;
            height: 58px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 16px;
            background: #ffffff;
            font-size: 30px;
            box-shadow: 0 5px 18px rgba(30, 64, 175, 0.10);
        }

        .header-title {
            font-size: 28px;
            font-weight: 800;
            color: #172554;
            line-height: 1.2;
        }

        .header-subtitle {
            margin-top: 5px;
            font-size: 14px;
            color: #64748b;
            letter-spacing: 0.3px;
        }

        /* =================================================
           Welcome Card
           ================================================= */

        .welcome-card {
            display: flex;
            align-items: center;
            gap: 14px;
            padding: 16px 20px;
            margin-bottom: 28px;
            border-radius: 16px;
            background: #ffffff;
            border: 1px solid #e5e7eb;
            box-shadow: 0 4px 16px rgba(15, 23, 42, 0.04);
        }

        .welcome-icon {
            font-size: 25px;
        }

        .welcome-title {
            font-size: 16px;
            font-weight: 700;
            color: #1e293b;
        }

        .welcome-text {
            margin-top: 3px;
            font-size: 13px;
            color: #64748b;
        }

        /* =================================================
           Section Heading
           ================================================= */

        .section-heading {
            display: flex;
            align-items: center;
            gap: 14px;
            margin: 15px 0 18px 0;
        }

        .section-icon {
            width: 48px;
            height: 48px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 14px;
            background: #eff6ff;
            font-size: 24px;
        }

        .section-title {
            font-size: 22px;
            font-weight: 800;
            color: #1e293b;
        }

        .section-description {
            margin-top: 3px;
            font-size: 13px;
            color: #64748b;
        }

        /* =================================================
           File Uploader
           ================================================= */

        [data-testid="stFileUploader"] {
            padding: 8px;
            border-radius: 18px;
            background: #ffffff;
        }

        [data-testid="stFileUploaderDropzone"] {
            border: 2px dashed #bfdbfe !important;
            border-radius: 16px !important;
            background: #f8fbff !important;
            transition: 0.2s ease;
        }

        [data-testid="stFileUploaderDropzone"]:hover {
            border-color: #60a5fa !important;
            background: #eff6ff !important;
        }

        .upload-hint {
            display: flex;
            justify-content: center;
            gap: 7px;
            margin-top: -8px;
            margin-bottom: 20px;
            font-size: 12px;
            color: #64748b;
        }

        /* =================================================
           Uploaded File Card
           ================================================= */

        .file-card {
            display: flex;
            align-items: center;
            gap: 15px;
            padding: 16px;
            margin: 15px 0 18px 0;
            border-radius: 16px;
            background: #f8fafc;
            border: 1px solid #e2e8f0;
        }

        .file-icon {
            width: 48px;
            height: 48px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 13px;
            background: #fee2e2;
            font-size: 24px;
        }

        .file-name {
            font-weight: 700;
            color: #1e293b;
            word-break: break-word;
        }

        .file-status {
            margin-top: 4px;
            font-size: 12px;
            color: #16a34a;
        }

        /* =================================================
           Action Heading
           ================================================= */

        .action-heading {
            display: flex;
            align-items: center;
            gap: 13px;
            margin: 28px 0 20px 0;
            padding-top: 25px;
            border-top: 1px solid #e5e7eb;
        }

        .action-heading-icon {
            font-size: 25px;
        }

        .action-title {
            font-size: 19px;
            font-weight: 800;
            color: #1e293b;
        }

        .action-description {
            margin-top: 3px;
            font-size: 13px;
            color: #64748b;
        }

        /* =================================================
           Tool Labels
           ================================================= */

        .tool-label {
            margin-top: 15px;
            margin-bottom: 2px;
            font-size: 16px;
            font-weight: 750;
            color: #1e293b;
        }

        .quiz-label {
            margin-top: 28px;
        }

        /* =================================================
           Buttons
           ================================================= */

        .stButton > button {
            min-height: 44px;
            border-radius: 12px;
            border: 1px solid #dbeafe;
            font-weight: 700;
            transition: all 0.2s ease;
        }

        .stButton > button:hover {
            transform: translateY(-1px);
            box-shadow: 0 5px 15px rgba(30, 64, 175, 0.10);
        }

        /* =================================================
           Select Boxes
           ================================================= */

        div[data-baseweb="select"] > div {
            border-radius: 11px !important;
        }

        /* =================================================
           Result Header
           ================================================= */

        .result-header {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-top: 32px;
            margin-bottom: 12px;
            padding: 14px 16px;
            border-radius: 14px;
            background: #f1f5f9;
            border: 1px solid #e2e8f0;
            font-size: 18px;
            font-weight: 800;
            color: #1e293b;
        }

        .result-icon {
            font-size: 22px;
        }

        /* =================================================
           Result Card
           ================================================= */

        .result-card {
            padding: 22px;
            margin-bottom: 25px;
            border-radius: 16px;
            background: #ffffff;
            border: 1px solid #e2e8f0;
            box-shadow: 0 5px 20px rgba(15, 23, 42, 0.05);
            color: #334155;
            line-height: 1.8;
        }

        /* =================================================
           Chat Messages
           ================================================= */

        [data-testid="stChatMessage"] {
            border-radius: 16px;
            margin-bottom: 10px;
        }

        /* =================================================
           Chat Input
           ================================================= */

        [data-testid="stChatInput"] {
            border-radius: 15px;
        }

        [data-testid="stChatInput"] textarea {
            border-radius: 14px;
        }

        /* =================================================
           Conversation Header
           ================================================= */

        .conversation-header {
            display: flex;
            align-items: center;
            gap: 13px;
            padding: 15px 18px;
            margin: 10px 0 22px 0;
            border-radius: 15px;
            background: #f8fafc;
            border: 1px solid #e2e8f0;
        }

        .conversation-icon {
            font-size: 25px;
        }

        .conversation-heading {
            font-size: 17px;
            font-weight: 750;
            color: #1e293b;
        }

        .conversation-subtitle {
            margin-top: 3px;
            font-size: 12px;
            color: #64748b;
        }

        .section-divider {
            height: 1px;
            margin: 25px 0;
            background: #e2e8f0;
        }

        /* =================================================
           Sidebar
           ================================================= */

        [data-testid="stSidebar"] {
            border-right: 1px solid #e5e7eb;
        }

        .sidebar-brand {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 8px 4px 20px 4px;
        }

        .sidebar-logo {
            width: 44px;
            height: 44px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 13px;
            background: #eff6ff;
            font-size: 23px;
        }

        .sidebar-brand-title {
            font-size: 17px;
            font-weight: 800;
            color: #1e293b;
        }

        .sidebar-brand-subtitle {
            margin-top: 2px;
            font-size: 11px;
            color: #64748b;
        }

        .sidebar-section-title {
            margin: 7px 0 10px 0;
            font-size: 13px;
            font-weight: 750;
            color: #475569;
        }

        .sidebar-divider {
            height: 1px;
            margin: 17px 0;
            background: #e5e7eb;
        }

        .sidebar-bottom-divider {
            height: 1px;
            margin: 25px 0 15px 0;
            background: #e5e7eb;
        }

        /* =================================================
           User Card
           ================================================= */

        .user-card {
            display: flex;
            align-items: center;
            gap: 11px;
            padding: 11px;
            border-radius: 13px;
            background: #f8fafc;
            border: 1px solid #e2e8f0;
        }

        .user-avatar {
            width: 36px;
            height: 36px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 10px;
            background: #ffffff;
            font-size: 18px;
        }

        .user-label {
            font-size: 10px;
            color: #94a3b8;
        }

        .user-name {
            margin-top: 2px;
            font-size: 13px;
            font-weight: 700;
            color: #334155;
        }

        /* =================================================
           Empty Conversations
           ================================================= */

        .empty-conversations {
            padding: 20px 10px;
            text-align: center;
            border-radius: 14px;
            background: #f8fafc;
            border: 1px dashed #cbd5e1;
        }

        .empty-icon {
            font-size: 25px;
            margin-bottom: 6px;
        }

        .empty-title {
            font-size: 12px;
            font-weight: 700;
            color: #475569;
        }

        .empty-text {
            margin-top: 4px;
            font-size: 10px;
            line-height: 1.5;
            color: #94a3b8;
        }

        /* =================================================
           Sidebar Buttons
           ================================================= */

        [data-testid="stSidebar"] .stButton > button {
            min-height: 40px;
            border-radius: 10px;
            text-align: left;
            font-size: 13px;
        }

        /* =================================================
           Alerts
           ================================================= */

        .stAlert {
            border-radius: 12px;
        }

        /* =================================================
           Footer
           ================================================= */

        .footer {
            text-align: center;
            margin-top: 50px;
            padding: 25px 10px 10px 10px;
        }

        .footer-line {
            height: 1px;
            margin-bottom: 18px;
            background: #e2e8f0;
        }

        .footer-text {
            font-size: 13px;
            font-weight: 700;
            color: #64748b;
        }

        .footer-author {
            margin-top: 5px;
            font-size: 11px;
            color: #94a3b8;
        }

        /* =================================================
           Responsive
           ================================================= */

        @media (max-width: 700px) {

            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }

            .app-header {
                padding: 18px;
                border-radius: 16px;
            }

            .header-title {
                font-size: 22px;
            }

            .header-icon {
                width: 48px;
                height: 48px;
                font-size: 25px;
            }

            .welcome-card {
                padding: 13px;
            }

            .section-title {
                font-size: 19px;
            }

            .result-card {
                padding: 17px;
            }

        }

        </style>
        """,
        unsafe_allow_html=True
    )
