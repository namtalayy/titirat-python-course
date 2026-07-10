print("1. Circle calculator:")
print("   - Ask for radius")
print("   - Calculate area (π * r²)")
print("   - Calculate circumference (2 * π * r)")
print("   - Use 3.14159 for π")

#input
r = float(input("radius: "))

#process
a = 3.14159 * r ** 2
circumference = 2 * 3.14159 * r

#output
print(f"Area: {a:.2f}")
print(f"Circumference: {circumference:.2f}")
