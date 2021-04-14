from google.cloud import language_v1
import os

class GNaturalLanguage:
    def __init__(self):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"
        self.client = language_v1.LanguageServiceClient()
    
    def sentiment_analysis(self, text):        
        document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
        sentiment = self.client.analyze_sentiment(request={'document': document}).document_sentiment
        return sentiment.score, sentiment.magnitude