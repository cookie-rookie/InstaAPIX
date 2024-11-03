import requests
from sessions import check_session  

class actions:
    def dm(session: requests.Session, user: str, msg: str):

        if not check_session(session):
            print("Session is inactive. Please log in again.")
            return False

        url = f"https://i.instagram.com/api/v1/direct_v2/web/create_thread/"


        payload = {
            "recipient_users": f"[['{user}']]",  
            "thread_ids": "[]",
            "text": msg
        }

    
        headers = {
            "User-Agent": "Instagram 123.0.0.26.121",
            "Content-Type": "application/x-www-form-urlencoded",
            "X-CSRFToken": session.cookies.get('csrftoken', ''),
        }

    
        response = session.post(url, headers=headers, data=payload)

        if response.status_code == 200:
            print("Message sent successfully!")
            return True
        else:
            print("Failed to send message:", response.json())
            return False

    # Example usage:
    # sessionA = join_session(proxy=True, username="user1", password="password1")
    # dm(sessionA, "target_user_id", "Hello from user1!")
