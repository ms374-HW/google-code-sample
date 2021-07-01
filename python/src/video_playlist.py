"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self, playlist_name):
        """The VideoPlaylist class is initialized."""
        self._videos = {}
        self._name = playlist_name
    
    def get_all_videos(self):
        """Returns all available video information from the video playlist."""
        return list(self._videos.values())
    
    def get_name(self):
        """Returns playlist name"""
        return self._name
    
    def add_video(self, video):
        """Adds video to the playlist"""
        self._videos[video.video_id] = video

        return list(self._videos.values())
    
    def remove_video(self, video):
        """Removes video from the playlist"""
        self._videos.pop(video.video_id)

        return list(self._videos.values())
    
    def clear_video(self):
        """Clears all video in the playlist"""
        self._videos = {}

    def get_video(self, video_id):
        """Returns the video object (title, url, tags) from the playlist

        Args:
            video_id: The video url.

        Returns:
            The Video object for the requested video_id. None if the video
            does not exist.
        """
        return self._videos.get(video_id, None)
