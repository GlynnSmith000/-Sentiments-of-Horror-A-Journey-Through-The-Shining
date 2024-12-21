# Sentiment Analysis and Topic Modeling on *The Shinning* (Stephen King)

This notebook analyzes the text of *The Shinning* by Stephen King through two main techniques: sentiment analysis and topic modeling. Below is an outline of the steps taken throughout the analysis.

## 1. **Text Preprocessing and Chapter Extraction**
The first step was to read in the full text of *The Shinning* and extract its chapters. The text was split by identifying the chatper identifier pattern in the text and each chapter was saved as a separate text file for individual analysis. Quotations, commas, paretheses, etc. were removed from the text for sentiment analysis. I had to go into all 58 chapter text files and manually separate each paragraph by cross referencing the original text. Indentations were lost in the online conversion process (this would of made it easy to automate the separation in each chapter). There is a large amount of conversational text, which makes it more difficult to split the text into paragraphs. Others could split the text in different spots because of this. This process allows us to focus on each chapter independently (and later each chapter's paragraphs) when performing sentiment analysis and topic modeling.

## 2. **Sentiment Analysis**
Sentiment analysis was conducted using the SentimentIntensityAnalyzer from the `nltk` library. The process involved analyzing the emotional tone of each chapter by evaluating the compound sentiment score for each sentence. The chapters were then classified into five sentiment categories based on their average sentiment score:

- Strong Positive
- Weak Positive
- Neutral
- Weak Negative
- Strong Negative

This classification helps to understand how the emotional tone shifts across the chapters.

## 3. **Topic Modeling (LDA)**
I thought it would be cool to try to find the topics for each paragraph. Latent Dirichlet Allocation (LDA) was applied to uncover the underlying topics in *The Shinning*. The text of each chapter was then processed further by removing stopwords, punctuation, and applying lemmatization. After preprocessing, a dictionary and document-term matrix were created, and the LDA model was trained to identify the main topics in the text. The model generated a set of topics, each represented by a collection of words that frequently co-occur in the text. The results were visualized using pyLDAvis, which provides an interactive visualization to explore the topics, their relationships, and the chapters belonging to the topic clusters. 

## 4. **Visualization of Sentiment Analysis**
To visualize the sentiment trends, a line plot was created showing the average sentiment score for each chapter. This visualization helps to track the emotional trajectory of the book, highlighting moments of positive, neutral, and negative sentiment across the chapters.

## 5. **Paragraph-Level Sentiment Analysis**
In addition to chapter-level sentiment analysis, sentiment was analyzed at the paragraph level to provide a more granular view of the emotional tone. Each paragraph in the chapters was processed, and a sentiment score was assigned to it. These results were stored in a structured format, allowing for further exploration of how the sentiment varies within individual chapters and scenes.
