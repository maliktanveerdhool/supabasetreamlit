import streamlit as st
from st_login_form import login_form

client = login_form()

if st.session_state.get("authenticated"):
    if st.session_state.get("username"):
        st.success(f"Welcome {st.session_state['username']}")
        # Redirect to app.py after successful login
        st.experimental_set_query_params(next='app.py')
    else:
        st.success("Welcome guest")
else:
    st.error("Not authenticated")
