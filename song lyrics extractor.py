import customtkinter as ctk
import requests
from bs4 import BeautifulSoup

class LyricsApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Lyrics Extractor")
        self.geometry("500x600")
        self.configure(bg_color='gray20')
        self.create_widgets()

    def create_widgets(self):
        self.search_frame = ctk.CTkFrame(self, bg_color='gray20')
        self.search_frame.pack(pady=20, padx=10)

        self.song_label = ctk.CTkLabel(self.search_frame, text="Song Name:", font=('Helvetica', 14), text_color='white')
        self.song_label.grid(row=0, column=0, pady=10, padx=5, sticky="w")

        self.song_entry = ctk.CTkEntry(self.search_frame, placeholder_text="Enter song name", width=250, font=('Helvetica', 14))
        self.song_entry.grid(row=0, column=1, pady=10, padx=5)

        self.artist_label = ctk.CTkLabel(self.search_frame, text="Artist Name:", font=('Helvetica', 14), text_color='white')
        self.artist_label.grid(row=1, column=0, pady=10, padx=5, sticky="w")

        self.artist_entry = ctk.CTkEntry(self.search_frame, placeholder_text="Enter artist name", width=250, font=('Helvetica', 14))
        self.artist_entry.grid(row=1, column=1, pady=10, padx=5)

        self.search_button = ctk.CTkButton(self.search_frame, text="Search Lyrics", command=self.search_lyrics, fg_color='blue', hover_color='darkblue')
        self.search_button.grid(row=2, columnspan=2, pady=20)

        self.result_frame = ctk.CTkFrame(self, bg_color='gray20')
        self.result_frame.pack(expand=True, fill='both', padx=10, pady=10)

        self.lyrics_area = ctk.CTkTextbox(self.result_frame, font=('Helvetica', 12), wrap='word', state='disabled', text_color='white', bg_color='black')
        self.lyrics_area.pack(expand=True, fill='both')

    def search_lyrics(self):
        song_name = self.song_entry.get().strip()
        artist_name = self.artist_entry.get().strip()

        if song_name and artist_name:
            lyrics = self.fetch_lyrics(song_name, artist_name)
            self.display_lyrics(lyrics)
        else:
            self.display_lyrics("Please enter both song and artist name.")

    def fetch_lyrics(self, song_name, artist_name):
        search_url = f"https://www.azlyrics.com/lyrics/{artist_name.replace(' ', '').lower()}/{song_name.replace(' ', '').lower()}.html"
        response = requests.get(search_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            lyrics_div = soup.find_all('div', class_=None, id=None)[0]
            return lyrics_div.get_text(separator="\n").strip()
        else:
            return "Lyrics not found. Please check the song and artist name or try a different source."

    def display_lyrics(self, lyrics):
        self.lyrics_area.configure(state='normal')
        self.lyrics_area.delete("1.0", 'end')
        self.lyrics_area.insert('end', lyrics)
        self.lyrics_area.configure(state='disabled')

if __name__ == "__main__":
    app = LyricsApp()
    app.mainloop()
