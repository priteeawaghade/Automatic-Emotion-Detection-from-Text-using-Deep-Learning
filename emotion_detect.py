from transformers import pipeline
import json

# Load pre-trained emotion detection model
emotion_classifier = pipeline(
    task="text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

def detect_emotion(text):
    """
    Detects dominant emotion from text
    Returns emotion and confidence score
    """
    predictions = emotion_classifier(text)[0]

    # Get emotion with highest confidence
    best_emotion = max(predictions, key=lambda x: x['score'])

    result = {
        "emotion": best_emotion["label"],
        "confidence": round(best_emotion["score"], 2)
    }

    return result


# -------- Main Program --------
if __name__ == "__main__":
    text_input = input("Enter text: ")

    output = detect_emotion(text_input)

    print("\nEmotion Detection Result:")
    print(json.dumps(output, indent=2))
