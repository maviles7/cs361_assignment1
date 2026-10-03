# MICROSERVICE
# reads prng-service.text file
# generates the modulo of the random number

# import modules
import os
import time

# constants
IMAGES_DIR = "images"
IMAGE_FILE = "image-service.txt"

# imgsrv function
def get_image(): 
    # return sorted list of images in the images directory
    # validate that path exists - if not, then create the path
    if not os.path.exists(IMAGES_DIR):
        os.makedirs(IMAGES_DIR)

    # validate file extension
    valid_extensions = [".png"]
    # get array of images from images directory w/valid extensions
    images = [ 
        os.path.join(IMAGES_DIR, f)
        for f in os.listdir(IMAGES_DIR)
        if f.lower().endswith(valid_extensions)
    ]

    return sorted(images)

print("image microservice started - listening for requests")

while True:
    time.sleep(1)  # sleep for 1 second
    # if path exists, then read the file
    if os.path.exists(IMAGE_FILE):
        with open(IMAGE_FILE, "r") as f:
            file_content = f.read().strip()

        # if file content is a digit, then generate the modulo of the random number & write to file
        if file_content.isdigit():
            index = int(file_content)
            images = get_image()

            if not images:
                response = "ERROR: no images found in images directory"
            else: 
                    # modulo logic
                    modulo_indexed_image = images[index % len(images)]
                    response = os.path.abspath(modulo_indexed_image)

            # write the response to the file
            with open(IMAGE_FILE, "w") as f:
                f.write(response)
            print(f"image microservice response: {response}")
            