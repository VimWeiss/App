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
    Привет, меня зовут Вадим Яшкин и я программист, технолог ERP систем.
    Я работаю в РЖД
    """)
    st.markdown("[Скачать мое резюме](./static/resume.pdf)", unsafe_allow_html=True)

# Projects section
elif options == "Проекты":
    st.title("Мои проекты")
    st.write("Несколько проектов над которыми я работал в последнее время:")

    st.subheader("Проект 1: Решение квадратных уравнений")
    st.write("Web приложение выполняет решение квадратных уравнений, выводит подробное решение, строит график функции, сохраняет решение в базу данных.")
    col1, col2 = st.columns(2)
    with col1:
        st.image("./static/Screenshot1.png", use_container_width=False, width=200)
    with col2:
        st.image("./static/Screenshot2.png", use_container_width=False, width=200)
    st.markdown("[GitHub репозиторий](https://github.com/VimWeiss/QuadraticSolver)", unsafe_allow_html=True)

    st.subheader("Проект 2: Сайт секции Тхэквондо")
    st.write("Лэндинг для секции тхэквондо с расписанием занятий, галереей и контактной информацией.")
    st.image("./static/Screenshot3.png", use_container_width=True)

    st.subheader("Проект 3: Интернет-магазин на Django")
    st.write("Небольшой интернет-магазин, написанный на фрэймворке Django")
    st.markdown("[GitHub репозиторий](https://github.com/VimWeiss/App/tree/743b2ce7a184e29118edadef03769293e15d7dac/django_market/mercury)", unsafe_allow_html=True)

# Contact section
elif options == "Контакты":
    st.title("Связаться со мной")
    st.write("Доступные способы связи:")

    st.write("Email: goodgod08@yandex.ru")
    st.write("GitHub: [Мой профиль GitHub](https://github.com/VimWeiss)")

# Footer
st.sidebar.write("---")
st.sidebar.write("© 2025")