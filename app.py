from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.JPG"
nizek = current_dir / "assets" / "nizek.jpeg"
tapsell = current_dir / "assets" / "tapsell.png"
bazaar = current_dir / "assets" / "bazaar.png"
raymand = current_dir / "assets" / "raymand.png"




# --- GENERAL SETTINGS ---
PAGE_TITLE = " Portfolio | Amir Yamini"
PAGE_ICON = ":wave:"
NAME = "Amir Yamini"
DESCRIPTION = """
A hardworking and non-stop learner data analyst with an engineering background,
and experience in collecting, organizing, interpreting various types of statistical figures.
Creative in finding solutions to problems and
determining modifications for optimal use of organizational data and
executive management with reports on specific data findings and their impact on organizational
growth and success.
"""
EMAIL = "amiryamini95@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/amiryamini/",
    "GitHub": "https://github.com/iamem1r",
    "Stackoverflow": "https://stackoverflow.com/users/12094597/amir-yamini"
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)
nizek = Image.open(nizek)
tapsell = Image.open(tapsell)
bazaar = Image.open(bazaar)
raymand = Image.open(raymand)




# --- HERO SECTION ---
col1, col2 = st.columns(2, gap='large')
with col1:
    st.image(profile_pic, use_column_width=True)

with col2:
    st.title(NAME)
    st.write("**Senior Data Analyst**")
    st.write(DESCRIPTION)
    # st.download_button(
    #     label=" 📄 Download Resume",
    #     data=PDFbyte,
    #     file_name=resume_file.name,
    #     mime="application/octet-stream",
    # )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ +2 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and SQL
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 🧑🏻‍💻 Programming: Python (OOP, Pandas, Numpy, Streamlit), SQL
- 📊 Data Visulization: Plotly, Matplotlib, Seaborn, Data Studio, PowerBi, 
- 🗄️ Databases: MongoDB, MySQL, Google BigQuery
- 💻 OS: Mac, Linux, Windows
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.image(nizek, width=120)
st.write("**Senior Data Analyst | Nizek Tech**")
st.write("11/2022 - Present")
st.write(
    """
    - ► design analytics data structures and custom events (user behavior, financial) for e-commerce applications (mobile, web)
    - ► design efficient events flow and define metrics and KPIs for e-commerce data
    - ► verify the implementation of events on the client side (mobile/web)
    - ► monitor data and make queries, reports and dashboards using our analytical platforms
    - ► connect databases to our analytical platforms
    - ► verify the implementation of analytical and marketing platforms specially push notification automation
"""
)

# --- JOB 2
st.write('\n')
st.write('\n')
st.write('\n')
st.image(tapsell, width=120)
st.write("**Product Data Analyst | Tapsell**")
st.write("10/2021 - 11/2022\t(1 yr 1 mo)")
st.write(
    """
    - ► Design and Develop a data dashboard for developers and designers teams to view all KPIs, such as retention, engagement time, LTV, ARPU and etc.
    - ► Design and develop metrics, reports, analyses, and KPIs to drive key business and product decisions; improve performance and reduce costs.
    - ► Designing experimentations and A/B tests to measure the real impact of the new features/ products.
    - ► Assist various teams in deeply understanding their shortcomings on data analysis, generate ideas or hypothesis and validate them, and finally developing and implementing solutions.
"""
)

# --- JOB 3
st.write('\n')
st.write('\n')
st.write('\n')
st.image(bazaar, width=100)
st.write("**Application Specialist | Cafe Bazaar**")
st.write("09/2019 - 1/2021\t(2 yrs 3 mos)")
st.write(
    """
    - ► Create interpretable dashboards by querying over millions records of data.
    - ► Monitoring user reports and detecting application malware.
    - ► Benchmarking android market research to develop appropriate programs to release in Cafe Bazaar.
    - ► Examined the applications that have been requested to be published in Cafe Bazaar. Communicated with developers regarding the result of the review.
"""
)

# --- JOB 4
st.write('\n')
st.write('\n')
st.write('\n')
st.image(raymand, width=100)
st.write("**Robotics Instructor | Raymand Robotic Inst**")
st.write("06/2017 - 09/2019\t(2 yrs 3 mos)")
st.write(
    """
    - ► Teaching Programming basics (Scratch, Raspberry Pi, Ready Boards
    - ► Teaching Solidworks software basics concepts (Designing Mechanical parts and printing by the 3D printer
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
