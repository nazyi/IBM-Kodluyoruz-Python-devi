import math


def euclideanDistance(point1, point2):
    return round(math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2))


points = [(2, 3), (5, 8), (1, 1), (7, 4)]

# Mesafeleri saklayacağımız liste
distances = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):  
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)


print("Tüm mesafeler:", distances)

min_distance = min(distances)
print("Minimum mesafe:", int(min_distance))
