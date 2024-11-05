# Liked song in dictionary
liked_song = {
    'Payphone': 'Maroon 5',
    'Miss You': 'Blink-182'
}

# Make function to write liked song from dict
def write_liked_songs_to_file(liked_songs, file_name):
    with open(file_name, 'w') as f:
        for song in liked_songs:
            f.writelines(song+ "\n")


# test code
write_liked_songs_to_file(liked_song, 'my_like_song')

# Trying to read
with open('my_like_song', 'r') as f:
    print(f.read())