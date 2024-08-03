import csv
import os
from library_item import LibraryItem

class VideoLibrary:
    
    def __init__(self, csv_file_path='C:/hoc/comp1752/Courswork/coursework/musiclist.csv'):
        self.csv_file_path = csv_file_path
        self.library = []
        self.load_library()

    def load_library(self):
        if os.path.exists(self.csv_file_path):
            with open(self.csv_file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip header
                for row in reader:
                    number = int(row[0])
                    name = row[1]
                    director = row[2]
                    rating = int(row[3])
                    play_count = int(row[4])
                    item = LibraryItem(number, name, director, rating, play_count)
                    self.library.append(item)
        else:
            print(f"File {self.csv_file_path} not found. Please ensure the file exists.")
            # Adding a dummy entry to prevent empty list errors
            self.library.append(LibraryItem(0, "No videos available", "N/A", 0, 0))

    def save_library_to_csv(self):
        with open(self.csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['number', 'name', 'director', 'rating', 'play_count'])
            for video in self.library:
                writer.writerow(video.to_csv_row())

    def append_video_to_csv(self, video):
        with open(self.csv_file_path, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(video.to_csv_row())

    def add_video(self, video):
        self.library.append(video)
        self.append_video_to_csv(video)

    def update_video(self, number, new_rating, new_play_count):
        video = self.get_video_by_number(number)
        if video:
            video.set_rating(new_rating)
            video.play_count = new_play_count
            self.save_library_to_csv()
            return True
        return False

    def delete_video(self, number):
        video = self.get_video_by_number(number)
        if video:
            self.library.remove(video)
            self.save_library_to_csv()
            return True
        return False

    def get_video_by_number(self, number):
        for video in self.library:
            if video.number == number:
                return video
        return None

    def get_video_titles(self):
        return [f"{video.number} {video.name} - {video.director} ,({video.rating}) ,( {video.play_count} ) " for video in self.library]
