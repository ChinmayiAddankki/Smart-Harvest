import streamlit as st
import pandas as pd
import datetime

# Page config
st.set_page_config(page_title="SmartHarvest", layout="wide")

# Header
st.title("🌱 SmartHarvest Dashboard")
st.markdown("Welcome to SmartHarvest! Let's optimize your taxes with smart, effortless strategies.")

# Tax Savings Chart
st.subheader("📈 Your Tax Saving Trends")
tax_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Savings (₹)': [200, 250, 300, 320]
})
st.line_chart(tax_data.set_index('Month'))

# Suggested Asset Card
st.subheader("💰 Asset Suggestion")
st.markdown("""
*Recommendation:* Sell ABC Corp to offset *₹2,500* in gains this quarter.

> This recommendation is based on short-term capital loss rules and gain balancing.

""")
if st.button("✅ Harvest Now"):
    st.success("Harvesting executed!")

# Learning Progress
st.subheader("📚 Learning Module")
progress = 80
st.progress(progress)
st.markdown("*80% completed* - Badge Unlocked: 🏅 Harvest Hero")
if st.button("📖 Continue Learning"):
    st.info("Redirecting to learning module...")

# Important Dates
st.subheader("📆 Important Dates")
st.markdown("- 🗓 *April 30*: Deadline to harvest ABC Corp for FY24")
st.markdown("- 📄 *May 15*: New tax report summary available")

# Success Metrics
st.subheader("📊 Success Metrics")
st.metric("Opportunities Identified", "3 this week")
st.metric("Learning Completion", "80%")
st.metric("User Confidence Score", "72%")

# Footer
st.markdown("---")
st.markdown("""
SmartHarvest is designed to make tax optimization intuitive and stress-free.  
*Maximize your savings. Minimize your confusion.*
""")
