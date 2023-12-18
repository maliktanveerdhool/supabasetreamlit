import streamlit as st
from st_supabase_connection import SupabaseConnection

# Set page title and layout
st.set_page_config(page_title="My Streamlit App", layout="wide")

# Initialize connection.
conn = st.connection("supabase", type=SupabaseConnection)

# Perform query.
rows = conn.query("*", table="mytable", ttl="10m").execute()

# Header and Filter
st.title("Data from Supabase")
st.markdown("---")
name_filter = st.text_input("Filter by Name")

# Filter and Display results
filtered_rows = [row for row in rows.data if name_filter.lower() in row['name'].lower()]

if filtered_rows:
    for row in filtered_rows:
        st.write(f"**{row['name']}** has a **{row['pet']}**.")
else:
    st.write("No matching records found.")

# Add a footer or additional information
st.markdown("---")
st.info("Data fetched from Supabase.")

# Add a footer for credits or references
st.markdown("---")
st.text("Created by Malik Tanveer")
