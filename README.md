This is a program that yoinks lyrics from Youtube music and shows it to you in the "always on top" floating window.

## Installation
1. install [python](https://www.python.org/downloads/)

2. install needed libs using pip:
3. ```
    pip install Flask
    pip install requests
    pip install tkinter
    ```
4. go to your browser extension page -> turn on developer mode -> import folder extension from this repository.

following steps can be exequted in any order, if something doesn't work refresh the page.

5. in seperate terminals run following in the \opaque_lyrics directory:
```
py window.py
```
and 
```
py lyric_server.py
```
6. When playing a track in youtube music open the lirycs tab. 

* *Note:*  You can use yt music with the song collapsed to the bottom, however inside it should be on the lyrics tab.