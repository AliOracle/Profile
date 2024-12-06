import streamlit as st

## Page setups
about_me = st.Page(
    page = "views/about_me.py",
    title = "About Me",
    icon = ":material/person:",
    default = True,
)

## Page setups
accedmic_qualification = st.Page(
    page = "views/accedmic_qualification.py",
    title = "Accedmic Qualification",
    icon = ":material/card_membership:",
)

## Page setups
additional_qualification = st.Page(
    page = "views/additional_qualification.py",
    title = "Additional Qualification",
    icon = ":material/workspace_premium:",
)

# pg = st.navigation(pages=[about_me, accedmic_qualification, additional_qualification])

pg = st.navigation(
    {"Personel": [about_me],
     "Qualification": [accedmic_qualification, additional_qualification],}
)

st.sidebar.text("Developed by Ali Asghar")

pg.run()
