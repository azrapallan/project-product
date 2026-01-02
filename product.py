import sys

ratings = []

if len(sys.argv) > 2:
    product = sys.argv[1]
    ratings = list(map(float, sys.argv[2:]))
else:
    product = "Headphones"
    ratings = [4, 5, 3, 4.5]

avg = sum(ratings) / len(ratings)

if avg >= 4.5:
    status = "Excellent"
if avg >= 3.5 and avg < 4.5:
    status = "Good"
if avg >= 2.5 and avg < 3.5:
    status = "Average"
if avg < 2.5:
    status = "Poor"

print("\nProduct:", product)
print("Ratings:", ratings)
print("Average Rating:", round(avg, 2))
print("Status:", status)  