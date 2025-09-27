from fastapi import FastAPI

app = FastAPI()

# ข้อมูลเพลงจำลอง
songs = [
    {"id": 1, "title": "อีกกี่วันจะได้พบเธอ", "artist": "MKLG ก้านกล้วย & MPLG เปตอง"},
    {"id": 2, "title": "ไม่มีวันไหนไม่รักเธอ", "artist": "MikeMek & Forever"}
]

@app.get("/")
def root():
    return {"message": "API พร้อมใช้งานแล้ว"}

@app.get("/songs")
def get_songs():
    return songs

@app.post("/songs")
def add_song(song: dict):
    songs.append(song)
    return {"status": "ok", "data": song}
