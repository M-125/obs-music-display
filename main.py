import obs
import getmusic as music
import time
import asyncio
#names of text objects to be used in obs
Artist="MArtist" 
Title="MTitle"
async def getmusic():
    artist, title=await music.get_media_info()
    obs.settext(Title,title)
    obs.settext(Artist,artist)
def main():
    while True:
        time.sleep(2)
        asyncio.run(getmusic())
        
main()