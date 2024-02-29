def artist_profile(artistName, albumTitle, **artist_info):
    artist_info["Artist Name"] = artistName
    artist_info["Album Title"] = albumTitle
    return artist_info

artist1 = artist_profile('Weeknd', 'Dawn FM', song1 = 'Sacrifice', song2 = 'Take My Breath', song3 = 'Less Than Zero')
print (artist1)
artist2 = artist_profile('Radiohead', 'No Surprises', song1 = 'No Surprises', song2 = 'Karma Police')
print (artist2)
artist3 = artist_profile('Joji', 'Nectar', song1 = 'High Hopes')
print (artist3)