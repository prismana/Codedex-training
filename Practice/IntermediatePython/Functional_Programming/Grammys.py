# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.8), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]

""" PROBLEM:
First, use the filter() function to pick out the songs that are longer than 5 minutes (i.e., 5.00).

Next, use map() to convert all the durations of the songs in your playlist from minutes to seconds.

Lastly, add up the total playtime of the playlist with reduce().

Since map(), filter(), and reduce() all use function parameters, it may be helpful to define separate named functions for them:

A longer_than_five_minutes() function for filter().
A minutes_to_seconds() function for map().
An add_durations() function for reduce().
"""

# Import reduce from functools
from functools import reduce

def longer_than_five_minutes(collection):
    return collection[1] > 5.00

def minute_to_second(song):
    duration = song[1]
    minute = int(duration)
    seconds = (duration - minute) * 100

    return minute * 60 + round(seconds)

def add_durations(total, song):
    duration = song[1]
    return total + duration

# print(playlist[0][1])

longerMusic = list(filter(longer_than_five_minutes, playlist))
durationInSecond = list(map(minute_to_second, playlist))
totalMinute = reduce(add_durations, playlist, 0)

print("Longest music in list: ", longerMusic)
print("Total Minute: ", totalMinute)
print("Duration each song in list: ", durationInSecond)

# for i in playlist:
#     print(i[1])

# print([i[1] for i in playlist])