
import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Page configuration
st.set_page_config(
    page_title="Maya Analytics - Feedback Analyzer",
    page_icon="💬",
    layout="centered"
)

# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Application heading
st.title("💬 Maya Analytics")
st.header("AI Customer Feedback Analyzer")
st.write(
    "Enter customer feedback to identify its overall sentiment."
)

# Customer feedback input
feedback = st.text_area(
    "Customer feedback",
    placeholder="Example: Your internet service is excellent!",
    height=150
)

# Analyze feedback
if st.button("Analyze Feedback", type="primary"):
    if not feedback.strip():
        st.warning("Please enter some customer feedback.")
    else:
        scores = analyzer.polarity_scores(feedback)
        compound = scores["compound"]

        # Classify sentiment
        if compound >= 0.05:
            sentiment = "Positive 😊"
            explanation = (
                "The text expresses a generally positive tone."
            )
        elif compound <= -0.05:
            sentiment = "Negative 😟"
            explanation = (
                "The text expresses a generally negative tone."
            )
        else:
            sentiment = "Neutral 😐"
            explanation = (
                "The text has a relatively neutral or mixed tone."
            )

        # Display results
        st.subheader("Analysis Result")
        st.success(f"Sentiment: {sentiment}")
        st.write(explanation)
        st.metric("Sentiment Score", f"{compound:.2f}")

        # Display technical details
        with st.expander("View Technical Details"):
            st.write("Positive score:", scores["pos"])
            st.write("Neutral score:", scores["neu"])
            st.write("Negative score:", scores["neg"])

        st.caption(
            "This is an automated sentiment estimate, not a "
            "definitive interpretation of customer intent."
        )

# Footer separator: compatible with older Streamlit versions
st.markdown("---")
st.caption("A practical AI project by Maya Analytics")
