import whisper
import json
import os

os.makedirs("jsons", exist_ok=True)
model = whisper.load_model("large-v2")
audios = os.listdir("audios")
for audio in audios: 
    if("_" in audio):
        number = audio.split("_")[0]
        title = audio.split("_", 1)[1][:-4]
        print(number, title)
        result = model.transcribe(audio = f"audios/{audio}", language="hi", task="translate", word_timestamps=False)
        chunks = []
        for segment in result["segments"]:
            chunks.append({"number": number, "title": title, "start": segment["start"], "end": segment["end"], "text": segment["text"]})
        chunks_with_metadata = {"chunks": chunks, "text": result["text"]}
        output_path = f"jsons/{audio}.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(chunks_with_metadata, f, ensure_ascii=False)
        print(f"Saved: {output_path}")