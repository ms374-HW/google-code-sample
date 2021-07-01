"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
import random
from builtins import input


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._video_playing = False
        self._current_video = None
        self._playlists = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        print("Here's a list of all available videos:")
        # A list of the videos as objects
        videos = self._video_library.get_all_videos()
        # sorting lin lexographical order
        videos = sorted(videos)

        # printing for every video
        for video in videos:
            # we turn the list of tags into a string by joining the tags seperated with a space (' ')
            tags = " ".join([tag for tag in video.tags])

            # if the video is flagged, we need to display appropriate message
            if video.flagged:
                print(
                    "{} ({}) [{}] - FLAGGED (reason: {})".format(
                        video.title, video.video_id, tags, video.flagged_reason
                    )
                )
            else:
                print("{} ({}) [{}]".format(video.title, video.video_id, tags))

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        # getting the video from the ID
        video = self._video_library.get_video(video_id)

        # if the video for the video ID exists:
        if video:

            # if the video is flagged, we cannot play it
            if video.flagged:
                print(
                    "Cannot play video: Video is currently flagged (reason: {})".format(
                        video.flagged_reason
                    )
                )
                return

            # if there is a video playing, we stop the video
            if self._current_video:
                print("Stopping video: {}".format(self._current_video.title))

            # we play the new video
            print("Playing video: {}".format(video.title))

            # setting the current video and that there is a video playing
            self._current_video = video
            self._video_playing = True
        # if there is no video existing by that video ID
        else:
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""

        # if there is a video playing
        if self._current_video:
            print("Stopping video: {}".format(self._current_video.title))

            # setting the current video and that there is a video playing as None
            self._current_video = None
            self._video_playing = False
        # if there is no video playing
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""

        # getting the list of videos
        videos = self._video_library.get_all_videos()

        # filtering out the flagged videos in the library
        videos = [video for video in videos if video.flagged == False]

        # if there are no videos:
        if len(videos) < 1:
            print("No videos available")
            return

        # getting a random video from the list of videos
        random_index = random.randrange(len(videos))
        video = videos[random_index]

        # if the video exists:
        if video:

            # if there is a video playing, we stop the video
            if self._current_video:
                print("Stopping video: {}".format(self._current_video.title))

            # we play the new video
            print("Playing video: {}".format(video.title))

            # setting the current video and that there is a video playing
            self._current_video = video
            self._video_playing = True

    def pause_video(self):
        """Pauses the current video."""

        # if there is a video playing
        if self._video_playing:
            print("Pausing video: {}".format(self._current_video.title))
            self._video_playing = False
        # if there is a current video, but it is not playing, then it is already paused
        elif self._current_video:
            print("Video already paused: {}".format(self._current_video.title))
        # otherwise there is no video played:
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""

        # if the video is already playing
        if self._video_playing:
            print("Cannot continue video: Video is not paused")
        # video is paused
        elif self._current_video:
            print("Continuing video: {}".format(self._current_video.title))
            self._video_playing = False
        # else there is no video played
        else:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""

        # if the video is playing
        if self._current_video:
            tags = " ".join([tag for tag in self._current_video.tags])

            # if the current video is not playing, it is paused
            if not self._video_playing:
                # printing the values
                print(
                    "Currently playing: {} ({}) [{}] - PAUSED".format(
                        self._current_video.title, self._current_video.video_id, tags
                    )
                )
            else:
                # printing the values
                print(
                    "Currently playing: {} ({}) [{}]".format(
                        self._current_video.title, self._current_video.video_id, tags
                    )
                )
        # no current video is playing
        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        # normalising the playlist name to check for different cases:
        norm_name = playlist_name.lower()

        # for every playlist, check if the name already exits
        for playlist in self._playlists.keys():
            # if the name exists, we inform and return
            if playlist.lower() == norm_name:
                print(
                    "Cannot create playlist: A playlist with the same name already exists"
                )
                return

        # create a playlist by the name
        playlist = Playlist(playlist_name)

        # add plalist to list of playlists
        self._playlists[playlist_name] = playlist

        print("Successfully created new playlist: {}".format(playlist_name))

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """

        # normalising the playlist name to check for different cases:
        norm_name = playlist_name.lower()

        # first check if play list doesn't exist
        # for every playlist, check if the name already exits
        for playlist_names in self._playlists.keys():
            # if the name exists, we continue
            if playlist_names.lower() == norm_name:
                video = self._video_library.get_video(video_id)
                playlist = self._playlists[playlist_names]
                # if the video exists, we add to the list:
                if video:

                    # check if the video is flagged
                    if video.flagged:
                        print(
                            "Cannot add video to my_playlist: Video is currently flagged (reason: {})".format(
                                video.flagged_reason
                            )
                        )

                    # check if the video exists in the playlist
                    elif playlist.get_video(video_id):
                        print(
                            "Cannot add video to {}: Video already added".format(
                                playlist_name
                            )
                        )

                    # it doesn't exist in the playlist so we add the video
                    else:
                        playlist.add_video(video)
                        print(
                            "Added video to {}: {}".format(playlist_name, video.title)
                        )

                    # return
                    return
                # other wise we say it doesn't exist
                else:
                    print(
                        "Cannot add video to {}: Video does not exist".format(
                            playlist_name
                        )
                    )

                return

        # if it is out of the loop, it didn't find any playlist:
        print("Cannot add video to {}: Playlist does not exist".format(playlist_name))

    def show_all_playlists(self):
        """Display all playlists."""

        # print right message if there is no playlists in the collection
        if self._playlists == {}:
            print("No playlists exist yet")
            return

        # else we print the playlists:
        print("Showing all playlists:")

        # looping through the dictionary keys, which are the names of the playlists:
        # and then printing them
        # the lists are sorted in ascending order
        playlist_names = list(self._playlists)
        for playlist_name in sorted(playlist_names):
            print(playlist_name)

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        # normalising the playlist name to check for different cases:
        norm_name = playlist_name.lower()

        # first check if play list doesn't exist
        # for every playlist, check if the name already exits
        for playlist_names in self._playlists.keys():
            # if the name exists, we continue
            if playlist_names.lower() == norm_name:
                print("Showing playlist: {}".format(playlist_name))
                videos = self._playlists[playlist_names].get_all_videos()

                # if there are no videos yet
                if videos == []:
                    print("No videos here yet")
                # else we print the videos
                else:
                    for video in videos:
                        tags = " ".join([tag for tag in video.tags])

                        # if the video is flagged, we need to display appropriate message
                        if video.flagged:
                            print(
                                "{} ({}) [{}] - FLAGGED (reason: {})".format(
                                    video.title,
                                    video.video_id,
                                    tags,
                                    video.flagged_reason,
                                )
                            )
                        else:
                            print(
                                "{} ({}) [{}]".format(video.title, video.video_id, tags)
                            )

                return

        # if we didn't find the playlist:
        print("Cannot show playlist {}: Playlist does not exist".format(playlist_name))

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        # normalising the playlist name to check for different cases:
        norm_name = playlist_name.lower()

        # first check if play list doesn't exist
        # for every playlist, check if the name already exits
        for playlist_names in self._playlists.keys():
            # if the name exists, we continue
            if playlist_names.lower() == norm_name:
                video = self._video_library.get_video(video_id)
                playlist = self._playlists[playlist_names]
                # if the video exists, we add to the list:
                if video:
                    # check if the video exists in the playlist
                    if playlist.get_video(video_id):
                        playlist.remove_video(video)
                        print(
                            "Removed video from {}: {}".format(
                                playlist_name, video.title
                            )
                        )
                    # else we print error to remove
                    else:
                        print(
                            "Cannot remove video from {}: Video is not in playlist".format(
                                playlist_name
                            )
                        )

                # other wise we say it doesn't exist
                else:
                    print(
                        "Cannot remove video from {}: Video does not exist".format(
                            playlist_name
                        )
                    )

                return

        # if it is out of the loop, it didn't find any playlist:
        print(
            "Cannot remove video from {}: Playlist does not exist".format(playlist_name)
        )

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        # normalising the playlist name to check for different cases:
        norm_name = playlist_name.lower()

        # first check if play list doesn't exist
        # for every playlist, check if the name already exits
        for playlist_names in self._playlists.keys():
            # if the name exists, we continue
            if playlist_names.lower() == norm_name:
                playlist = self._playlists[playlist_names]
                # we clear the playlist
                playlist.clear_video()
                print("Successfully removed all videos from {}".format(playlist_name))
                return

        # if it is out of the loop, it didn't find any playlist:
        print("Cannot clear playlist {}: Playlist does not exist".format(playlist_name))

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        # normalising the playlist name to check for different cases:
        norm_name = playlist_name.lower()

        # first check if play list doesn't exist
        # for every playlist, check if the name already exits
        for playlist_names in self._playlists.keys():
            # if the name exists, we continue
            if playlist_names.lower() == norm_name:
                self._playlists.pop(playlist_names)
                print("Deleted playlist: {}".format(playlist_name))
                return

        print(
            "Cannot delete playlist {}: Playlist does not exist".format(playlist_name)
        )

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """

        # getting all videos
        videos = self._video_library.get_all_videos()

        # creating a list of videos that contain search term
        # and are not flagged
        suggested_videos = [
            video
            for video in videos
            if search_term.lower() in video.title.lower() and video.flagged == False
        ]

        # if no searches found:
        if suggested_videos == []:
            print("No search results for {}".format(search_term))
            return

        # other wise the search results in something, which we must display
        # count of videos displayed yet
        count = 1

        print("Here are the results for {}:".format(search_term))

        # sorting the videos
        suggested_videos = sorted(suggested_videos)

        # printing list of videos
        for video in suggested_videos:
            tags = " ".join([tag for tag in video.tags])
            print("{}) {} ({}) [{}]".format(count, video.title, video.video_id, tags))
            count += 1

        print(
            "Would you like to play any of the above? If yes, specify the number of the video.\nIf your answer is not a valid number, we will assume it's a no."
        )

        ip = input()

        if ip.isnumeric():
            # if the input is a valid number
            if int(ip) <= len(suggested_videos):
                selected_video = suggested_videos[int(ip) - 1]
                self.play_video(selected_video.video_id)

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """

        # getting all videos
        videos = self._video_library.get_all_videos()

        # creating a list of videos that contain search tag
        # and are not flagged
        suggested_videos = [
            video
            for video in videos
            if video_tag.lower() in [tag.lower() for tag in video.tags]
            and video.flagged == False
        ]

        # if no searches found:
        if suggested_videos == []:
            print("No search results for {}".format(video_tag))
            return

        # other wise the search results in something, which we must display
        # count of videos displayed yet
        count = 1

        print("Here are the results for {}:".format(video_tag))

        # sorting the videos
        suggested_videos = sorted(suggested_videos)

        # printing list of videos
        for video in suggested_videos:
            tags = " ".join([tag for tag in video.tags])
            print("{}) {} ({}) [{}]".format(count, video.title, video.video_id, tags))
            count += 1

        print(
            "Would you like to play any of the above? If yes, specify the number of the video.\nIf your answer is not a valid number, we will assume it's a no."
        )

        ip = input()

        if ip.isnumeric():
            # if the input is a valid number
            if int(ip) <= len(suggested_videos):
                selected_video = suggested_videos[int(ip) - 1]
                self.play_video(selected_video.video_id)

    def flag_video(self, video_id, flag_reason="Not supplied"):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        # getting the video from the ID
        video = self._video_library.get_video(video_id)

        # if the video for the video ID exists:
        if video:
            # if the video is flagged, we display error, else we flag it
            if video.flagged:
                print("Cannot flag video: Video is already flagged")

            else:
                # if the video is playing, it should be stopped
                if self._current_video == video:
                    self.stop_video()

                video.flag(flag_reason)
                print(
                    "Successfully flagged video: {} (reason: {})".format(
                        video.title, flag_reason
                    )
                )
        # if there is no video of that Video ID, we have to print the error
        else:
            print("Cannot flag video: Video does not exist")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        # getting the video from the ID
        video = self._video_library.get_video(video_id)

        # if the video for the video ID exists:
        if video:
            # if the video is flagged, we unflag it
            if video.flagged:
                video.allow()
                print("Successfully removed flag from video: {}".format(video.title))
            # else we display an error
            else:
                print("Cannot remove flag from video: Video is not flagged")

        # if there is no video of that Video ID, we have to print the error
        else:
            print("Cannot remove flag from video: Video does not exist")
