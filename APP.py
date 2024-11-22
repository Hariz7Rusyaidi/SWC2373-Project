from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI(access_token='YOUR_ACCESS_TOKEN')

meeting = api.meetings.create(
    title='My Conference',
    start='2024-11-22T10:00:00Z',
    end='2024-11-22T11:00:00Z',
    invitees=['email@example.com']
)
print(f'Meeting created with ID: {meeting.id}')