from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

# เปิด CORS ให้ Softr เรียก API ได้
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve ไฟล์เพลงและรูปภาพ
app.mount("/media/songs", StaticFiles(directory="media/songs"), name="songs")
app.mount("/media/album_covers", StaticFiles(directory="media/album_covers"), name="album_covers")

# โมเดลข้อมูลเพลง
class Song(BaseModel):
    title: str
    song_format: str
    artist: str
    album: str
    album_cover_url: str
    song_url: str
    composer: str
    producer: str
    arranger: str
    musician: str
    phone: str
    email: str
    facebook: str
    release_date: str
    genre: str
    upc_ean: str
    isrc: str
    explicit: bool
    content_id: str

# Mock database
songs_data = []

@app.get("/songs")
def get_songs():
    return songs_data

@app.post("/songs")
def add_song(song: Song):
    new_id = len(songs_data) + 1
    song_dict = song.dict()
    song_dict["id"] = new_id
    songs_data.append(song_dict)
    return song_dict
