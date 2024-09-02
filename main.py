import streamlit as st
import google.generativeai as gen_ai

# Configure Streamlit page settings
st.set_page_config(
    page_title="Competitor Blog Analyzer",
    page_icon=":chart_with_upwards_trend:",  # Favicon emoji
    layout="centered",  # Page layout option
)

# Directly set the API key here (not recommended for production)
GOOGLE_API_KEY = "AIzaSyCO7WIRmXTQUPeiARLTklKLufkZRfjfg4U"

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Streamlit app layout
st.title("Competitor Blog Analyzer")

# User input: Competitor's blog link
competitor_blog_url = st.text_input("Enter the URL of the top-ranking competitor blog")

# User input: User's blog content or URL
user_blog_input = st.text_area("Enter your blog content or URL")

# Analysis level
analysis_level = st.selectbox(
    "Select the level of analysis needed:",
    ["Basic", "Standard", "Advanced"]
)

# Combine user inputs for the analysis
if st.button("Analyze Blogs"):
    prompt = f"""
    Create a detailed analysis of competitor blogs, focusing on the SEO factors that contribute to their rankings. The analysis should include a comprehensive comparison of target keywords, content quality, on-page SEO, user experience, off-page SEO, technical SEO, and content promotion strategies. For each competitor blog, evaluate how these factors are optimized and where they outperform or underperform compared to the user's blog. Summarize your findings in a well-structured table, highlighting key metrics and differences. At the end of the report, provide a pros and cons list for each competitor and the user's blog, offering actionable insights and recommendations for improvement {analysis_level}:

    Competitor Blog URL: '{competitor_blog_url}'

    User Blog Content/URL: '{user_blog_input}'
    """

    with st.spinner("Analyzing blogs..."):
        # Generate the analysis using the Gemini-Pro model
        response = model.generate_content([prompt])
        analysis_report = response.text

    # Display the analysis report
    st.subheader(f"{analysis_level} Analysis Report")
    st.write(analysis_report)
