import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Manufacturing KPI Dashboard")
st.write("Built by Valentina Ruiz")

st.write("""
This dashboard analyzes manufacturing performance using production data,
quality data, and equipment efficiency metrics.
""")

uploaded_file = st.file_uploader("Upload Manufacturing CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    df["Total Parts"] = df["Good Parts"] + df["Defective Parts"]
    df["Availability"] = df["Run Time"] / df["Planned Time"]
    df["Performance"] = (df["Ideal Cycle Time"] * df["Total Parts"]) / df["Run Time"]
    df["Quality"] = df["Good Parts"] / df["Total Parts"]
    df["OEE"] = df["Availability"] * df["Performance"] * df["Quality"]
    df["Defect Rate"] = df["Defective Parts"] / df["Total Parts"]

    st.success("File uploaded successfully!")

    st.header("Data Preview")
    st.dataframe(df)

    total_parts = df["Total Parts"].sum()
    total_good = df["Good Parts"].sum()
    total_defects = df["Defective Parts"].sum()
    defect_rate = total_defects / total_parts * 100
    average_oee = df["OEE"].mean() * 100

    st.header("Overall Manufacturing KPIs")
avg_availability = df["Availability"].mean() * 100
avg_performance = df["Performance"].mean() * 100
avg_quality = df["Quality"].mean() * 100

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Production", int(total_parts))
col2.metric("Good Parts", int(total_good))
col3.metric("Defective Parts", int(total_defects))
col4.metric("Defect Rate", f"{defect_rate:.2f}%")

col5, col6, col7, col8 = st.columns(4)
col5.metric("Avg Availability", f"{avg_availability:.2f}%")
col6.metric("Avg Performance", f"{avg_performance:.2f}%")
col7.metric("Avg Quality", f"{avg_quality:.2f}%")
col8.metric("Average OEE", f"{average_oee:.2f}%")

    st.header("Machine-Level Insights")

    best_machine = df.loc[df["OEE"].idxmax(), "Machine"]
    worst_machine = df.loc[df["OEE"].idxmin(), "Machine"]
    highest_defect_machine = df.loc[df["Defect Rate"].idxmax(), "Machine"]

    st.write(f"Best performing machine based on OEE: **{best_machine}**")
    st.write(f"Lowest performing machine based on OEE: **{worst_machine}**")
    st.write(f"Machine with highest defect rate: **{highest_defect_machine}**")

    st.header("OEE by Machine")

    oee_chart = px.bar(
        df,
        x="Machine",
        y="OEE",
        title="OEE by Machine"
    )

    st.plotly_chart(oee_chart)

    st.header("Good Parts by Machine")

    production_chart = px.bar(
        df,
        x="Machine",
        y="Good Parts",
        title="Good Parts Produced by Machine"
    )

    st.plotly_chart(production_chart)
    
