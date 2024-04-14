# IntelliMatch: AI-Driven Question-Answer Matching System

## Overview

IntelliMatch is an AI-powered web application designed to match user-provided answers with pre-defined questions and answers using advanced natural language processing techniques. The system utilizes BERT embeddings, cosine similarity, and fuzzy string matching to evaluate the correctness of user answers.

## Features

- **BERT Embeddings**: Utilizes pre-trained BERT models to generate embeddings for both questions and user-provided answers.
- **Cosine Similarity**: Calculates similarity scores between user answers and dataset answers using cosine similarity metrics.
- **Fuzzy String Matching**: Incorporates fuzzy string matching to handle minor variations and improve matching accuracy.
- **Web Interface**: Provides a user-friendly web interface built with Flask for users to interact with the question-answer matching system.

## Setup and Installation

1. Clone the repository:

2. Install dependencies:

3. Prepare the dataset:

- Replace `data.csv` with your own CSV file containing questions and answers.

4. Run the application:

5. Access the application in your web browser at `http://localhost:5000`.

## Usage

1. Access the home page to start the quiz.
2. Answer each question and submit your response.
3. The system will evaluate your answer based on similarity scores and provide instant feedback.
4. After completing the quiz, view the results page to see your score.

## Technologies Used

- Python
- Flask
- pandas
- PyTorch
- Hugging Face Transformers
- fuzzywuzzy
- sentence-transformers

## Contributors

- Savitha
-

## Acknowledgments

- Inspired by the advancements in natural language processing and question-answer matching techniques.
- Special thanks to the open-source community for providing valuable tools and resources.
