from product_rating import calculate_average_rating, product_status

def test_average_rating():
    ratings = [4, 5, 3, 4]
    assert calculate_average_rating(ratings) == 4.0

def test_average_empty():
    ratings = []
    assert calculate_average_rating(ratings) == 0

def test_status_excellent():
    avg = 4.7
    assert product_status(avg) == "Excellent"

def test_status_good():
    avg = 3.8
    assert product_status(avg) == "Good"

def test_status_average():
    avg = 2.9
    assert product_status(avg) == "Average"

def test_status_poor():
    avg = 2.0
    assert product_status(avg) == "Poor"