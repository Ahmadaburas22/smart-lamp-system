from datetime import datetime

def should_lamp_turn_on(motion, light_level):
    if motion not in ["yes", "y", "n","no"]:
        raise ValueError("Motion must be 'n' , 'y', 'yes' 'no'")

    if light_level < 0 or light_level > 100:
        raise ValueError("Light level must be between 0 and 100")

    if motion in ["yes", "y"] and light_level < 50:
        return True

    return False


def main():
    print("=== Smart Lamp Simulator V1 ===")

    # Get information from the sensors
    motion = input("Is motion detected? (yes/no): ").lower()
    try:
        light_level = int(input("Enter light level (0-100): "))
        print("\n--- Sensor Status ---")
        print(f"Motion: {motion}")
        print(f"Light Level: {light_level}")
        print("---------------------")


        if should_lamp_turn_on(motion, light_level):
            lamp_status = "ON"
            print("Lamp ON")
        else:
            lamp_status = "OFF"
            print("Lamp OFF")

    except ValueError as error:
        print(f"Error: {error}")
        return


    # Save the event to the log file
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("smart_lamp.log", "a") as log_file:
        log_file.write(
            f"{current_time} | Motion={motion} | "
            f"Light={light_level} | Lamp={lamp_status}\n"
        )


if __name__ == "__main__":
    main()
