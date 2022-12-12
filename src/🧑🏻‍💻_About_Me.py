from pathlib import Path
from streamlit_lottie import st_lottie

from data import DATA_DIR
import streamlit as st
from PIL import Image
import requests

PAGE_TITLE = " Portfolio | Amir Yamini"
PAGE_ICON = ":wave:"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# --- PATH SETTINGS ---
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
lottie_horiz = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_18QlHa.json")
css_file = DATA_DIR / "styles" / "main.css"
resume_file = DATA_DIR / "assets" / "CV.pdf"
profile_pic = DATA_DIR / "assets" / "profile-pic.JPG"
nizek = DATA_DIR / "assets" / "nizek.jpeg"
tapsell = DATA_DIR / "assets" / "tapsell.png"
bazaar = DATA_DIR / "assets" / "bazaar.png"
raymand = DATA_DIR / "assets" / "raymand.png"


# --- GENERAL SETTINGS ---
NAME = "Amir Yamini"
DESCRIPTION = """
**Data Analyst** with an engineering background, and experience in
collecting, organizing, interpreting,
and disseminatingvarious types of statistical figures.
Energetic presenter and confident communicator with the ability to circulate
information in a way that is clear, efficient, and beneficial for end-users.
Creative in finding solutions to problems and determining modifications fo
optimal use of organizational data.
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
with st.container():
    st.title("Hi, I am Amir :wave:")
    st.write("\n")
    st.write(DESCRIPTION)

st_lottie(lottie_horiz, height=100, key="codingg")

# --- SOCIAL LINKS ---
# st.write('\n')
# cols = st.columns(len(SOCIAL_MEDIA))
# for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#     cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
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
- 🧑🏻‍💻 Programming: Python (OOP, Sckit-Learn, Pandas, Numpy, Streamlit), SQL
- 📊 Data Visulization: Plotly, Matplotlib, Seaborn, Data Studio, PowerBi
- 🗄️ Databases: MongoDB, MySQL, Google BigQuery
- 💻 OS: Windows, Linux, Mac
"""
)

st_lottie(lottie_horiz, height=100, key="coding")


# --- WORK HISTORY ---
st.subheader("I worked in ...")

nizek_, tapsell_, bazaar_, raymand_ = st.columns(4)

with nizek_:
    st.image(nizek, width=110)
with tapsell_:
    st.image(tapsell, width=80)
with bazaar_:
    st.image(bazaar, width=60)
with raymand_:
    st.image(raymand, width=60)


# --- JOB 1
# st.image(nizek, width=120)
# st.write("**Senior Data Analyst | Nizek Tech**")
# st.write("11/2022 - Present")
# st.write(
#     """
#     - ► design analytics data structures and custom events (user behavior, financial) for e-commerce applications (mobile, web)
#     - ► design efficient events flow and define metrics and KPIs for e-commerce data
#     - ► verify the implementation of events on the client side (mobile/web)
#     - ► monitor data and make queries, reports and dashboards using our analytical platforms
#     - ► connect databases to our analytical platforms
#     - ► verify the implementation of analytical and marketing platforms specially push notification automation
# """
# )

# --- JOB 2
# st.write('\n')
# st.write('\n')
# st.write('\n')
# st.image(tapsell, width=120)
# st.write("**Product Data Analyst | Tapsell**")
# st.write("10/2021 - 11/2022\t(1 yr 1 mo)")
# st.write(
#     """
#     - ► Design and Develop a data dashboard for developers and designers teams to view all KPIs, such as retention, engagement time, LTV, ARPU and etc.
#     - ► Design and develop metrics, reports, analyses, and KPIs to drive key business and product decisions; improve performance and reduce costs.
#     - ► Designing experimentations and A/B tests to measure the real impact of the new features/ products.
#     - ► Assist various teams in deeply understanding their shortcomings on data analysis, generate ideas or hypothesis and validate them, and finally developing and implementing solutions.
# """
# )

# --- JOB 3
# st.write('\n')
# st.write('\n')
# st.write('\n')
# st.image(bazaar, width=100)
# st.write("**Application Specialist | Cafe Bazaar**")
# st.write("09/2019 - 1/2021\t(2 yrs 3 mos)")
# st.write(
#     """
#     - ► Create interpretable dashboards by querying over millions records of data.
#     - ► Monitoring user reports and detecting application malware.
#     - ► Benchmarking android market research to develop appropriate programs to release in Cafe Bazaar.
#     - ► Examined the applications that have been requested to be published in Cafe Bazaar. Communicated with developers regarding the result of the review.
# """
# )

# --- JOB 4
# st.write('\n')
# st.write('\n')
# st.write('\n')
# st.image(raymand, width=100)
# st.write("**Robotics Instructor | Raymand Robotic Inst**")
# st.write("06/2017 - 09/2019\t(2 yrs 3 mos)")
# st.write(
#     """
#     - ► Teaching Programming basics (Scratch, Raspberry Pi, Ready Boards
#     - ► Teaching Solidworks software basics concepts (Designing Mechanical parts and printing by the 3D printer
# """
# )


# --- Projects & Accomplishments ---
# st.write('\n')
# st.subheader("Projects & Accomplishments")
# st.write("---")
# for project, link in PROJECTS.items():
#     st.write(f"[{project}]({link})")
st_lottie(lottie_horiz, height=100, key="codiing")

# ---- CONTACT ----
with st.container():
    st.subheader("Feel free to contact")
    # st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/amiryamini95@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()


# --- Projects & Accomplishments ---
# st.write('\n')
# st.download_button(
#         label=" 📄 Download Resume",
#         data=PDFbyte,
#         file_name=resume_file.name,
#         mime="application/octet-stream",
#     )
