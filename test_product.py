from product import avg, status

def test_average_rating():
    ratings = [4, 5, 3, 4]
    assert avg(ratings) == 4.0

def test_average_empty():
    ratings = []
    assert avg(ratings) == 0

def test_status_excellent():
    avg = 4.7
    assert product_status(avg) == "Excellent"

def test_status_good():
    avg = 3.8
    assert status(avg) == "Good"

def test_status_average():
    avg = 2.9
    assert status(avg) == "Average"

def test_status_poor():
    avg = 2.0
    assert status(avg) == "Poor"
