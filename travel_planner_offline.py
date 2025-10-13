import streamlit as st
import time
from gpt4all import GPT4All

# Load offline AI model (make sure your model file is in the GPT4All folder)
# Example model: orca-mini-3b-gguf2-q4_0.gguf
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

# Page setup
st.set_page_config(page_title="AI Travel Planner for Students", layout="centered")

# Add custom background image (replace with your own image path or URL)
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e");
background-size: cover;
background-position: center;
background-attachment: fixed;
filter: brightness(0.85);
}
div.block-container {
background: rgba(0, 0, 0, 0.45);
padding: 2rem;
border-radius: 20px;
color: white;
}
h1, h2, h3, h4, h5 {
color: #ffd166;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# App title
st.title("🎒 AI Travel Planner for Students")

# User inputs
destination = st.text_input("Enter your destination:", placeholder="e.g., Darjeeling")
days = st.number_input("Trip Duration (Days):", min_value=1, max_value=15, value=3)
budget = st.number_input("Total Budget (₹):", min_value=500, max_value=100000, value=5000)
interests = st.text_input("Your interests (optional):", placeholder="e.g., food, adventure, nature")

# Generate button
if st.button("✨ Generate Travel Plan"):
    if not destination:
        st.warning("Please enter a destination first.")
    else:
        with st.spinner("🧠 Generating your personalized plan..."):
            time.sleep(2)

            # AI Prompt
            prompt = f"""
            Create a detailed {days}-day travel itinerary for students visiting {destination}.
            Budget: ₹{budget}. Interests: {interests if interests else 'general'}.
            For each day, suggest:
            - 2-3 tourist spots
            - Affordable food options
            - Budget-friendly stays
            - Estimated total cost per day
            Format the result like:
            Day 1:
            Places:
            Food:
            Stay:
            Total Cost:
            """

    # output = model.generate(prompt, max_tokens=700, temp=0.7)
    with model.chat_session() as session:
        output = session.generate(
            prompt=prompt,
            max_tokens=700,
            temp=0.8,
        )

        st.subheader(f"🌍 Your {days}-Day Plan for {destination}")
        

        st.success("✅ Plan generated successfully!")
        days_output = output.split("Day")
        for day_text in days_output:
            if day_text.strip():
        # Extract the day number before ':'
                day_num = day_text.split(":")[0].strip()
                with st.expander(f"🌤️ Day {day_num} Plan"):
                    st.markdown(day_text.replace(day_num + ":", "").strip())

# Footer
st.markdown("---")
st.caption("Built by Rohan Karuri — AI Travel Planner for Students")
