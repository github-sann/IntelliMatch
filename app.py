from flask import Flask, render_template, request, redirect
import pandas as pd
import torch
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import fuzz
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

# Load pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')
model.eval()

# Initialize SentenceTransformer model
sentence_model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

data = pd.read_csv("data.csv")  # Replace with your actual CSV file path

correct_answers = 0
incorrect_answers = 0
current_question_index = 0

def get_bert_embedding(text):
    # Tokenize input text
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    # Forward pass through BERT model
    with torch.no_grad():
        outputs = model(**inputs)
        # Use the output of the [CLS] token as the sentence embedding
        sentence_embedding = torch.mean(outputs.last_hidden_state[:, 0, :], dim=0)
    return sentence_embedding.numpy()

@app.route('/')
@app.route('/')
def index():
    global current_question_index
    total_questions = len(data)  # Get the total number of questions
    if current_question_index < total_questions:
        question = data['Question'].iloc[current_question_index]
        return render_template('index.html', question=question, 
                               question_index=current_question_index,
                               total_questions=total_questions)
    else:
        return redirect('/results')  

@app.route('/evaluate', methods=['POST'])
def evaluate():
    global current_question_index, correct_answers, incorrect_answers
    user_answer = request.form['answer']
    question_index = int(request.form['question_index'])

    user_embedding = sentence_model.encode(user_answer)

    dataset_answers = data['Answer']

    # Calculate similarity scores between user answer and dataset answers
    similarities = []
    for answer in dataset_answers:
        answer_embedding = sentence_model.encode(answer)
        similarity = cosine_similarity([user_embedding], [answer_embedding])[0][0]
        similarities.append(similarity)

        # Additionally, check for fuzzy matching
        fuzzy_similarity = fuzz.partial_ratio(user_answer.lower(), answer.lower()) / 100.0
        similarities[-1] = max(similarities[-1], fuzzy_similarity)

    best_match_index = similarities.index(max(similarities))
    best_match_score = similarities[best_match_index]

    if best_match_score > 0.7:
        correct_answers += 1
    else:
        incorrect_answers += 1

    current_question_index += 1  # Move to the next question
    return redirect('/')  # Redirect back to the quiz (or results if it's the last question)

@app.route('/results')
def results():
    return render_template('results.html', 
                           correct_answers=correct_answers,
                           incorrect_answers=incorrect_answers)

# if __name__ == '__main__':
#     app.run(debug=True)