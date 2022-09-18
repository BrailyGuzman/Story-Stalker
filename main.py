import os, stdiomask, platform, time
from random import randint
from colorama import Fore, init

try:
    import requests
    from colorama import Fore, init
except ModuleNotFoundError:
    os.system('pip install requests')
    import requests
    os.system('pip install colorama')
    from colorama import Fore, init

os.system("cls" if platform.system() == "Windows" else "clear")
init(autoreset=True)
r = requests.Session()

logo = f"""{Fore.LIGHTCYAN_EX}
 _____ _                  _____ _       _ _           
|   __| |_ ___ ___ _ _   |   __| |_ ___| | |_ ___ ___ 
|__   |  _| . |  _| | |  |__   |  _| .'| | '_| -_|  _|
|_____|_| |___|_| |_  |  |_____|_| |__,|_|_,_|___|_|  {Fore.RESET}
                  |___

"""
print(logo)

session = requests.Session()

username = input(f"[{Fore.LIGHTRED_EX}+{Fore.RESET}] Username: ")
password = stdiomask.getpass(prompt=f"[{Fore.LIGHTRED_EX}+{Fore.RESET}] Password: ", mask='*')

url = "https://www.instagram.com/accounts/login/ajax/"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "x-csrftoken": "flABydJVnZRJYaGedv2ItjmC9UI77bqW",
    "mid": "xgDrB4ZsEzKAr1Tqyb5QlmbS2oa6JqCt"
}

data = {
"enc_password": "#PWD_INSTAGRAM_BROWSER:0:1651709336:" + password,
"username": username,
"queryParams": "{}",
"optIntoOneTap": "false",
}

data = session.post(url, headers=headers, data=data)
print(data.text)

session_id = data.cookies.get("sessionid")
headers["cookie"] = f"sessionid={session_id}"

if "userId" in data.text:
    print(f"\n[{Fore.LIGHTRED_EX}+{Fore.RESET}] Successfully Logged In")
    time.sleep(3)
else:
    print(f"\n[{Fore.LIGHTRED_EX}ERROR{Fore.RESET}] Wrong Username/Password")
    time.sleep(3)
    exit()

os.system("cls" if platform.system() == "Windows" else "clear")
target_logo = f"""{Fore.LIGHTCYAN_EX}
 _____ _       _ _      _____                 _   
|   __| |_ ___| | |_   |_   _|___ ___ ___ ___| |_ 
|__   |  _| .'| | '_|    | | | .'|  _| . | -_|  _|
|_____|_| |__,|_|_,_|    |_| |__,|_| |_  |___|_|  
                                     |___|        {Fore.RESET}

"""
print(target_logo)

target = input(f"[{Fore.LIGHTRED_EX}+{Fore.RESET}] Target: ")
headers["user-agent"] = "Instagram 85.0.0.21.100 Android (28/9; 380dpi; 1080x2147; OnePlus; HWEVA; OnePlus6T; qcom; en_US; 146536611)"
target_info = session.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={target}", headers=headers)
target_stories = []
userId = target_info.json()["data"] ["user"] ["id"]

x = (f"https://i.instagram.com/api/v1/feed/user/{userId}/story/")

response = session.get(x, headers=headers,)
story_items = response.json()["reel"] ["items"]
    
for story in story_items:
    story_url = story["image_versions2"] ["candidates"] [0] ["url"]
    target_stories.append(story_url)

for collected_story in target_stories:
    response = session.get(collected_story)
    with open (f"{randint(0, 100)}.jpeg", "wb") as writer:
        writer.write(response.content)
