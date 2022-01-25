# Movie Recommendation System
This machine learning project implements a content-based movie recommendation system in Python that predicts or suggests movies based on user's movie interests. 

## Database
IDBM dataset

### API

## Approach:
![App Screenshot](images/contentbased.JPG)

Content based algorithm attempts to figure out the user's favourite aspects of an item and then recommends similar items that includes those aspects. In this project, attributes such as genre, top 3 actors of the movie, overview/plot, director, and keywords representing the movie are used to make suggestions for the users. These features can provide a great insight on understanding users' preferences and help to produce better movie recommendations that are similar to their chosen movie. 

Those features will then be processed using TF-IDF Vectorizer, an algorithm that transforms text into meaningful representation of numbers which will be used to fit machine algorithm for prediction. Each term is assigned a dimension and associated vector that corresponds to the frequency of the term in the document, which allows for the Cosine Similarity measurement to distinguish and compare documents to each other based upon their similarities and overlap of subject matter. 

### Cosine similarity
![App Screenshot](images/cosinesim.JPG)
Aforementioned, cosine similarity gives a useful measure of how similar two documents are likely to be in terms of their subject matter. It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.


##3 Deploy
streamlit
