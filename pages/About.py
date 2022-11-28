import streamlit as st

st.set_page_config(layout='wide')

st.title('About Us - Datavengers')

row0_1, row0_spacer1, row0_2, row0_spacer2 = st.columns(
    (1, 0.1, 1, 0.1)
)

with row0_1:
    st.header('Na Ni')
    st.markdown('+  Email: ' + '**' + 'nani@usc.edu' + '**' + '\n' +
                '+  Current Program: ' + '**' + 'Applied Data Science' + '**' + '\n' +
                '+  Undergraduate Major: ' + '**' + 'Geography' + '**' + '\n' +
                '+  Skills: ' + '**' + 'Data Processing, Machine Learning' + '**' + '\n')
    st.header('Wenhao Zhang')
    st.markdown('+  Email: ' + '**' + 'wzhang01@usc.edu' + '**' + '\n' +
                '+  Current Program: ' + '**' + 'Applied Data Science' + '**' + '\n' +
                '+  Undergraduate Major: ' + '**' + 'Software Engineering' + '**' + '\n' +
                '+  Skills: ' + '**' + 'Web Development, Machine Learning' + '**' + '\n')

with row0_2:
    st.header('Tianran Qiu')
    st.markdown('+  Email: ' + '**' + 'tianranq@usc.edu' + '**' + '\n' +
                '+  Current Program: ' + '**' + 'Applied Data Science' + '**' + '\n' +
                '+  Undergraduate Major: ' + '**' + 'Data Science' + '**' + '\n' +
                '+  Skills: ' + '**' + 'Machine Learning, Data Analytics' + '**' + '\n')
    st.header('Da Gong')
    st.markdown('+  Email: ' + '**' + 'dagong@usc.edu' + '**' + '\n' +
                '+  Current Program: ' + '**' + 'Applied Data Science' + '**' + '\n' +
                '+  Undergraduate Major: ' + '**' + 'Software Engineering' + '**' + '\n' +
                '+  Skills: ' + '**' + 'Data Modeling, Data Analysis' + '**' + '\n')   