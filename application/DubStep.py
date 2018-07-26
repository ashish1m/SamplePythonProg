import re


def song_decoder(song):
    song = re.sub("(WUB)+", " ", song)
    return song.strip()


print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))
