import streamlit as st

#st.title("About Me")

st.subheader("PERSONAL INFORMATION")
# st.text("""
# Address : Flat 306, Melhoof 2 Building,
#           Street 15, Nahda2, Dubai, U.A.E 
# Contact : (Res) +971 06 5258336 
#           (Mob) +971 50 1985414
#           (Email) ali.oracle@gmail.com 
#                   alisbraveheart@hotmail.com 
# Father Name      : Shabbir Hussain 
# Marital Status   : Married 
# Date of Birth    : 13th Sep 1977 
# Passport #       : AQ1821372 
# Nationality      : Pakistani 
# Resident of      : U.A.E 
# Visa Status      : Job / Residential
# """)

# Custom HTML with CSS for font styling
st.markdown(
    """
    <style>
    .info-table {
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 14px;
        color: #333333;
        width: 100%;
        border-collapse: collapse; /* Removes spacing between cells */
        border: none; /* Removes table borders */
    }
    .info-table td {
        padding: 5px 10px;
        vertical-align: top;
        border: none; /* Removes cell borders */
    }
    .info-table .label {
        font-weight: bold;
        width: 30%;
    }
    </style>
    <table class="info-table">
        <tr><td class="label">Address</td><td>1201, Tiger 1 Building, Near Sahara Centre,<br>Al Nahda, Sharjah, U.A.E</td></tr>
        <tr><td class="label">Contact</td><td>(Res) +971 06 5258336<br>(Mob) +971 50 1985414<br>(Email) ali.oracle@gmail.com<br>alisbraveheart@hotmail.com</td></tr>
        <tr><td class="label">Father Name</td><td>Shabbir Hussain</td></tr>
        <tr><td class="label">Marital Status</td><td>Married</td></tr>
        <tr><td class="label">Date of Birth</td><td>13th Sep 1977</td></tr>
        <tr><td class="label">Passport #</td><td>AQ1821372</td></tr>
        <tr><td class="label">Nationality</td><td>Pakistani</td></tr>
        <tr><td class="label">Resident of</td><td>U.A.E</td></tr>
        <tr><td class="label">Visa Status</td><td>Job / Residential</td></tr>
    </table>
    """,
    unsafe_allow_html=True,
)


st.subheader("PROFILE")
st.write("Detail-oriented individual with 10+ years of experience in Oracle SQL & PL/SQL, Oracle Performance tuning, Technical and functional analysis and leading a mid-size team looking to secure a suitable position.")

st.subheader("HOBBIES & INTRESTS")
st.write(
    """
    - Fishing
    - Travelling
    - Watching & Playing Cricket
    - Watching Movies
    - Puzzles (Crosswords)
    """
)
