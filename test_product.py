def avg(ratings):
    """
    Calculate average rating.
    Returns 0 for empty list.
    """
    if not ratings:
        return 0
    return sum(ratings) / len(ratings)


def status(avg_rating):
    """
    Return product status based on average rating.
    """
    if avg_rating >= 4.5:
        return "Excellent"
    elif avg_rating >= 3.5:
        return "Good"
    elif avg_rating >= 2.5:
        return "Average"
    else:
        return "Poor"

