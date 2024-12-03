import math

# Öklid mesafesi hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    """İki nokta arasındaki Öklid mesafesini hesaplar."""
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# 2D noktaları içeren bir liste oluşturma
points = [
    (1, 2), 
    (4, 6), 
    (7, 1), 
    (3, 5), 
    (2, 8)
]

# Nokta çiftleri arasındaki mesafeleri hesaplamak için liste
distances = []

# Mesafeleri hesaplama
for i in range(len(points)):
    for j in range(i + 1, len(points)):  # Aynı çiftlerin tekrar hesaplanmasını önler
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bulma
minimum_distance = min(distances)

# Sonuçları yazdırma
print(f"Noktalar: {points}")
print(f"Öklid Mesafeleri: {distances}")
print(f"Minimum Mesafe: {minimum_distance}")
