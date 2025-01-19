# VLC Media Player API Controller

This project provides a Python-based interface for controlling VLC Media Player via its HTTP API. It allows you to control playback, manage volume, navigate tracks, and retrieve detailed information about the current media.

## Features

- Adjust volume within a range of 0 to 512.
- Pause or resume playback.
- Navigate to the previous or next track in the playlist.
- Fetch detailed metadata of the current media, including:
  - Artist
  - Title
  - Album
  - Artwork URL
  - Playback position and duration.

## Prerequisites

- VLC Media Player with the HTTP interface enabled.
- Python 3.x.
- `requests` library.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/NullRien/VLCWebAPI.git
   ```

2. Navigate to the project directory:
   ```bash
   cd VLCWebAPI
   ```

3. Install the required dependencies:
   ```bash
   pip install requests
   ```

## Usage

1. Enable the VLC HTTP interface:
   - Enable VLC's web interface:
     - Open VLC -> Tools -> Preferences -> (set show settings to all) -> Interface -> Main Interfaces.
     - Check the box for "Web."
   - Set a password for the VLC web interface:
     - Navigate to `Main Interfaces -> Lua`.
     - Set a password in the "Lua HTTP" section.

2. Update the Python script with your VLC HTTP credentials.

3. Run the desired functions. For example:

   ```python
   from vlcapi import get_info

   info = get_info(password="yourpassword")
   print(info)
   ```

### Example Functions

- **Set Volume:**
  ```python
  set_volume(username="", password="yourpassword", volume=256)
  ```

- **Pause Music:**
  ```python
  pause_music(username="", password="yourpassword")
  ```

- **Previous Track:**
  ```python
  pl_previous(username="", password="yourpassword")
  ```

- **Next Track:**
  ```python
  pl_next(username="", password="yourpassword")
  ```

- **Get Media Info:**
  ```python
  get_info(username="", password="yourpassword")
  ```

## Response Format

All functions return a dictionary with the following structure:

```json
{
  "status": true,
  "error": null,
  "data": {
    "volume": "256",
    "current_position": "1:34",
    "max_position": "4:12",
    "state": "playing",
    "loop": "off",
    "length": "252",
    "artist": "Artist Name",
    "title": "Song Title",
    "album": "Album Name",
    "artwork_url": "file:///home/user/.cache/vlc/art/artistalbum/songname/art/art.jpg"
  }
}
```

## Note

If people actually use this api and want more features/ease of use id gladly add them if you open a issue!
