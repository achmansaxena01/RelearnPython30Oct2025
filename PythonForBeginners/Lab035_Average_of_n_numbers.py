
y = int(input("Enter the count number you want to find average of: "))
print("Enter the numbers you want to find average of: ")
nums1 = [float(input()) for _ in range(1, y+1)]
average = sum(nums1) / y

print(nums1)
print(type(nums1))
print(f"Average of {y} numbers {nums1} is : {average}")


print("\nAgain enter the numbers you want average of separated by space ")
nums2 = [float(x) for x in input().split()]
average = sum(nums2) / len(nums2)

print(f"Average of {len(nums2)} numbers {nums2} is : {average}")

