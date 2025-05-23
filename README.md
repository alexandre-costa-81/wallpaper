# Reddit Wallpaper Downloader

This Python app downloads the latest hot wallpapers from Reddit's [r/wallpaper](https://www.reddit.com/r/wallpaper/) subreddit. It fetches direct image links and saves them locally in the `images` folder with sequential filenames.

## Features

- Downloads images from the top hot posts in r/wallpaper
- Checks if the URL is a direct image link
- Saves images with unique, sequential names
- Uses environment variables for Reddit API credentials

## Requirements

- Python 3.7+
- [PRAW](https://praw.readthedocs.io/)
- [requests](https://docs.python-requests.org/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/wallpaper.git
   cd wallpaper
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file** in the project root with your Reddit API credentials:
   ```
   REDDIT_CLIENT_ID=your_client_id
   REDDIT_CLIENT_SECRET=your_client_secret
   REDDIT_USER_AGENT=your_user_agent
   ```

4. **Create an `images` folder** in the project root:
   ```bash
   mkdir images
   ```

## Usage

Run the script:

```bash
python app.py
```

Downloaded images will be saved in the `images` folder.

## License

MIT License