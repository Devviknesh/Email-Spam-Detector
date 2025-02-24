from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

data = [
    ("Win a FREE iPhone now!", "spam"),
    ("Meeting at 3 PM in the office.", "ham"),
    ("Congratulations! You won a lottery!", "spam"),
    ("Please review the attached report.", "ham"),
]
// thenunmber pf usern to be includefor the mostt of the technologies used in this therefore it is used in many ways ti aadvanscce diibdf 
clf = MultinomialNB()
clf.fit(X_train_counts, y_train)

test_email = input("Enter an email: ")
pred = clf.predict(vectorizer.transform([test_email]))

print("Spam" if pred[0] == "spam" else "Not Spam")
