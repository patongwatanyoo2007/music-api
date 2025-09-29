from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# เปิด CORS ให้ Softr เรียก API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve ไฟล์เพลงและรูปอัลบั้ม
app.mount("/media/songs", StaticFiles(directory="media/songs"), name="songs")
app.mount("/media/album_covers", StaticFiles(directory="media/album_covers"), name="album_covers")

songs_data = [
    {
        "id":1,
        "title":"อีกกี่วันจะได้พบเธอ",
        "song_format":"WAV",
        "artist":"MKLG ก้านกล้วย & MPLG เปตอง",
        "album":"Album Name",
        "album_cover_url":"https://music-api-lxh4.onrender.com/media/album_covers/album1.jpg",
        "song_url":"https://music-api-lxh4.onrender.com/media/songs/song1.wav",
        "composer":"วทัญญู กันหาวงศ์",
        "producer":"วทัญญู กันหาวงศ์",
        "arranger":"วทัญญู กันหาวงศ์",
        "musician":"วทัญญู กันหาวงศ์",
        "phone":"0812345678",
        "email":"example@example.com",
        "facebook":"https://facebook.com/artist",
        "release_date":"2025-09-29",
        "genre":"Pop",
        "upc_ean":"123456789012",
        "isrc":"TH-A01-20-00001",
        "explicit":False,
        "content_id":"content_001"
    }
]

@app.get("/songs")
def get_songs():
    return songs_data
