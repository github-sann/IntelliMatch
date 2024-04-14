// Fetch questions from the backend
fetch('/get_questions')
  .then(response => response.text())
  .then(questionsHtml => {
    document.getElementById('questions-container').innerHTML = questionsHtml;
  });

// Submit answers to the backend
function submitAnswers() {
  const answers = {};
  const answerInputs = document.querySelectorAll('input[type="text"]');
  answerInputs.forEach(input => {
    answers[input.name] = input.value;
  });

  // Add event listener to the "Start Quiz" button
document.getElementById('start-button').addEventListener('click', () => {
    document.getElementById('quiz-container').style.display = 'block'; 
    // Hide the start button after it's clicked
    document.getElementById('start-button').style.display = 'none';
  
    // Fetch and display questions (same as before)
    fetch('/get_questions')
      .then(response => response.text())
      .then(questionsHtml => {
        document.getElementById('questions-container').innerHTML = questionsHtml;
      });
  });
  

  // Send answers to the backend for evaluation
  fetch('/evaluate_answers', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(answers)
  })
  .then(response => response.text())
  .then(result => {
    // Redirect to results page
    window.location.href = `/results?scores=${result}`;
  });
}