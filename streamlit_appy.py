import streamlit as st
import os
import shutil

from utils import extract_frames
from emotion import analyze_emotions
from speech import extract_audio, speech_to_text, count_filler_words
from confidence import calculate_confidence

# Create folders
os.makedirs("uploads", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

st.set_page_config(page_title="AI Interview Analyzer", layout="centered")

# 🎨 UI Title
st.title("🎤 AI Interview Performance Analyzer")
st.markdown("Upload your interview video and get AI-based feedback 🚀")

# 📤 Upload video
video_file = st.file_uploader("Upload Video", type=["mp4"])

if video_file is not None:

    # Save video
    video_path = "uploads/input_video.mp4"
    with open(video_path, "wb") as f:
        f.write(video_file.read())

    st.video(video_path)

    if st.button("Analyze Interview"):

        with st.spinner("Analyzing... Please wait ⏳"):

            # Processing
            frames = extract_frames(video_path)
            emotions = analyze_emotions(frames)
            audio = extract_audio(video_path)
            text = speech_to_text(audio)
            fillers = count_filler_words(text)
            score = calculate_confidence(emotions, fillers, text)

        # 🎯 Results
        st.success("Analysis Complete ✅")

        st.subheader("📊 Results")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Confidence Score", f"{score}/100")

        with col2:
            if score > 75:
                st.metric("Performance", "Excellent 🟢")
            elif score > 50:
                st.metric("Performance", "Good 🟡")
            else:
                st.metric("Performance", "Needs Improvement 🔴")

        st.write("😊 Emotions:", emotions[:5])
        st.write("🗣️ Filler Words:", fillers)

        st.subheader("📝 Speech Preview")
        st.write(text[:200])

        st.subheader("📌 Feedback")
        st.write("""
        - Reduce filler words  
        - Maintain eye contact  
        - Speak clearly and confidently  
        """)