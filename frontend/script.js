function sendMessage() {
    const question = document.getElementById('question').value;
    fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: question })
    })
    .then(response => response.json())
    .then(data => {
        const chatBox = document.getElementById('chat-box');
        chatBox.innerHTML += `<p><strong>You:</strong> ${question}</p>`;
        chatBox.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
        document.getElementById('question').value = '';
    });
}

function startNewChat() {
    document.getElementById('chat-box').innerHTML = '';
}

function viewHistory() {
    fetch('/history')
    .then(response => response.json())
    .then(data => {
        const chatBox = document.getElementById('chat-box');
        chatBox.innerHTML = '<h3>Chat History:</h3>';
        data.forEach(item => {
            chatBox.innerHTML += `<p><strong>You:</strong> ${item[0]}<br><strong>Bot:</strong> ${item[1]}<br><em>${item[2]}</em></p><hr>`;
        });
    });
}
