import streamlit as st

st.title("Asset Naming Tool")

# Step 1: Select asset type
asset_type = st.selectbox("Select asset type", ["Dashboard", "Event", "Funnel", "Metric"])

def get_input(label, options):
    choice = st.selectbox(label, options + ["Other"])
    if choice == "Other":
        return st.text_input(f"Enter custom {label.lower()}")
    return choice

# Step 2: Show form based on asset type
name = ""
if asset_type == "Dashboard":
    team = get_input("Owner Team", ["Cathay Shop", "IBE", "MMB", "OLCI", "Membership", "TravelApp", "TRP", "General"])
    title = get_input("Dashboard Title", ["Sales Overview", "User Engagement", "System Health"])
    product = get_input("Product Name", ["AppX", "WebY", "ServiceZ"])
    if team and title and product:
        name = f"{team}_{product}_dashboard_{title.replace(' ', '_')}"

elif asset_type == "Event":
    product = get_input("Product Name", ["Cathay Shop", "IBE", "MMB", "OLCI", "Membership", "TravelApp", "TRP", "General"])
    feature = get_input("Feature, element, page or screen name", ["Homepage Personal Banner", "PDP Add-to-cart"])
    action = get_input("Trigger action", ["click", "pageview", "present"])
    platform = get_input("Channel", ["web", "IOS", "Android"])
    if product and feature and action and platform:
        name = f"{product} - {feature} - {action} - {platform}"

elif asset_type == "Funnel":
    team = get_input("Owner Team", ["Marketing", "Product", "Engineering"])
    funnel_name = get_input("Funnel Name", ["Conversion", "Signup Flow", "Checkout"])
    steps = get_input("Steps", ["Step1, Step2, Step3"])
    if team and funnel_name and steps:
        name = f"{team}_funnel_{funnel_name.replace(' ', '_')}_{steps.replace(',', '_')}"

elif asset_type == "Metric":
    team = get_input("Owner Team", ["Marketing", "Product", "Engineering"])
    metric_name = get_input("Metric Name", ["Retention Rate", "Conversion Rate", "Bounce Rate"])
    logic = get_input("Calculation Logic", ["Users Retained / Total Users"])
    if team and metric_name and logic:
        name = f"{team}_metric_{metric_name.replace(' ', '_')}_{logic.replace(' ', '_')}"

# Step 3: Show result and copy button
if name:
    st.text_area("Generated Name", value=name, height=100)
    st.code(name, language="text")
    st.success("You can copy the name above using the copy icon.")
