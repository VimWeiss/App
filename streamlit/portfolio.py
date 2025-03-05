import streamlit as st

# Set the page title and layout
st.set_page_config(page_title="Мое портфолио", layout="centered")

# Sidebar for navigation
st.sidebar.title("Навигация")
options = st.sidebar.radio("Меню", ["Домой", "Проекты", "Контакты"])

# Home section
if options == "Домой":
    st.title("Добро пожаловать в мое портфолио!")
    st.image("./static/portrait.JPG", use_container_width=False, width=200)
    st.write("""
    ## Немного обо мне
    Привет, меня зовут Вадим Яшкин и я программист, технолог ERP систем, а также Специалист по кибербезопасности.
    Я работаю в РЖД
    """)
    st.markdown("[Скачать мое резюме](./static/resume.pdf)", unsafe_allow_html=True)

# Projects section
elif options == "Проекты":
    st.title("Мои проекты")
    st.write("Несколько проектов над которыми я работал:")

    st.subheader("Проект 1: Решение квадратных уравнений")
    st.write("Web приложение выполняет решение квадратных уравнений, выводит подробное решение, строит график функции, сохраняет решение в базу данных.")
    col1, col2 = st.columns(2)
    with col1:
        st.image("./static/Screenshot1.png", use_container_width=False, width=200)
    with col2:
        st.image("./static/Screenshot2.png", use_container_width=False, width=200)
    st.markdown("[GitHub репозиторий](https://github.com/VimWeiss/QuadraticSolver)", unsafe_allow_html=True)

    st.subheader("Project 2: Data Visualization")
    st.write("An interactive dashboard for visualizing complex datasets using Python and Streamlit.")
    st.image("https://via.placeholder.com/400x200", use_column_width=True)

    st.subheader("Project 3: Machine Learning Model")
    st.write("A machine learning model that predicts housing prices based on various features.")
    st.image("https://via.placeholder.com/400x200", use_column_width=True)

# Contact section
elif options == "Контакты":
    st.title("Contact Me")
    st.write("Feel free to reach out to me through the following channels:")

    st.write("Email: myemail@example.com")
    st.write("LinkedIn: [My LinkedIn Profile](https://www.linkedin.com)")
    st.write("GitHub: [My GitHub Repositories](https://github.com)")

# Footer
st.sidebar.write("---")
st.sidebar.write("© 2025 Мое портфолио")