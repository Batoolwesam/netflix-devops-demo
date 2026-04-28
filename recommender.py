def recommend_movies(user_age, genre_preference):
    if user_age < 13:
        return ["Cartoon Adventures", "Kids Fun Show"]

    if genre_preference == "action":
        return ["Fast Action Movie", "Hero Returns"]

    elif genre_preference == "comedy":
        return ["Funny Moments", "Laugh Out Loud"]

    elif genre_preference == "drama":
        return ["Deep Story", "Life Journey"]

    else:
        return ["Popular Movie"]
