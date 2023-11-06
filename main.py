all_users = {"aaa": "111", "bbb": "222", "ccc": "333"}
while True:
    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")
    # if username in all_users and all_users[username] == password: # si eilute is GPTchat
    for username, password in all_users.items():
        if entered_username == username and entered_password == password:
            print("welcome")
            break
    else:
        print("Wrong")
        continue
    break