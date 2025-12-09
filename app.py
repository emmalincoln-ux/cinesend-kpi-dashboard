import streamlit as st
import pandas as pd
from data_fetchers import (
    get_ga4_users,
    get_webflow_form_submissions,
    get_hotjar_events,
    get_hubspot_leads
)

st.set_page_config(page_title="Cinesend KPI Dashboard", layout="wide")

st.title("🎬 Cinesend KPI Dashboard")
st.write("Automatically pulling KPIs from GA4, Webflow, Hotjar, and HubSpot.")

# ----------------------------
# Fetch Data
# ----------------------------
st.header("📊 Live KPIs")

col1, col2, col3, col4 = st.columns(4)

with st.spinner("Fetching Google Analytics data..."):
    ga4_users = get_ga4_users()

with st.spinner("Fetching Webflow form submissions..."):
    webflow_forms = get_webflow_form_submissions()

with st.spinner("Fetching Hotjar events..."):
    hotjar_events = get_hotjar_events()

with st.spinner("Fetching HubSpot leads..."):
    hubspot_leads = get_hubspot_leads()

# ----------------------------
# Display KPIs
# ----------------------------

col1.metric("GA4 Users (Last 7 Days)", ga4_users)
col2.metric("Webflow Form Submissions", webflow_forms)
col3.metric("Hotjar Key Events", hotjar_events)
col4.metric("HubSpot New Contacts", hubspot_leads)

st.divider()

# ----------------------------
# Detailed Data Section
# ----------------------------

st.header("📁 Detailed Raw Data")

tabs = st.tabs(["GA4", "Webflow", "Hotjar", "HubSpot"])

with tabs[0]:
    st.subheader("Google Analytics 4")
    st.write("Users in last 7 days:")
    st.write(pd.DataFrame({"Users": [ga4_users]}))

with tabs[1]:
    st.subheader("Webflow")
    st.write(pd.DataFrame({"Form Submissions": [webflow_forms]}))

with tabs[2]:
    st.subheader("Hotjar")
    st.write(pd.DataFrame({"Events": [hotjar_events]}))

with tabs[3]:
    st.subheader("HubSpot")
    st.write(pd.DataFrame({"New Contacts": [hubspot_leads]}))

st.success("Dashboard loaded successfully!")
