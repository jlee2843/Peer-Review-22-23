from transformers import pipeline


class AdvancedNLP:
    def __init__(self, model_name='distilbert-base-uncased-finetuned-sst-2-english'):
        self.classifier = pipeline('sentiment-analysis', model=model_name)

    def analyze_sentiments(self, texts):
        return self.classifier(texts)
