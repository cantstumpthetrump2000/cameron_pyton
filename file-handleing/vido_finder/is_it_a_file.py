

#https://stackoverflow.com/questions/14919609/is-this-file-a-video-python


fileInfo = MediaInfo.parse('some/file/name.ext')
for track in fileInfo.tracks:
    if track.track_type == "Video":
        # success!
