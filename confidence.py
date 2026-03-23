def calculate_confidence(emotions, filler_count, text):

    # Emotion Score (50)
    if len(emotions) > 0:
        positive = emotions.count("happy") + emotions.count("neutral")
        emotion_score = (positive / len(emotions)) * 50
    else:
        emotion_score = 0

    # Filler Score (30)
    filler_score = max(0, 30 - filler_count)

    # Speech Score (20)
    word_count = len(text.split())
    speech_score = 20 if word_count > 20 else 10

    total = emotion_score + filler_score + speech_score

    return round(total, 2)