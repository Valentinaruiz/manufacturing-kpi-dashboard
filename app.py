import streamlit as st
import pandas as pd
import plotly.express as px
st.title("Manufacturing KPI Dashboard")

st.write("Built by Valentina Ruiz")

st.header("Project Overview")

st.write("""
This dashboard helps manufacturing engineers monitor:

- Throughput
- Utilization
- OEE (Overall Equipment Effectiveness)
- Defect Rate
- Production Performance
""")

st.header("Machine Status")

st.metric("Throughput", "950 units/day")
st.metric("Defect Rate", "2.5%")
st.metric("OEE", "87%")


st.header("Upload Manufacturing Data")

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully!")

    st.subheader("Data Preview")

    st.dataframe(df)

    total_good = df["Good Parts"].sum()
    total_defects = df["Defective Parts"].sum()

    total_parts = total_good + total_defects

    defect_rate = (total_defects / total_parts) * 100

    st.header("Manufacturing KPIs")

    st.metric("Total Production", total_parts)

    st.metric("Good Parts", total_good)

    st.metric("Defect Rate (%)", round(defect_rate, 2))

    st.header("Production by Machine")

    fig = px.bar(
    df,
    x="Machine",
    y="Good Parts",
    title="Good Parts Produced by Machine"
)

    st.plotly_chart(fig)   
