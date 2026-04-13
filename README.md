# 🎓 RAG-Based AI Teaching Assistant

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Whisper](https://img.shields.io/badge/OpenAI-Whisper-green?style=for-the-badge&logo=openai)
![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-orange?style=for-the-badge)

The **RAG-Based AI Teaching Assistant** is an innovative and intelligent educational tool meticulously designed to help students navigate extensive course materials seamlessly. In today's digital learning environments, students often spend hours manually scrubbing through long lecture recordings to find specific concepts. This project eliminates that friction by deploying a cutting-edge **Retrieval-Augmented Generation (RAG)** pipeline entirely on your local machine.

It autonomously processes course videos, extracts the audio, and performs highly accurate transcriptions using OpenAI's powerful **Whisper** model. Once the audio is transcribed, the system breaks the text into manageable, timestamp-tagged chunks. To deeply understand the semantic meaning of these lecture segments, the assistant generates high-dimensional vector embeddings using Ollama's `bge-m3` model. These embeddings are efficiently stored using Pandas and Joblib, creating a robust, easily queryable knowledge base that perfectly represents the entirety of your course curriculum.

When a student asks a natural language question, the system instantly embeds their query and performs a rapid semantic search across the entire course knowledge base using cosine similarity via Scikit-Learn. It then leverages a powerful local Large Language Model—specifically **Llama 3.2** running via **Ollama**—to synthesize this retrieved context. The LLM generates a conversational, human-like response that not only answers the question but explicitly guides the student to the exact video title, tutorial number, and specific timestamp where the topic is taught.

---

## ✨ Key Features
* **Automated Data Pipeline:** Seamless Video-to-Audio conversion utilizing `ffmpeg`.
* **Precise Extraction:** High-fidelity audio transcription and intelligent timestamp chunking powered by Whisper.
* **Rapid Retrieval:** Efficient local vector embeddings and semantic search mechanisms using Scikit-Learn and Pandas.
* **Secure & Local:** 100% private LLM inference using Ollama, guaranteeing secure, context-aware, and highly accurate educational guidance without relying on costly external APIs.

---

## 🛠️ Prerequisites

Before running the project, ensure you have the following installed on your system:
1. **Python 3.8+**
2. **FFmpeg:** Required for extracting audio from video files.
3. **Ollama:** Installed and running locally.
   * You need to pull the embedding model: `ollama run bge-m3`
   * You need to pull the chat model: `ollama run llama3.2`

---

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/RedAro/RAG-Based-AI-Teaching-Assistant.git
   cd RAG-Based-AI-Teaching-Assistant
   ```

2. **Install the required Python packages:**
   ```bash
   pip install -r requirements.txt
   pip install openai-whisper
   ```

---

## 📖 How to Use on Your Own Data

Follow these steps to process your course videos and start asking questions:

### Step 1: Collect Your Videos
Create a folder named `videos/` in the root directory and move all your course `.mp4` files into it. 
*(Recommended naming convention: `01 Video Title.mp4`)*

### Step 2: Convert to Audio
Extract the audio from your video files by running the extraction script. This will populate the `audios/` folder.
```bash
python video_to_mp3.py
```

### Step 3: Transcribe & Chunk (Convert MP3 to JSON)
Generate transcriptions with timestamps using Whisper. The outputs will be saved in the `jsons/` directory.
```bash
python mp3_to_json.py
```

### Step 4: Generate Embeddings
Convert the JSON chunks into vector embeddings using Ollama's `bge-m3` model. This creates a highly efficient `embeddings.joblib` database.
```bash
python preprocess_json.py
```

### Step 5: Ask Questions!
Run the interactive inference script. Type your question, and the local Llama 3.2 model will guide you to the exact video and timestamp.
```bash
python process_incoming.py
```

---

## 📂 Project Structure

```text
├── videos/                 # Put your raw course videos here
├── audios/                 # Generated MP3 files
├── jsons/                  # Generated transcriptions and chunks
├── embeddings.joblib       # Vector database
├── requirements.txt        # Python dependencies
├── video_to_mp3.py         # Script to convert mp4 to mp3
├── mp3_to_json.py          # Script to transcribe audio via Whisper
├── preprocess_json.py      # Script to generate vector embeddings
├── process_incoming.py     # Main RAG inference script
└── README.md               # Project documentation
```
