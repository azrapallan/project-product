import sys
product = "Headphones"
ratings = [4, 5, 3, 4.5]
if len(sys.argv) >= 3:
    product = sys.argv[1]
    try:
        ratings = [float(r) for r in sys.argv[2:] if r.strip()]
    except ValueError:
        print("ERROR: Ratings must be numbers")
        sys.exit(1)

if not ratings:
    print("ERROR: No ratings provided")
    sys.exit(1)

avg = sum(ratings) / len(ratings)

if avg >= 4.5:
    status = "Excellent"
elif avg >= 3.5:
    status = "Good"
elif avg >= 2.5:
    status = "Average"
else:
    status = "Poor"

print("\nProduct:", product)
print("Ratings:", ratings)
print("Average Rating:", round(avg, 2))
print("Status:", status)
