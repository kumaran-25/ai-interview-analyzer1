import gradio as gr
import os
import shutil

from utils import extract_frames
from emotion import analyze_emotions
from speech import extract_audio, speech_to_text, count_filler_words
from confidence import calculate_confidence

# Create folders
os.makedirs("uploads", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

def analyze(video_file):

    video_path = "uploads/input_video.mp4"
    shutil.copy(video_file, video_path)

    # Processing
    frames = extract_frames(video_path)
    emotions = analyze_emotions(frames)
    audio = extract_audio(video_path)
    text = speech_to_text(audio)
    fillers = count_filler_words(text)
    score = calculate_confidence(emotions, fillers, text)

    # Emoji feedback
    if score > 75:
        status = "🟢 Excellent"
    elif score > 50:
        status = "🟡 Good"
    else:
        status = "🔴 Needs Improvement"

    return (
        f"{score} / 100",
        status,
        ", ".join(emotions[:5]),
        fillers,
        text[:200]
    )

# 🎨 Custom UI
with gr.Blocks(theme=gr.themes.Soft()) as app:

    gr.Markdown("""
    # 🎤 AI Interview Performance Analyzer
    ### Analyze your interview skills using AI 🚀
    Upload your video and get instant feedback!
    """)

    with gr.Row():
        video_input = gr.Video(label="📤 Upload Interview Video")

    with gr.Row():
        analyze_btn = gr.Button("🔍 Analyze", variant="primary")

    gr.Markdown("## 📊 Results")

    with gr.Row():
        score_output = gr.Textbox(label="🎯 Confidence Score")
        status_output = gr.Textbox(label="📈 Performance Level")

    with gr.Row():
        emotion_output = gr.Textbox(label="😊 Emotions Detected")
        filler_output = gr.Textbox(label="🗣️ Filler Words Count")

    gr.Markdown("### 📝 Speech Preview")
    speech_output = gr.Textbox(lines=4)

    analyze_btn.click(
        fn=analyze,
        inputs=video_input,
        outputs=[
            score_output,
            status_output,
            emotion_output,
            filler_output,
            speech_output
        ]
    )

app.launch(share=True)