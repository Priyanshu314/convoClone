from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def find_most_relevant_context(user_message, context_list):
    if not context_list:
        return None
    vectorizer = TfidfVectorizer()
    documents = [user_message] + context_list
    tfidf_matrix = vectorizer.fit_transform(documents)
    similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
    most_similar_index = similarities.argmax()
    return context_list[most_similar_index]
