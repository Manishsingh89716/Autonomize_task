import requests

'''fetch the github users details using github api'''
def fetch_github_user(username):
    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code != 200:
        raise Exception("GitHub user not found")
    data = response.json()
    return {
        "username": data["login"],
        "location": data.get("location"),
        "bio": data.get("bio"),
        "public_repos": data["public_repos"],
        "following": data["following"],
        "followers": data["followers"],
    }