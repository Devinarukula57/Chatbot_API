💬 AI Chatbot using Cohere API

________________________________________

🧠 Project Summary

This project is a full-stack, web-based AI chatbot application built using Python Flask for the backend and Cohere's NLP API for generating intelligent, human-like responses. It enables real-time conversation through a clean and responsive HTML/CSS frontend. The chatbot is enhanced with context-aware memory and optionally stores chat history using MongoDB. This project demonstrates how to integrate an AI language model into a complete web application with persistent storage and a user-friendly interface.
________________________________________

🔧 Features

•	✅ AI-powered chat using Cohere’s Command Language Model
•	🧠 Contextual memory: Maintains the last 10 messages to keep the flow natural
•	💾 Persistent chat history: Stores messages using MongoDB per user session
•	🔁 Reset support: Clear current session or delete full chat history
•	📱 Responsive UI: Works on mobile, tablet, and desktop devices
•	🎨 Clean layout: Includes styled, color-coded chat bubbles and input area


| 💡 Category          | 🛠️ Technology           | 📄 Purpose / Role                                            |
| -------------------- | ------------------------ | ------------------------------------------------------------ |
| Programming Language | **Python**               | Backend development and AI API integration                   |
| Web Framework        | **Flask**                | Handles routes, user requests, and templates                 |
| AI/NLP API           | **Cohere API**           | Generates AI-based responses from user input                 |
| Database             | **MongoDB**              | Stores chat history and session messages                     |
| Frontend (UI)        | **HTML & CSS**           | Builds and styles the chatbot interface for all device types |
| Client-side Logic    | **JavaScript (Vanilla)** | Sends messages and handles frontend updates dynamically      |
| Version Control      | **Git**                  | Tracks code changes and history                              |
| Repository Hosting   | **GitHub**               | Hosts and publishes the project code                         |
| Terminal Tool        | **Git Bash / CMD**       | Runs local Git, Flask server, and pip commands               |

.env file
COHERE_API_KEY=your_actual_cohere_api_key
MONGO_URI=mongodb://localhost:27017

