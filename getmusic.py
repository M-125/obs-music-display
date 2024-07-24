#the power of copypasta here  ˇ
from winsdk.windows.media.control import GlobalSystemMediaTransportControlsSessionManager as MediaManager

async def get_media_info():
    sessions = await MediaManager.request_async()
    current_session = sessions.get_current_session()
    if current_session:
        info = await current_session.try_get_media_properties_async()
        return info.artist, info.title
    else:
        return "",""