import time
import pygame

def beep(time):
    pygame.mixer.init()
    beep_sound = pygame.mixer.Sound("square.mp3")
    beep_sound.play()
    pygame.time.wait(time)
    beep_sound.stop()

beep(3000) #test sound

max = 100
min = 60

def check_hr_file():
    file_path = "www\hr.txt"

    try:
        while True:
            with open(file_path, 'r') as file:
                number_str = file.readline().strip()
                if number_str.isdigit():
                    number = int(number_str)
                    if min <= number <= max:
                        print(f"Heart rate in range {max}-{min}. Current value: {number}")
                    elif number > max:
                        print(f"Danger: Above {max}! Current value: {number}")
                        beep(1000)
                    else:
                        print(f"Danger: Below {min}! Current value: {number}")
                        beep(1000)
                else:
                    print("The file 'hr.txt' does not contain a valid number.")
            time.sleep(2)  # maybe match the hr update interval?
    except FileNotFoundError:
        print("hr.txt doesnt exist")
    except KeyboardInterrupt:
        print("Stopping the monitoring.")
        beep(5000)

if __name__ == "__main__":
    check_hr_file()
