document.getElementById('sentimentForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const textInput = document.getElementById('textInput').value;
    const resultDiv = document.getElementById('result');
    
    // Show loading state
    resultDiv.textContent = 'Analyzing...';
    resultDiv.className = 'result';

    try {
        const response = await fetch('http://localhost:8000/api/sentiment-analyser/post/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ sentence: textInput }),
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        
        if (data.sentiment) {
            resultDiv.textContent = `Sentiment: ${data.sentiment}`;
            resultDiv.className = `result ${data.sentiment.toLowerCase()}`;
        } else if (data.error) {
            resultDiv.textContent = `Error: ${data.error}`;
            resultDiv.className = 'result';
        }
    } catch (error) {
        resultDiv.textContent = `Error: ${error.message}`;
        resultDiv.className = 'result';
    }
});