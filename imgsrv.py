# MICROSERVICE
# reads prng-service.text file
# generates the modulo of the random number

# import modules
import os
import time

# constants
IMAGES_DIR = "images"
IMAGE_FILE = "image-service.txt"

NUM_IMAGES = 6

# imgsrv function
while True:
    time.sleep(1)

    # open image-service.txt and read
    if os.path.exists(IMAGE_FILE):
        with open(IMAGE_FILE, "r") as f:
            file_content = f.read().strip()

        # if file content is a number, generate image path
        if file_content.isdigit():
            random_number = int(file_content)
            # modulo logic 
            mod_num = random_number % NUM_IMAGES

            # image logic
            if mod_num == 0: 
                image_index = "black"
            elif mod_num == 1:
                image_index = "blue"
            elif mod_num == 2:
                image_index = "green"
            elif mod_num == 3:
                image_index = "orange"
            elif mod_num == 4:
                image_index = "red"
            elif mod_num == 5:
                image_index = "brown"

            # image path 
            image_path = os.path.join(IMAGES_DIR, f"{image_index}.png")
            print(f"Image microservice generated image path: {image_path}")

            # write image path to image-service.txt
            with open(IMAGE_FILE, "w") as f:
                f.write(image_path)

            print(f"random number: {random_number}")
            print(f"image path: {image_path}")