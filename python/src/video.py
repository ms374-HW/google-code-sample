"""A video class."""

from typing import Sequence


class Video:
    """A class used to represent a Video."""

    def __init__(self, video_title: str, video_id: str, video_tags: Sequence[str]):
        """Video constructor."""
        self._title = video_title
        self._video_id = video_id
        self._flagged = False
        self._flagged_reason = ""

        # Turn the tags into a tuple here so it's unmodifiable,
        # in case the caller changes the 'video_tags' they passed to us
        self._tags = tuple(video_tags)

    @property
    def title(self) -> str:
        """Returns the title of a video."""
        return self._title

    @property
    def video_id(self) -> str:
        """Returns the video id of a video."""
        return self._video_id

    @property
    def tags(self) -> Sequence[str]:
        """Returns the list of tags of a video."""
        return self._tags

    @property
    def flagged(self) -> Sequence[str]:
        """Returns whether a video is flagged."""
        return self._flagged

    @property
    def flagged_reason(self) -> Sequence[str]:
        """Returns the reason for a video to be flagged"""
        return self._flagged_reason

    def __eq__(self, other):
        if other:
            return self.title == other.title and self.video_id == other.video_id
        return False

    def __lt__(self, other):
        return self.title < other.title

    def flag(self, reason=""):
        self._flagged = True
        self._flagged_reason = reason

    def allow(self):
        self._flagged = False
        self._flagged_reason = ""
