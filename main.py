import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(
    page_title="Student Performance Analyzer",
    page_icon="🎓",
    layout="wide"
)

st.title("Student Performance Analyzer")
st.markdown("Analyze student academic performance through automated data insights and rankings.")
st.divider()

with st.sidebar:
    st.header("Upload Student Dataset")
    file = st.file_uploader("", type=["csv", "xlsx"])

    if file is not None:
        if file.name.endswith("csv"):
            df = pd.read_csv(file).dropna()
        else:
            df = pd.read_excel(file).dropna()

        st.divider()
        st.subheader("Map Your Columns")

        name_df = df.select_dtypes(include=['object', 'string'])
        name_options = name_df.columns.tolist()
        name_col = st.selectbox("Select Student Name Column:", options=name_options)

        numeric_df = df.select_dtypes(include=['number'])
        subject_options = numeric_df.columns.tolist()
        safe_subjects = [col for col in subject_options if col != name_col]
        subj_col = st.multiselect("Select Subject Columns:", options=safe_subjects)

if file is not None:
    if len(subj_col) > 0:
        df['Average_Marks'] = df[subj_col].mean(axis=1)

        bins = [0, 50, 60, 70, 80, 100]
        grades = ['F', 'D', 'C', 'B', 'A']
        df['Grade'] = pd.cut(df['Average_Marks'], bins=bins, labels=grades)

        failing_students = df[df['Grade'] == 'F']
        top_10_students = df.nlargest(10, 'Average_Marks')

        st.markdown("### Class Overview")
        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric("Total Students", len(df))
        with m2:
            class_avg = round(df['Average_Marks'].mean(), 2)
            st.metric("Overall Class Average", f"{class_avg}")
        with m3:
            st.metric("Students Failing", len(failing_students))
        st.divider()

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Top Performers")
            leaderboard_view = top_10_students[[name_col, 'Average_Marks', 'Grade']]
            st.dataframe(leaderboard_view, use_container_width=True, hide_index=True)
        with col2:
            st.subheader("Attention Required")
            st.dataframe(failing_students[[name_col, 'Average_Marks', 'Grade']], use_container_width=True,
                         hide_index=True)
        st.divider()

        with st.expander("View Raw Dataset"):
            st.dataframe(df, use_container_width=True)

    else:
        st.info("Please select your subject columns in the sidebar to generate the dashboard.")


else:
    st.info("Please upload a CSV or Excel file in the sidebar to begin.")