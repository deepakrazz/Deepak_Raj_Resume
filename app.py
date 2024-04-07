from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "main.css"
resume_file = current_dir / "Deepak_Raj_Resume.pdf"
profile_pic = current_dir / "profile_pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Deepak Raj"
PAGE_ICON = ":wave:"
NAME = "Deepak Raj"
DESCRIPTION = """
Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "deepakraj11298@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/deepakraj018/",
    "GitHub": "https://github.com/deepakrazz",
    }

### -- Projects 
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 *T20 World Cup Cricket data analytics*" : "Link_1",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


## --- load css, pdf, & profile pic ----
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html = True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


## --- Hero Section ----
col1, col2 = st.columns(2,gap="small")
with col1:
    st.image(profile_pic,width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📩", EMAIL)

## --- Social Links ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write("---")
st.write(
    """
- 👩‍💻 Programming: Python (NumPy, Pandas), SQL, R
- 📊 Data Visulization: Power BI, MS Excel, Tableau
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: MySQL
"""
)

# --- Education ---
st.write('\n')
st.subheader("Education")
st.write("---")
##--- M.Tech ----
st.write("🎓", "**National Institute of Technology Karnataka**")
st.write("Master of Technology" '\t' "(09/2021 - 07/2023)")
##--- B.Tech ----
st.write("👨‍🎓", "**National Institute of Technology Agartala**") 
st.write("Bachelor of Technology" '\t' "(08/2017 - 06/2021)")
##--- !2th  ----
st.write("🏫", "**Yadav Public Senior Secondary School Jodhpur**")
st.write("Class 12th" '\t' "(06/2015 - 05/2016)")
##--- B.Tech ----
st.write("🏫", "**Dr B.R. Ambedkar Govt. Residential School Mandore Jodhpur**")
st.write("Class 10th" '\t' "(06/2013 - 06/2014)")



# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Analyst | The Purple Heaven**")
st.write("08/2023 - 02/2024")

st.write(
    """
- ▶️ Using Power BI, Excel, and Google Sheets, create a monthly and weekly business intelligence (BI) dashboard to track :
    - ⚫ Top and bottom-selling dishes
    - ⚫ Revenue generated
    - ⚫ Profit earned
"""
)


# --- Projects ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")