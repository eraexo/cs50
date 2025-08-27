# using requests and sys library for itunes api
import requests
import sys
import json

"""
if len(sys.argv) > 1:
    artist = sys.argv[1]
    response = requests.get(f"https://itunes.apple.com/search?term={artist}&limit=5")
    data = response.json()
    for result in data['results']:
        print(f"Track: {result['trackName']}, Artist: {result['artistName']}")

"""

if len(sys.argv) != 2:
    print("To few arguments. Please provide an artist name.")
    sys.exit()
else:
    response = requests.get(f"https://itunes.apple.com/search?term={sys.argv[1]}&limit=5")
    print(json.dumps(response.json(), indent=2))
    # list of tracks
    data = response.json()
    for result in data['results']:
        print(f"Track: {result['trackName']}, Artist: {result['artistName']}")
