import tkinter as tk
from video_library import VideoLibrary
from library_item import LibraryItem
import csv
import webbrowser

class VideoPlayerApp:
    def __init__(self, root, library):
        self.root = root
        self.library = library
        self.playlist = []
        self.playlist_file_path = "C:/hoc/comp1752/Courswork/coursework/playlist.csv"
        self.create_main_window()

    def create_main_window(self):
        self.root.title("Video Player")
        self.root.geometry("900x600")
        self.root.resizable(False, False)

        tk.Label(self.root, text="Select an option by clicking one of the buttons below", fg='black', font=('Italic', 16), width=60).grid(row=0, column=0, columnspan=4, pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.grid(row=1, column=0, columnspan=4, pady=20)

        tk.Button(button_frame, text='Check Videos', width=20, height=2, font=('Italic', 12), command=self.show_video_check_window).grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text='Create Video List', width=20, height=2, font=('Italic', 12), command=self.show_create_video_window).grid(row=0, column=1, padx=10)
        tk.Button(button_frame, text='Update Videos', width=20, height=2, font=('Italic', 12), command=self.show_update_video_window).grid(row=0, column=2, padx=10)
        tk.Button(button_frame, text='Delete Videos', width=20, height=2, font=('Italic', 12), command=self.show_delete_video_window).grid(row=0, column=3, padx=10)
        tk.Button(button_frame, text='Import Playlist', width=20, height=2, font=('Italic', 12), command=self.show_import_playlist_window).grid(row=1, column=1, padx=10)
        tk.Button(button_frame, text='Export Playlist', width=20, height=2, font=('Italic', 12), command=self.show_export_playlist_window).grid(row=1, column=2, padx=10)

    def show_video_check_window(self):
        check_window = tk.Toplevel(self.root)
        check_window.title("Check Videos")
        check_window.geometry('1000x1000')

        video_player_frame = tk.Frame(check_window)
        video_player_frame.pack(pady=20)

        self.video_list = tk.Listbox(video_player_frame, width=50, height=10, font=("Arial", 12))
        self.video_list.pack(side=tk.LEFT, padx=10, pady=20)
        self.video_list.bind('<Double-1>', self.open_youtube)

        button_frame = tk.Frame(video_player_frame)
        button_frame.pack(side=tk.LEFT, padx=20)

        list_video_button = tk.Button(button_frame, text="List All Videos", font=("Arial", 12), command=self.list_all_videos)
        list_video_button.pack(pady=5)

        video_number_label = tk.Label(button_frame, text="Enter Video Number", font=("Arial", 12))
        video_number_label.pack(pady=5)
        self.video_number_entry = tk.Entry(button_frame, font=("Arial", 12), width=10)
        self.video_number_entry.pack(pady=5)

        check_video_button = tk.Button(button_frame, text="Check Video", font=("Arial", 12), command=self.check_video)
        check_video_button.pack(pady=5)

        self.blank_box = tk.Text(button_frame, height=5, width=30, font=("Arial", 12))
        self.blank_box.pack(pady=5)

        add_music_label = tk.Label(button_frame, text="Enter Video Number to Add to Playlist", font=("Arial", 12))
        add_music_label.pack(pady=5)
        self.add_music_entry = tk.Entry(button_frame, font=("Arial", 12), width=10)
        self.add_music_entry.pack(pady=5)

        add_music_button = tk.Button(button_frame, text="Add Music to Playlist", font=("Arial", 12), command=self.add_music_to_playlist)
        add_music_button.pack(pady=5)

        self.status_label = tk.Label(check_window, text="", font=("Arial", 12))
        self.status_label.pack(pady=10)

        self.playlist_text = tk.Text(check_window, height=10, width=60, font=("Arial", 12))
        self.playlist_text.pack(pady=10)

        back_button = tk.Button(check_window, text="Back", font=("Arial", 12), command=lambda: self.go_back(check_window))
        back_button.pack(pady=10)

    def show_create_video_window(self):
        create_window = tk.Toplevel(self.root)
        create_window.title("Create Video List")
        create_window.geometry('700x500')

        create_video_frame = tk.Frame(create_window)
        create_video_frame.pack(pady=20)

        create_video_number_label = tk.Label(create_video_frame, text="Video Number", font=("Arial", 12))
        create_video_number_label.pack(pady=5)
        self.create_video_number_entry = tk.Entry(create_video_frame, font=("Arial", 12))
        self.create_video_number_entry.pack(pady=5)

        create_video_name_label = tk.Label(create_video_frame, text="Video Name", font=("Arial", 12))
        create_video_name_label.pack(pady=5)
        self.create_video_name_entry = tk.Entry(create_video_frame, font=("Arial", 12))
        self.create_video_name_entry.pack(pady=5)

        create_video_director_label = tk.Label(create_video_frame, text="Director", font=("Arial", 12))
        create_video_director_label.pack(pady=5)
        self.create_video_director_entry = tk.Entry(create_video_frame, font=("Arial", 12))
        self.create_video_director_entry.pack(pady=5)

        create_video_rating_label = tk.Label(create_video_frame, text="Rating", font=("Arial", 12))
        create_video_rating_label.pack(pady=5)
        self.create_video_rating_entry = tk.Entry(create_video_frame, font=("Arial", 12))
        self.create_video_rating_entry.pack(pady=5)

        create_video_play_count_label = tk.Label(create_video_frame, text="Play Count", font=("Arial", 12))
        create_video_play_count_label.pack(pady=5)
        self.create_video_play_count_entry = tk.Entry(create_video_frame, font=("Arial", 12))
        self.create_video_play_count_entry.pack(pady=5)

        create_video_button = tk.Button(create_video_frame, text="Create Video", font=("Arial", 12), command=self.create_video)
        create_video_button.pack(pady=10)

        self.status_label = tk.Label(create_window, text="", font=("Arial", 12))
        self.status_label.pack(pady=10)

        back_button = tk.Button(create_window, text="Back", font=("Arial", 12), command=lambda: self.go_back(create_window))
        back_button.pack(pady=10)

    def show_update_video_window(self):
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Videos")
        update_window.geometry('700x500')

        update_video_frame = tk.Frame(update_window)
        update_video_frame.pack(pady=20)

        update_video_number_label = tk.Label(update_video_frame, text="Video Number", font=("Arial", 12))
        update_video_number_label.pack(pady=5)
        self.update_video_number_entry = tk.Entry(update_video_frame, font=("Arial", 12))
        self.update_video_number_entry.pack(pady=5)

        update_video_rating_label = tk.Label(update_video_frame, text="New Rating", font=("Arial", 12))
        update_video_rating_label.pack(pady=5)
        self.update_video_rating_entry = tk.Entry(update_video_frame, font=("Arial", 12))
        self.update_video_rating_entry.pack(pady=5)

        update_video_play_count_label = tk.Label(update_video_frame, text="New Play Count", font=("Arial", 12))
        update_video_play_count_label.pack(pady=5)
        self.update_video_play_count_entry = tk.Entry(update_video_frame, font=("Arial", 12))
        self.update_video_play_count_entry.pack(pady=5)

        update_video_button = tk.Button(update_video_frame, text="Update Video", font=("Arial", 12), command=self.update_video)
        update_video_button.pack(pady=10)

        self.status_label = tk.Label(update_window, text="", font=("Arial", 12))
        self.status_label.pack(pady=10)

        back_button = tk.Button(update_window, text="Back", font=("Arial", 12), command=lambda: self.go_back(update_window))
        back_button.pack(pady=10)

    def show_delete_video_window(self):
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Videos")
        delete_window.geometry('700x500')

        delete_video_frame = tk.Frame(delete_window)
        delete_video_frame.pack(pady=20)

        delete_video_number_label = tk.Label(delete_video_frame, text="Video Number", font=("Arial", 12))
        delete_video_number_label.pack(pady=5)
        self.delete_video_number_entry = tk.Entry(delete_video_frame, font=("Arial", 12))
        self.delete_video_number_entry.pack(pady=5)

        delete_video_button = tk.Button(delete_video_frame, text="Delete Video", font=("Arial", 12), command=self.delete_video)
        delete_video_button.pack(pady=10)

        self.status_label = tk.Label(delete_window, text="", font=("Arial", 12))
        self.status_label.pack(pady=10)

        back_button = tk.Button(delete_window, text="Back", font=("Arial", 12), command=lambda: self.go_back(delete_window))
        back_button.pack(pady=10)

    def show_import_playlist_window(self):
        import_window = tk.Toplevel(self.root)
        import_window.title("Import Playlist")
        import_window.geometry('500x300')

        import_playlist_button = tk.Button(import_window, text="Import Playlist", font=("Arial", 12), command=self.import_playlist)
        import_playlist_button.pack(pady=50)

        self.status_label = tk.Label(import_window, text="", font=("Arial", 12))
        self.status_label.pack(pady=20)

        back_button = tk.Button(import_window, text="Back", font=("Arial", 12), command=lambda: self.go_back(import_window))
        back_button.pack(pady=10)

    def show_export_playlist_window(self):
        export_window = tk.Toplevel(self.root)
        export_window.title("Export Playlist")
        export_window.geometry('500x300')

        export_playlist_button = tk.Button(export_window, text="Export Playlist", font=("Arial", 12), command=self.export_playlist)
        export_playlist_button.pack(pady=50)

        self.status_label = tk.Label(export_window, text="", font=("Arial", 12))
        self.status_label.pack(pady=20)

        back_button = tk.Button(export_window, text="Back", font=("Arial", 12), command=lambda: self.go_back(export_window))
        back_button.pack(pady=10)

    def list_all_videos(self):
        self.video_list.delete(0, tk.END)
        for title in self.library.get_video_titles():
            self.video_list.insert(tk.END, title)

    def check_video(self):
        video_number = self.video_number_entry.get()
        video = self.library.get_video_by_number(int(video_number))
        if video:
            self.blank_box.delete('1.0', tk.END)
            self.blank_box.insert(tk.END, f"Name: {video.name}\nDirector: {video.director}\nRating: {video.rating}\nPlay Count: {video.play_count}")
        else:
            self.blank_box.delete('1.0', tk.END)
            self.blank_box.insert(tk.END, "Video not found")

    def add_music_to_playlist(self):
        video_number = self.add_music_entry.get()
        video = self.library.get_video_by_number(int(video_number))
        if video:
            self.playlist.append(video)
            self.save_playlist()
            self.status_label.config(text=f"Added {video.name} to playlist")
            self.update_playlist_display()
        else:
            self.status_label.config(text="Video not found")

    def save_playlist(self):
        with open(self.playlist_file_path, 'w', newline='') as csvfile:
            fieldnames = ['number', 'name', 'director', 'rating', 'play_count']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for video in self.playlist:
                writer.writerow({
                    'number': video.number,
                    'name': video.name,
                    'director': video.director,
                    'rating': video.rating,
                    'play_count': video.play_count
                })

    def import_playlist(self):
        self.playlist = []
        try:
            with open(self.playlist_file_path, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    video = LibraryItem(
                        int(row['number']),
                        row['name'],
                        row['director'],
                        int(row['rating']),
                        int(row['play_count'])
                    )
                    self.playlist.append(video)
            self.status_label.config(text="Playlist imported successfully")
        except FileNotFoundError:
            self.status_label.config(text="Playlist file not found")

    def export_playlist(self):
        self.save_playlist()
        self.status_label.config(text="Playlist exported successfully")

    def update_playlist_display(self):
        self.playlist_text.delete('1.0', tk.END)
        for video in self.playlist:
            self.playlist_text.insert(tk.END, f"Number: {video.number}, Name: {video.name}, Director: {video.director}, Rating: {video.rating}, Play Count: {video.play_count}\n")

    def go_back(self, window):
        window.destroy()

    def create_video(self):
        number = int(self.create_video_number_entry.get())
        name = self.create_video_name_entry.get()
        director = self.create_video_director_entry.get()
        rating = int(self.create_video_rating_entry.get())
        play_count = int(self.create_video_play_count_entry.get())

        video = LibraryItem(number, name, director, rating, play_count)
        self.library.add_video(video)
        self.status_label.config(text="Video created successfully")

    def update_video(self):
        number = int(self.update_video_number_entry.get())
        new_rating = int(self.update_video_rating_entry.get())
        new_play_count = int(self.update_video_play_count_entry.get())

        video = self.library.get_video_by_number(number)
        if video:
            video.set_rating(new_rating)
            video.play_count = new_play_count
            self.status_label.config(text="Video updated successfully")
        else:
            self.status_label.config(text="Video not found")

    def delete_video(self):
        number = int(self.delete_video_number_entry.get())
        success = self.library.delete_video(number)
        if success:
            self.status_label.config(text="Video deleted successfully")
        else:
            self.status_label.config(text="Video not found")

    def open_youtube(self, event):
        selected_video = self.video_list.get(self.video_list.curselection())
        search_query = f"https://www.youtube.com/results?search_query={selected_video.replace(' ', '+')}"
        webbrowser.open(search_query)

if __name__ == "__main__":
    root = tk.Tk()
    csv_file_path = "C:/hoc/comp1752/Courswork/coursework/musiclist.csv"
    video_library = VideoLibrary(csv_file_path)
    app = VideoPlayerApp(root, video_library)
    root.mainloop()
