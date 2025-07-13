# 💬 Cohere Chatbot API (Flask App)

A responsive and modern AI chatbot built using **Flask** for the backend and **Cohere's NLP API** for intelligent response generation. It features a clean web interface, real-time communication, and professional UI — ideal for learning, demos, and AI integration projects.

---

## 🌟 Features

- ⚡ **Real-time chatbot** using Cohere's `command` model
- 🧠 Built with **Python (Flask)** for fast backend development
- 🎨 Modern and clean **HTML + CSS UI**
- 🔐 API keys managed securely via `.env`
- 🛡️ `.gitignore` added to protect sensitive files
- 🌐 Easily deployable on platforms like Render, Replit, or Heroku

---

## 📁 Project Structure

chatbot-app/
├── backend/
│ └── app.py # Flask app logic
├── templates/
│ └── index.html # Chatbot UI
├── .env # Contains COHERE_API_KEY (not pushed)
├── .gitignore
├── README.md

yaml
Copy
Edit

---

## ⚙️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **AI Engine**: [Cohere API](https://cohere.com)
- **Hosting Ready**: Render / Replit / Heroku

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Devinarukula57/Chatbot_API.git
cd Chatbot_API
2. Install Python dependencies
bash
Copy
Edit
pip install flask cohere python-dotenv
3. Set up .env file
Create a .env file in the root directory:

env
Copy
Edit
COHERE_API_KEY=your_actual_cohere_api_key
🔒 Never share your API key publicly!

4. Run the Flask app
bash
Copy
Edit
python backend/app.py
Then open http://localhost:5000 in your browser.

