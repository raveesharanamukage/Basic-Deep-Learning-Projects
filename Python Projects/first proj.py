print("Imdb movie review sentiment analysis")
def proj(a,b):
    if a==b:
        return True
    else:
        return False
    
class MovieReview:
    def __init__(self, review, sentiment):
        self.review = review
        self.sentiment = sentiment

    def __str__(self):
        return f"Review: {self.review}, Sentiment: {self.sentiment}"