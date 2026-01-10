def avg(ratings):
    if not ratings:
        return 0
    return sum(ratings) / len(ratings)


def status(avg_rating):
    if avg_rating >= 4.5:
        return "Excellent"
    elif avg_rating >= 3.5:
        return "Good"
    elif avg_rating >= 2.5:
        return "Average"
    else:
        return "Poor"


if __name__ == "__main__":
    # OPTIONAL: only runs when executed directly, NOT during pytest
    ratings = [4, 5, 3, 4.5]
    average = avg(ratings)
    print("Average Rating:", average)
    print("Status:", status(average))
