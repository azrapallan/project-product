from product import avg, status


def test_average_rating():
    ratings = [4, 5, 3, 4]
    assert avg(ratings) == 4.0


def test_average_empty():
    ratings = []
    assert avg(ratings) == 0


def test_status_excellent():
    avg_rating = 4.7
    assert status(avg_rating) == "Excellent"


def test_status_good():
    avg_rating = 3.8
    assert status(avg_rating) == "Good"


def test_status_average():
    avg_rating = 2.9
    assert status(avg_rating) == "Average"


def test_status_poor():
    avg_rating = 2.0
    assert status(avg_rating) == "Poor"
