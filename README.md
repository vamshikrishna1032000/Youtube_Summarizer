# YouTube Summarizer

This project is a web application that summarizes YouTube videos by identifying and playing the most important segments based on keyword extraction. The application is built with Django and uses KeyBERT for keyword extraction and the YouTube Transcript API to fetch video transcripts.

## Features

- Submit a YouTube link to summarize the video.
- Extracts important segments based on keyword relevance.
- Plays the identified segments within the web interface.


## Installation

1. **Clone the repository:**

    ```
    git clone https://github.com/yourusername/youtube-summarizer.git
    cd youtube-summarizer
    ```

2. **Create and activate a virtual environment:**

    ```
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up Django:**

    ```
    python manage.py migrate
    python manage.py runserver
    ```

## Usage

1. **Start the Django development server:**

    ```bash
    python manage.py runserver
    ```

2. **Submit a YouTube link:**

    - Enter a YouTube link into the input field and click "Summarize".
    - The application will fetch the transcript, extract keywords, and display buttons to play the most important segments of the video.


