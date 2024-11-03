class Utils:
    def get_csrf_token(response):
        return response.cookies.get('csrftoken', None)

    def set_default_headers():
        return {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
        }