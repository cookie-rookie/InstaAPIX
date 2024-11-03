class InfoManager:
    def fetch_user_info(session, username):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
        }

        user_info_response = session.get(f'https://www.instagram.com/{username}/?__a=1', headers=headers)

        if user_info_response.status_code == 200:
            return user_info_response.json()
        else:
            print('Failed to fetch user information')
            return None