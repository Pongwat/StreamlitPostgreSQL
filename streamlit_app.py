import streamlit as st

st.title("Teacher Management Dashboard")

conn = st.connection("postgresql", type="sql")

df = conn.query('SELECT * FROM teachers;', ttl="10m")

st.subheader("All Teachers")
st.dataframe(df, use_container_width=True)

st.subheader("Teacher Details")

for row in df.itertuples():
    st.write(f"{row.first_name} has a : {row.last_name}"
             f"works at {row.school} and earns ${row.salary:,}"
             )