print("What level of brightness is required? (even number)")
#ask for an even number for brightness
brightness = int(input())
print("\nAdjusting Brightness...\n")
for count in range(2, brightness + 1, 2):
    print(f"Beep's brightness level: {count * '*'}")
    print(f"Bop's brightness level: {count * '*'}")
    print()
print("Adjustments complete")