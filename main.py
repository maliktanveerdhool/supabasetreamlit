import streamlit as st
from st_supabase_connection import SupabaseConnection
from st_login_form import login_form

# Function to display the app content
def display_app_content():
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

# Main part of the code
client = login_form()

# Check authentication and display content accordingly
if st.session_state.get("authenticated"):
    if st.session_state.get("username"):
        st.success(f"Welcome {st.session_state['username']}")
        display_app_content()  # Display app content after successful login
    else:
        st.success("Welcome guest")
else:
    st.error("Not authenticated")
