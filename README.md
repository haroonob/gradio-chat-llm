# gradio-chat-llm
# ✈️  Gradio Chatbot

Gradio CHAT is an AI-powered chatbot for an airline that helps customers with ticket prices, travel inquiries, and more. It features natural language processing, text-to-speech, speech-to-text transcription, and AI-generated travel images.

---

## 🚀 **Project Features**
- **Chatbot Integration**: Provides airline-related information.
- **Ticket Price Lookup**: Fetches flight ticket prices for major cities.
- **Text-to-Speech**: Converts chatbot responses into speech using OpenAI's TTS model.
- **Speech-to-Text (Whisper)**: Converts user speech to text using OpenAI Whisper.
- **Image Generation**: Generates AI images of travel destinations.
- **Interactive UI**: Built using Gradio for a seamless user experience.

---


---

## 🛠 **Setup & Installation**

### **1️⃣ Prerequisites**
Ensure you have:
- Python  3.12.8 or later
- Pip installed

### **2️⃣ Clone the Repository**
git clone https://github.com/haroonob/gradio-chat-llm
cd gradio-chat-llm


### **23️⃣  Install Dependencies**
 
pip install -r requirements.txt

### **4️⃣  Install Dependencies**
OPENAI_API_KEY=your_openai_api_key

### **5️⃣  Run the Application**

Modules & Functionality
🔹 1. config.py
Handles environment variables.

🔹 2. chat.py
Manages chatbot conversation logic.
Calls tools when needed (e.g., ticket price lookup).
Uses OpenAI's GPT model.
🔹 3. tools.py
Handles airline-related queries.
Fetches ticket prices for major cities.
🔹 4. audio.py
Converts text responses to speech (talker()).
Converts user speech to text using OpenAI Whisper (transcribe_with_whisper()).
🔹 5. image_generator.py
Uses OpenAI's DALL·E to generate travel destination images.
🔹 6. ui.py
Creates an interactive chat interface with Gradio.
📡 Running Tests
Run unit tests with:

bash
Copy
Edit
pytest tests/
📜 License
This project is licensed under the MIT License.

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.

yaml
Copy
Edit

---

## 📌 **requirements.txt**
```txt
openai
gradio
python-dotenv
pillow
pytest
This should get your project running smoothly. Let me know if you need any modifications! 🚀



