import sys
import instaloader
if "__main__" == __name__:
    if not len(sys.argv) == 3:
        sys.exit(
            "Invalid usage, please use: python script.py <username-to-login-with> <username-to-check>")
    L = instaloader.Instaloader()
    username_login = sys.argv[1]
    username_to_check = sys.argv[2]
    L.interactive_login(username_login)
    profile = instaloader.Profile.from_username(L.context, username_to_check)
    followers = set(profile.get_followers())
    following = set(profile.get_followees())
    print(following - followers)
