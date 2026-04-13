# RAG-Based AI Teaching Assistant

The RAG-Based AI Teaching Assistant is an innovative and intelligent educational tool meticulously designed to help students navigate extensive course materials seamlessly. In today's digital learning environments, students often spend hours manually scrubbing through long lecture recordings to find specific concepts. This project eliminates that friction by deploying a cutting-edge Retrieval-Augmented Generation (RAG) pipeline entirely on your local machine. It autonomously processes course videos, extracts the audio, and performs highly accurate transcriptions using OpenAI's powerful Whisper model.

Once the audio is transcribed, the system breaks the text into manageable, timestamp-tagged chunks. To deeply understand the semantic meaning of these lecture segments, the assistant generates high-dimensional vector embeddings using Ollama's `bge-m3` model. These embeddings are then stored efficiently using Pandas and Joblib, creating a robust, easily queryable knowledge base that perfectly represents the entirety of your course curriculum.

When a student asks a natural language question, the system instantly embeds their query and performs a rapid semantic search across the entire course knowledge base using cosine similarity via Scikit-Learn. This ensures the AI retrieves only the most relevant contextual video chunks. Finally, it leverages a powerful local Large Language Model—specifically Llama 3.2 running via Ollama—to synthesize this retrieved context. The LLM generates a conversational, human-like response that not only answers the question but explicitly guides the student to the exact video title, tutorial number, and specific timestamp where the topic is taught. 

## How to use this RAG AI Teaching assistant on your own data

### Step 1 - Collect your videos
Move all your video files to the videos folder

### Step 2 - Convert to mp3
Convert all the video files to mp3 by ruunning video_to_mp3

### Step 3 - Convert mp3 to json 
Convert all the mp3 files to json by ruunning mp3_to_json

### Step 4 - Convert the json files to Vectors
Use the file preprocess_json to convert the json files to a dataframe with Embeddings and save it as a joblib pickle

### Step 5 - Prompt generation and feeding to LLM
Read the joblib file and load it into the memory. Then create a relevant prompt as per the user query and feed it to the LLM
