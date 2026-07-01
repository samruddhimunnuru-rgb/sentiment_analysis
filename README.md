<img width="804" height="684" alt="Screenshot 2026-04-05 115757" src="https://github.com/user-attachments/assets/3e33cba5-28d4-428c-ba50-2e61f99dc36c" />
## Aspect-Based Sentiment Analysis on App Reviews

# Project Overview

This project performs Aspect-Based Sentiment Analysis (ABSA) on user reviews stored in a CSV file. Instead of classifying the entire review with a single sentiment, the system identifies sentiments for specific aspects such as:

* UI
* Performance
* Features

The project uses TextBlob for Natural Language Processing (NLP) and sentiment analysis.



# Features

* Reads reviews from a CSV dataset
* Automatically detects the review text column
* Performs sentiment analysis using TextBlob
* Extracts aspect-specific sentiments
* Generates a results table
* Saves output to a CSV file
* Visualizes sentiment distribution using bar charts



#  Technologies Used

* Python 3.x
* Pandas
* TextBlob
* Matplotlib

#  Project Structure

text
project-folder/
│
├── reviews.csv
├── main.py
├── output_results.csv
├── README.md
└── requirements.txt

#  Installation

1. Clone the repository

bash
git clone https://github.com/your-username/aspect-based-sentiment-analysis.git
cd aspect-based-sentiment-analysis


 2. Install dependencies

bash
pip install -r requirements.txt


3. Download TextBlob corpora

bash
python -m textblob.download_corpora


 Running the Project

Place your dataset (`reviews.csv`) inside the project folder and run:

bash
python main.py

#  Dataset Format

The CSV file should contain one of the following columns:

* review
* content
* review_text
* text

Example:

#  review                          

 Great UI and smooth performance 
 App crashes frequently          
 Useful features and nice design 

 Aspects Analyzed

 UI

# Keywords:

* ui
* design
* interface
* layout

 Performance

# Keywords:

* slow
* fast
* lag
* crash
* loading

#  Features

Keywords:

* feature
* option
* tool
* function



 # Working of the System

1. Load review dataset from CSV.
2. Detect the review text column automatically.
3. Split reviews into sentences using TextBlob.
4. Search for aspect keywords.
5. Compute sentiment polarity:

   * Positive (polarity > 0)
   * Negative (polarity < 0)
   * Neutral (polarity = 0)
6. Store results in a DataFrame.
7. Export results to `output_results.csv`.
8. Display sentiment distribution graph.



#  Output

CSV Output

The generated file:

text
output_results.csv

# contains:

 Review                     UI        Performance  Features 
 
 Great UI and fast loading  Positive  Positive     N/A      

# Visualization

A bar chart displays the count of:

* Positive sentiments
* Negative sentiments
* Neutral sentiments

for each aspect.


# Requirements

Create a `requirements.txt` file containing:

text
pandas
textblob
matplotlib

# Install using:

bash
pip install -r requirements.txt


# Future Improvements

* Use advanced NLP models such as BERT
* Add more aspects dynamically
* Build a web interface using Flask or Streamlit
* Support multiple languages
* Improve keyword extraction using machine learning

#  Author

Developed as a Python NLP project for Aspect-Based Sentiment Analysis using TextBlob.


