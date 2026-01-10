from product import avg, status


def test_average_rating():
    assert avg([4, 5, 3, 4]) == 4.0


def test_average_empty():
    assert avg([]) == 0


def test_status_excellent():
    assert status(4.7) == "Excellent"


def test_status_good():
    assert status(3.8) == "Good"


def test_status_average():
    assert status(2.9) == "Average"


def test_status_poor():
    assert status(2.0) == "Poor"
