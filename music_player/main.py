import flet as ft

class Song(object):
    def __init__(self, song_name: str, artist_name:str, audio_path: str, img_path: str):
        super(Song, self).__init__()
        self.song_name = song_name
        self.artist_name = artist_name
        self.audio_path = audio_path
        self.img_path = img_path
        
        
    @property
    def name(self):
        return self.song_name    

    @property
    def artist(self):
        return self.artist_name 
    
    @property
    def path(self):
        return self.audio_path 
    
    @property
    def path_img(self):
        return self.img_path 

class AudioDirectory(object):
    playlist: list = [
        Song(
            song_name = "Deutschland",
            artist_name="Rammstein",
            audio_path="1.mp3",
            img_path="1.jpg"            
        )
    ]

class Playlist(ft.View):
    def __init__(self, page: ft.Page):
        super(Playlist, self).__init__(
            route="/playlist",
            horizontal_alignment="center",
        )
        
        self.page = page
        self.playlist: list[Song] = AudioDirectory.playlist
        
        self.controls = [
            ft.Row(
                [
                    ft.Text("PLAYLIST", size=21, weight="bold",)
                ],
                alignment="center"
            ),
            ft.Divider(height=10, color="transparent")
        ]
        
        self.generate_playlist_ui()
        
    def generate_playlist_ui(self):
        for song in self.playlist:
            self.controls.append(
                self.create_song_row(
                    song_name = song.song_name,
                    artist_name = song.artist_name,
                    song=song
                    )
                )
                
    def create_song_row(self, song_name, artist_name, song: Song):
        return ft.Container(
            content=ft.Row(
                [
                    ft.Text(f"Название: {song.name}"),
                    ft.Text(artist_name),
                ],
                alignment="spaceBetween"
            ),
            data=song,
            padding=10,
            on_click=self.toggle_song
        )
        
    def toggle_song(self, e):
        self.page.session.set("song", e.control.data)
        self.page.go("/song")

class CurrentSong(ft.View):
    def __init__(self, page: ft.Page):
        super(CurrentSong, self).__init__(
            route="/song",
            padding=20,
            horizontal_alignment="center",
            vertical_alignment="center",
        )
        
        self.page = page
        self.song = self.page.session.get("song")
        self.duration: int=0
        self.start: int=0
        self.end: int=0
        self.is_playing: bool = False
        self.txt_start = ft.Text(self.format_time(self.start))
        self.txt_end = ft.Text(f"--{self.format_time(self.start)}")
        self.slider = ft.Slider(
            min=0, 
            thumb_color="transparent",
            on_change_end=None
        )
        

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    
    def router(route):
        page.views.clear()
        if page.route == "/playlist":
            playlist = Playlist(page)
            page.views.append(playlist)
        
        if page.route == "/song":
            song = CurrentSong(page)
            page.views.append(song)   
        
            
        page.update()
        
        
    page.on_route_change = router
    page.go("/playlist")
    
ft.app(target=main, assets_dir='assets')