# pylint: disable=all
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from dotenv import load_dotenv

load_dotenv()


def list_playlists():
    # Set up the OAuth 2.0 flow for user authentication.
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        os.environ["GOOGLE_OAUTH_CLIENT_SECRET_FILE"],
        ["https://www.googleapis.com/auth/youtube.readonly"],
    )
    credentials = flow.run_local_server(port=8080)

    # Create the API client
    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)

    # Retrieve the user's playlists
    # pylint: disable=no-member
    request = youtube.playlists().list(
        part="snippet,contentDetails",
        mine=True,
        maxResults=50,  # You can adjust the number of results per page
    )
    response = request.execute()
    return response

    # Print the titles and IDs of the playlists
    # for playlist in response["items"]:
    #     print(f"Playlist Title: {playlist['snippet']['title']}")
    #     print(f"Playlist ID: {playlist['id']}\n")


if __name__ == "__main__":
    list_playlists()
