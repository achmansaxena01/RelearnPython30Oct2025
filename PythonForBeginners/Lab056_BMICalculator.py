# bmi = weight in kg /(height in meter * height in meter)
def calculate_bmi(height, weight):
    heigh_In_meters = height * 0.4536
    bmi = weight / (heigh_In_meters * heigh_In_meters)
    return bmi


print(calculate_bmi(5.8, 70))
print(calculate_bmi(5.2, 50))
print(calculate_bmi(5, 85))
