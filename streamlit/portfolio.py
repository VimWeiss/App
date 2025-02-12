import streamlit as st

# Set the page title and layout
st.set_page_config(page_title="My Portfolio", layout="centered")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["Home", "Projects", "Contact"])

# Home section
if options == "Home":
    st.title("Welcome to My Portfolio!")
    st.image("https://via.placeholder.com/800x300", use_column_width=True)
    st.write("""
    ## About Me
    Hello! I'm a passionate developer with experience in building web applications and data analysis. 
    I love to explore new technologies and apply them in my projects.
    """)

# Projects section
elif options == "Projects":
    st.title("Projects")
    st.write("Here are some of the projects I've worked on:")

    st.subheader("Project 1: Web Scraper")
    st.write("A web scraper that collects data from various websites and stores it in a structured format.")
    st.image("https://via.placeholder.com/400x200", use_column_width=True)

    st.subheader("Project 2: Data Visualization")
    st.write("An interactive dashboard for visualizing complex datasets using Python and Streamlit.")
    st.image("https://via.placeholder.com/400x200", use_column_width=True)

    st.subheader("Project 3: Machine Learning Model")
    st.write("A machine learning model that predicts housing prices based on various features.")
    st.image("https://via.placeholder.com/400x200", use_column_width=True)

# Contact section
elif options == "Contact":
    st.title("Contact Me")
    st.write("Feel free to reach out to me through the following channels:")

    st.write("Email: myemail@example.com")
    st.write("LinkedIn: [My LinkedIn Profile](https://www.linkedin.com)")
    st.write("GitHub: [My GitHub Repositories](https://github.com)")

# Footer
st.sidebar.write("---")
st.sidebar.write("© 2023 My Portfolio")