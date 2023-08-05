from transformers import RobertaTokenizerFast, TFRobertaForSequenceClassification, pipeline
import data_manage

tokenizer = RobertaTokenizerFast.from_pretrained("arpanghoshal/EmoRoBERTa")
model = TFRobertaForSequenceClassification.from_pretrained("arpanghoshal/EmoRoBERTa")

emotion = pipeline('sentiment-analysis', 
                    model='arpanghoshal/EmoRoBERTa')

def emotion_classify(text):
    emotion_labels = emotion(text)
    data_manage.add_data(text, emotion_labels[0]['label'], emotion_labels[0]['score'])