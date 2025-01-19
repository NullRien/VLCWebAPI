import requests
from requests.auth import HTTPBasicAuth
import xml.etree.ElementTree as ET

def set_volume(username="", password="", volume=0):
    try:
        volume = int(volume)
    except ValueError:
        return {'status': False, 'error': "Volume must be an INT"}

    if volume < 0 or volume > 512:
        return {'status': False, 'error': "Volume must be between 0-512"}

    url = f"http://127.0.0.1:8080/requests/status.xml?command=volume&val={volume}"

    try:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))

        if response.status_code == 200:
            return {'status': True, 'error': None}
        else:
            return {'status': False, 'error': response.status_code}
    except Exception as e:
        return {'status': False, 'error': str(e)}

def pause_music(username="", password=""):
    url = "http://127.0.0.1:8080/requests/status.xml?command=pl_pause"

    try:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))

        if response.status_code == 200:
            return {'status': True, 'error': None}
        else:
            return {'status': False, 'error': response.status_code}
    except Exception as e:
        return {'status': False, 'error': str(e)}

def pl_previous(username="", password=""):
    url = "http://127.0.0.1:8080/requests/status.xml?command=pl_previous"

    try:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))

        if response.status_code == 200:
            return {'status': True, 'error': None}
        else:
            return {'status': False, 'error': response.status_code}
    except Exception as e:
        return {'status': False, 'error': str(e)}

def pl_next(username="", password=""):
    url = "http://127.0.0.1:8080/requests/status.xml?command=pl_next"

    try:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))

        if response.status_code == 200:
            return {'status': True, 'error': None}
        else:
            return {'status': False, 'error': response.status_code}
    except Exception as e:
        return {'status': False, 'error': str(e)}

def get_info(username="", password=""):
    url = "http://127.0.0.1:8080/requests/status.xml"

    try:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))

        if response.status_code == 200:
            root = ET.fromstring(response.content)

            volume = root.findtext('volume')
            position = root.findtext('position')
            state = root.findtext('state')
            loop = root.findtext('loop')
            length = root.findtext('length')

            meta = root.find(".//category[@name='meta']")
            artist = meta.findtext("info[@name='artist']") if meta is not None else None
            title = meta.findtext("info[@name='title']") if meta is not None else None
            album = meta.findtext("info[@name='album']") if meta is not None else None
            artwork_url = meta.findtext("info[@name='artwork_url']") if meta is not None else None

            current_position_sec = 0
            current_position_min = 0
            length_min = 0
            length_sec = 0

            if position and length:
                current_position_sec = float(position) * float(length)
                current_position_min = int(current_position_sec // 60)
                current_position_sec = int(current_position_sec % 60)
                length_min = int(int(length) // 60)
                length_sec = int(int(length) % 60)

            return {
                'status': True,
                'error': None,
                'data': {
                    'volume': volume,
                    'current_position': f"{current_position_min}:{current_position_sec:02d}",
                    'max_position': f"{length_min}:{length_sec:02d}",
                    'state': state,
                    'loop': loop,
                    'length': length,
                    'artist': artist,
                    'title': title,
                    'album': album,
                    'artwork_url': artwork_url
                }
            }
        else:
            return {'status': False, 'error': response.status_code}
    except Exception as e:
        return {'status': False, 'error': str(e)}

if __name__ == "__main__":
    print(get_info(password="yourpassword"))
