import datetime
import requests
from bs4 import BeautifulSoup

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
MY_API_KEY = "" # Your YouTube Data API key here
# https://developers.google.com/youtube/v3/getting-started

def get_youtube_video(music,artist):
    # YouTube Data API v3
    # https://developers.google.com/youtube/v3/docs/search/list
    YOUTUBE_SEARCH_API_URL = "https://www.googleapis.com/youtube/v3/search"
    q = f"{artist} songs|{music}"
    params = {
        "part": "id",
        "maxResults": 1,
        "miner": "false",
        "key": MY_API_KEY,
        "type": "video",
        "q": q
    }
    response = requests.get(YOUTUBE_SEARCH_API_URL, params=params)
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return None
    data = response.json()
    return f"https://www.youtube.com/watch?v={data["items"][0]["id"]["videoId"]}"


birth_day_year = 2021 # Your birth year here
# Example: 2021
birth_month = 6 # Your birth month here
# Example: 6
birth_day = 10  # Your birth day here
# Example: 10

date = datetime.date(birth_day_year, birth_month, birth_day)

my_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}

print(f"Billboard Hot 1 from {birth_day_year}-{birth_month}-{birth_day} to last birthday, on every birthdays.")
while date <= datetime.date.today():
    print(date.strftime("%Y-%m-%d"))

    # Get the URL for the Billboard Hot 100 chart for the given date
    url = f"{BILLBOARD_URL}{date.strftime('%Y-%m-%d')}/"

    response = requests.get(url, headers=my_header)
    if response.status_code != 200:
        print(f"Error: {response.status_code} for date {date}")
    else:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")
        # Find the top 1 songs on the chart
        top_song = soup.select_one("li h3")

        song_title = top_song.find_next("span", class_="c-label").get_text(strip=True)

        print(f"Song: {song_title}, Artist: {top_song.get_text(strip=True)}")

        # get youtube video if key exists
        if MY_API_KEY:
            # Get the YouTube video URL for the song
            video_url = get_youtube_video(song_title, top_song.get_text(strip=True))
            print(f"Video URL: {video_url}")

    # Increment the date by one week (1 year)
    birth_day_year += 1
    date = datetime.date(birth_day_year, birth_month, birth_day)



