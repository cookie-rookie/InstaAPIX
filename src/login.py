import requests

def login(username, password):
    session = requests.Session()
    response = session.get('https://www.instagram.com/', headers=headers)
    csrf_token = response.cookies.get('csrftoken', '')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
        'X-CSRFToken': csrf_token,
        'X-Instagram-AJAX': '1',
        'X-Requested-With': 'XMLHttpRequest',
    }

  

    login_data = {
        'username': username,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}',
    }

    login_response = session.post('https://www.instagram.com/accounts/login/ajax/', data=login_data, headers=headers)

    if login_response.json().get('authenticated'):
        print('Login successful!')
        return session
    else:
        print('Login failed :', login_response.json().get('message'))
        return None