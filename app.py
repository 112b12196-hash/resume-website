import streamlit as st

from pathlib import Path
from PIL import Image
import os

# -----------------------------
# 基本設定
# -----------------------------
st.set_page_config(
    page_title="黃紫薇｜個人履歷",
    page_icon="📄",
    layout="wide"
)

# -----------------------------
# 載入CSS
# -----------------------------
def load_css():
    if Path("style.css").exists():
        with open("style.css", encoding="utf-8") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

load_css()

# -----------------------------
# Header
# -----------------------------
st.markdown("""
<div class="top-banner">
    <h1>黃紫薇</h1>
    <h3>Chang Jung Christian University｜企業履歷 Resume</h3>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    if Path("profile.jpg").exists():
        st.image("profile.jpg", use_container_width=True)

    st.markdown("## 個人資訊")

    st.write("🎓 長榮大學")
    st.write("✈️ 航管系")
    st.write("📍 台北大安區浦城街")
    st.write("🌏 中文 / English")

    st.divider()

    st.markdown("## 求職方向")

    st.info("""
航空業實習  
航空公司行政  
營運管理  
客服管理  
物流與供應鏈  
""")

    st.divider()

    st.markdown("## 核心能力")

    st.progress(90, text="溝通協調")
    st.progress(88, text="團隊合作")
    st.progress(85, text="文書處理")
    st.progress(60, text="英文能力")
    st.progress(82, text="專案管理")

# -----------------------------
# 自我介紹
# -----------------------------

col1, col2 = st.columns([2,3])

with col1:

    st.markdown("""
## 個人簡介
""")

    st.write("""
目前就讀於長榮大學，具備航空管理相關背景，
對航空產業、服務管理及物流供應鏈具有濃厚興趣。

除了課堂學習之外，也積極參與校內外活動，
培養團隊合作、溝通協調及問題解決能力，
希望未來能投入航空公司或大型企業，
持續提升專業能力並創造價值。
""")

with col2:

    st.markdown("""
## 個人特色
""")

    st.success("✔ 積極主動")
    st.success("✔ 具責任感")
    st.success("✔ 團隊合作能力佳")
    st.success("✔ 快速學習能力")
    st.success("✔ 抗壓性良好")

# -----------------------------
# 分隔
# -----------------------------
st.markdown("---")
# ==========================================================
# 學歷背景
# ==========================================================

st.markdown("## 🎓 學歷背景")

st.markdown("""
<div class="resume-card">

### 長榮大學（Chang Jung Christian University）

**科系：** 航運管理學系

**在學期間：** 就讀中

在校期間修習航空管理、物流管理、供應鏈管理、航空運輸、服務品質、
行銷管理等相關課程，並透過專題與團隊合作培養分析能力與實務經驗。

</div>
""", unsafe_allow_html=True)

st.markdown("---")


# ==========================================================
# 專業技能
# ==========================================================

st.markdown("## 💼 專業技能")

col1, col2 = st.columns(2)

with col1:

    st.markdown("### 文書與資訊能力")

    st.write("Microsoft Word")
    st.progress(95)

    st.write("Microsoft PowerPoint")
    st.progress(92)

    st.write("Microsoft Excel")
    st.progress(60)

    st.write("Google Workspace")
    st.progress(90)

    st.write("Canva")
    st.progress(88)

with col2:

    st.markdown("### 專業能力")

    st.write("團隊合作")
    st.progress(95)

    st.write("溝通協調")
    st.progress(92)

    st.write("問題分析")
    st.progress(85)

    st.write("專案執行")
    st.progress(83)

    st.write("服務管理")
    st.progress(90)

st.markdown("---")


# ==========================================================
# 語言能力
# ==========================================================

st.markdown("## 🌏 語言能力")

language_col1, language_col2 = st.columns(2)

with language_col1:

    st.metric(
        label="中文",
        value="母語"
    )

    st.metric(
        label="英文",
        value="基本溝通能力"
    )

with language_col2:

    st.info("""
具備閱讀英文文件能力，
可進行日常溝通及基礎商務交流，
持續精進英文能力中。
""")


st.markdown("---")


# ==========================================================
# 專長整理
# ==========================================================

st.markdown("## ⭐ 專長摘要")

c1, c2, c3 = st.columns(3)

with c1:

    st.markdown("""
### 行政能力

- 文件整理
- 資料彙整
- 文書處理
- 簡報製作
""")

with c2:

    st.markdown("""
### 管理能力

- 團隊合作
- 時間管理
- 專案規劃
- 溝通協調
""")

with c3:

    st.markdown("""
### 航空相關

- 航空管理
- 物流管理
- 供應鏈概念
- 服務品質
""")


st.markdown("---")


# ==========================================================
# 自我介紹
# ==========================================================

st.markdown("## 📝 自傳")

st.markdown("""
<div class="resume-card">

我目前就讀於長榮大學航管系，對航空產業及服務管理領域抱持高度興趣，
在學期間除了持續累積專業知識，也積極參與各項活動，
培養團隊合作、溝通表達及解決問題的能力。

我相信細心與責任感是完成工作的基礎，因此在課堂專案、
活動執行以及日常任務中，都以認真負責的態度完成每一項工作。

未來希望能投入航空公司或大型企業，
持續精進專業能力，並透過實務經驗提升自己的管理能力，
成為能夠為團隊創造價值的人才。

</div>
""", unsafe_allow_html=True)

st.markdown("---")


# ==========================================================
# 求職目標
# ==========================================================

st.markdown("## 🎯 求職目標")

goal1, goal2 = st.columns(2)

with goal1:

    st.success("""
✔ 航空公司實習

✔ 航空行政管理

✔ 客戶服務管理

✔ 營運管理

✔ 物流管理
""")

with goal2:

    st.info("""
希望透過實習或正式工作，
將課堂所學應用於實務環境，
持續學習並提升專業能力，
成為兼具服務精神與管理能力的人才。
""")

st.markdown("---")
def get_image_files(folder_path):

    exts = [".jpg", ".jpeg", ".png", ".webp"]

    if not Path(folder_path).exists():
        return []

    files = []

    for file in sorted(os.listdir(folder_path)):

        full_path = os.path.join(folder_path, file)

        if Path(full_path).suffix.lower() in exts:

            files.append(full_path)

    return files
  
    # ----------------------------
    # 沒有資料夾或資料夾是空的 -> 從根目錄抓
    # ----------------------------

    keywords = {

        "activities": [
            "活動",
            "主持",
            "ISBU",
            "境外生"
        ],

        "awards": [
            "AI",
            "競賽",
            "獎"
        ],

        "certificates": [
            "證",
            "證照",
            "Sabre",
            "Saber",
            "ESG"
        ]

    }

    # ⭐ 如果資料夾存在而且裡面有圖片，就直接使用資料夾

    if Path(folder_path).exists():

        folder_files = []

        for file in sorted(os.listdir(folder_path)):

            full_path = os.path.join(folder_path, file)

            if Path(full_path).suffix.lower() in [".jpg", ".jpeg", ".png", ".webp"]:

                folder_files.append(full_path)

        if len(folder_files) > 0:
            return folder_files

    # ⭐ 如果沒有資料夾，或資料夾是空的，就改抓根目錄

    if folder_path not in keywords:
        return []

    files = []

    for file in sorted(os.listdir(".")):

        suffix = Path(file).suffix.lower()

        if suffix not in [".jpg", ".jpeg", ".png", ".webp"]:
            continue

        for key in keywords[folder_path]:

            if key.lower() in file.lower():

                files.append(file)
                break

    return files
# ==========================================================
# 校園與課外經歷
# ==========================================================

st.markdown("## 👥 校園與課外經歷")

experience_data = [

    (
        "校內團隊合作",
        "透過課堂分組專案與報告，培養團隊合作、時間管理及溝通能力。"
    ),

    (
        "航空管理相關課程",
        "修習航空管理、物流管理及服務品質等專業課程，建立完整基礎知識。"
    ),

    (
        "專題與簡報製作",
        "熟悉資料蒐集、簡報設計及成果發表流程。"
    ),

    (
        "活動參與",
        "積極參與校內外活動，培養跨領域合作與應變能力。"
    )

]

for title, content in experience_data:

    with st.container(border=True):

        st.markdown(f"### {title}")

        st.write(content)

st.markdown("---")
# ==========================================================
# 專業證照
# ==========================================================

st.markdown("## 📜 專業證照")

certificate_files = get_image_files("certificates")

if len(certificate_files) == 0:

    st.info("沒有找到證照圖片")

else:

    cols = st.columns(2)

    for i, img in enumerate(certificate_files):

        with cols[i % 2]:

            st.image(img, use_container_width=True)

            st.caption(Path(img).stem)

st.markdown("---")


# ==========================================================
# 獲獎紀錄
# ==========================================================

st.markdown("## 🏆 獲獎紀錄")

award_files = get_image_files("awards")

if len(award_files) == 0:

    st.info("沒有找到獎狀圖片")

else:

    cols = st.columns(2)

    for i, img in enumerate(award_files):

        with cols[i % 2]:

            st.image(img, use_container_width=True)

            st.caption(Path(img).stem)

st.markdown("---")


# ==========================================================
# 活動參與
# ==========================================================

st.markdown("## 🎯 活動參與")

activity_files = get_image_files("activities")

if len(activity_files) == 0:

    st.info("沒有找到活動圖片")

else:

    cols = st.columns(3)

    for i, img in enumerate(activity_files):

        with cols[i % 3]:

            st.image(img, use_container_width=True)

            st.caption(Path(img).stem)

st.markdown("---")

# ==========================================================
# 個人特質
# ==========================================================

st.markdown("## 🌟 個人特質")

trait1, trait2 = st.columns(2)

with trait1:

    st.success("✔ 細心負責")
    st.success("✔ 做事有條理")
    st.success("✔ 願意學習")
    st.success("✔ 具抗壓能力")

with trait2:

    st.success("✔ 團隊合作")
    st.success("✔ 溝通能力")
    st.success("✔ 配合度高")
    st.success("✔ 主動解決問題")

st.markdown("---")


# ==========================================================
# 未來發展方向
# ==========================================================

st.markdown("## 🚀 未來發展方向")

st.markdown("""
<div class="resume-card">

希望能進入航空公司或大型企業，將所學應用於實際工作，
透過持續學習與累積經驗，在航空管理、營運管理、服務管理、
物流供應鏈等領域持續成長。

也期待在團隊合作中發揮自身細心、負責與積極學習的特質，
為公司創造價值，同時實現自我成長。

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# Part 4：文件下載、聯絡資訊、Footer
# ==========================================================

# -----------------------------
# 工具函式：取得文件
# -----------------------------

def get_document_files(folder_path):
    """
    自動讀取 documents 資料夾中的檔案
    """
    exts = [
        ".pdf",
        ".doc",
        ".docx",
        ".ppt",
        ".pptx",
        ".xls",
        ".xlsx"
    ]

    if not Path(folder_path).exists():
        return []

    files = []

    for file in sorted(os.listdir(folder_path)):

        if Path(file).suffix.lower() in exts:

            files.append(os.path.join(folder_path, file))

    return files


# ==========================================================
# 履歷附件
# ==========================================================

st.markdown("## 📂 履歷附件")

documents = get_document_files("documents")

if len(documents) == 0:

    st.info("請將 PDF、DOCX 或其他文件放入 documents 資料夾。")

else:

    for file in documents:

        with open(file, "rb") as f:

            st.download_button(
                label=f"📄 {Path(file).stem}",
                data=f,
                file_name=Path(file).name,
                mime="application/octet-stream",
                use_container_width=True
            )

st.markdown("---")


# ==========================================================
# 個人優勢
# ==========================================================

st.markdown("## 💡 個人優勢")

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
### 工作態度

✔ 認真負責

✔ 配合度高

✔ 做事細心

✔ 守時守信
""")

with col2:

    st.markdown("""
### 學習能力

✔ 願意接受挑戰

✔ 快速學習

✔ 自主進修

✔ 持續成長
""")

with col3:

    st.markdown("""
### 團隊合作

✔ 溝通協調

✔ 跨部門合作

✔ 共同解決問題

✔ 積極參與
""")

st.markdown("---")


# ==========================================================
# 求職宣言
# ==========================================================
st.markdown("## ✈️ 求職宣言")

st.markdown("""
<div class="resume-card">

我相信每一次學習都是累積未來實力的重要過程。

希望能加入優秀的團隊，在實務工作中持續精進專業能力，
將所學知識應用於航空產業或企業管理領域，並以積極、
細心、負責的態度完成每一項任務，為團隊創造價值。

</div>
""", unsafe_allow_html=True)

st.markdown("---")


# ==========================================================
# 聯絡資訊
# ==========================================================

st.markdown("## 📬 聯絡方式")

contact1, contact2 = st.columns(2)

with contact1:

    st.markdown("""
**姓名**

黃紫薇

**學校**

長榮大學

**求職方向**

航空公司實習／航空行政／營運管理
""")

with contact2:

    st.markdown("""
**Email**

ziwei041022@example.com

**電話**

0966-020-110

**所在地**

台北大安區浦城街
""")

st.markdown("---")


# ==========================================================
# 履歷總結
# ==========================================================

st.markdown("## 📖 履歷總覽")

st.success("""
✔ 航空管理相關背景

✔ 長榮大學在學

✔ 具團隊合作能力

✔ 具文書與簡報能力

✔ 積極學習、責任感佳

✔ 適合航空公司及企業實習職缺
""")

st.markdown("---")


# ==========================================================
# Footer
# ==========================================================

st.markdown(
    """
    <div class="footer">

    <h4>Resume Website</h4>

    <p>
    © 2026 黃紫薇 ｜ Chang Jung Christian University
    </p>

    <p>
    Designed with Streamlit
    </p>

    </div>
    """,
    unsafe_allow_html=True,
)
