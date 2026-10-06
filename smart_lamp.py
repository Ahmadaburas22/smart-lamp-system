print("=== Smart Lamp Simulator V1 ===")

# Get information from the sensors
motion = input("Is motion detected? (yes/no): ").lower()
light_level = int(input("Enter light level (0-100): "))

print("\n--- Sensor Status ---")
print(f"Motion: {motion}")
print(f"Light Level: {light_level}")
print("---------------------")


# Decide if the lamp should turn on
if motion == "yes" and light_level < 50:
    print("💡 Lamp ON")

elif motion == "yes" and light_level >= 50:
    print("☀️ Motion detected, but there is enough light.")
    print("Lamp OFF")

else:
    print("No motion detected.")
    print("Lamp OFF")