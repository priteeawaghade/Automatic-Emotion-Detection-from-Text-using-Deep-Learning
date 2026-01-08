# Automatic-Emotion-Detection-from-Text-using-Deep-Learning
Automatic Emotion Detection from Text is a Natural Language Processing (NLP) based deep learning project that identifies the dominant emotional state expressed in written text. The system analyzes user-provided text such as chat messages, tweets, emails, or reviews and predicts the emotion conveyed by the author along with a confidence score.
## 🎯 Objective

The objective of this project is to:
- Automatically analyze textual input
- Detect the dominant emotion conveyed by the author
- Provide a confidence score for the prediction

---

## 🧠 Emotions Supported

The model classifies text into the following emotions:
- Joy
- Sadness
- Anger
- Fear
- Surprise
- Disgust
- Neutral

---

## ⚙️ Technologies Used

- Python
- Hugging Face Transformers
- DistilRoBERTa (Transformer-based Deep Learning Model)
- PyTorch
- JSON (for structured output)

---

## 🔄 Project Workflow

1. User provides a text input
2. Text is preprocessed and tokenized
3. Contextual embeddings are generated using a transformer model
4. The deep learning model predicts emotion probabilities
5. The dominant emotion with the highest confidence is selected
6. Output is returned in JSON format

---

## 📥 Input

**Example:**
I feel very lonely and tired of everything.

---

## 📤 Output

The output is displayed in JSON format.

```json
{
  "emotion": "sadness",
  "confidence": 0.89
}
How to Run the Project
Step 1: Install Dependencies
pip install transformers torch

Step 2: Run the Program
python emotion_detection.py

Step 3: Enter Text

Enter any sentence or paragraph when prompted to get the emotion prediction.

📊 Evaluation Metrics

Accuracy

Precision

Recall

F1-Score

Confusion Matrix

🧩 Applications

Mental health monitoring

Social media emotion analysis

Customer feedback analysis

Chatbots and virtual assistants

Human–computer interaction systems

📌 Conclusion

This project demonstrates the effective use of deep learning and transformer-based models for automatic emotion detection from text. By leveraging contextual embeddings, the system accurately captures emotional nuances and provides reliable predictions, making it suitable for academic and practical applications.
