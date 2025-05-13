# udemy_python_MusicTimeMachine
Create a list of top 1 songs of your birthday, since the date you want.

This script is designed to retrieve the top song from the Billboard Hot 100 chart for a user's birthday each year, starting from a specified birth date up to the current date. It also optionally fetches a YouTube video link for the song using the YouTube Data API. Here's a detailed explanation:

1. Imports and Constants
The script imports the datetime module for handling dates, requests for making HTTP requests, and BeautifulSoup from the bs4 library for parsing HTML.
BILLBOARD_URL is the base URL for the Billboard Hot 100 chart.
MY_API_KEY is a placeholder for a YouTube Data API key, which is required to fetch YouTube video links.
2. YouTube Video Fetching Function
The get_youtube_video function uses the YouTube Data API to search for a video related to a song and its artist.
It constructs a query (q) combining the artist's name and song title, then sends a GET request to the YouTube API.
If the request is successful, it extracts the video ID from the API response and constructs a YouTube video URL. If the request fails, it prints an error message and returns None.
3. User's Birth Date
The script initializes the user's birth year, month, and day using the variables birth_day_year, birth_month, and birth_day.
A datetime.date object (date) is created to represent the user's birthday in the specified year.
4. Iterating Through Birthdays
The script iterates through each birthday from the user's birth year to the current year using a while loop.
For each birthday:
The date is printed in the format YYYY-MM-DD.
A URL is constructed to fetch the Billboard Hot 100 chart for that specific date.
A GET request is sent to the Billboard URL with a custom User-Agent header to mimic a browser request.
5. Parsing Billboard Data
If the HTTP request is successful, the HTML content of the page is parsed using BeautifulSoup.
The script attempts to find the top song on the chart using the CSS selector "li h3".
The song title is extracted from the HTML, and the artist's name is retrieved using the find_next method and the c-label class.
6. Fetching YouTube Video (Optional)
If a YouTube API key is provided (MY_API_KEY is not empty), the script calls the get_youtube_video function to fetch a YouTube video link for the song.
The video URL is printed if successfully retrieved.
7. Incrementing the Date
After processing the current birthday, the script increments the year (birth_day_year) by 1 and updates the date object to represent the next birthday.
Key Points:
Error Handling: The script checks the HTTP response status code for both the Billboard and YouTube API requests. If a request fails, it prints an error message.
Dynamic Date Handling: The script automatically stops iterating once the current date is reached.
YouTube API Dependency: The YouTube video fetching functionality requires a valid API key. If no key is provided, this feature is skipped.
HTML Parsing Assumptions: The script assumes a specific HTML structure for the Billboard website. If the structure changes, the CSS selectors ("li h3" and "span.c-label") may need to be updated.
