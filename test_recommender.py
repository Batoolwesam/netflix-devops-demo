from recommender import recommend_movies

def test_kids_content():
    assert "Cartoon Adventures" in recommend_movies(10, "action")

def test_action_movies():
    result = recommend_movies(25, "action")
    assert "Fast Action Movie" in result
