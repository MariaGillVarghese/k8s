import os
from functools import partial
import shutil
from PIL import Image


def create_folder(root_directory='./Dir'):
    folders = ('low_res', 'Medium_res', 'High_res')
    concat_root_path = partial(os.path.join, root_directory)
    make_directory = partial(os.makedirs, exist_ok=True)

    for path_items in map(concat_root_path, folders):
        make_directory(path_items)


def get_resolution(path='./Dir'):
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    image_resolutions = []
    
    for file in files:
        if file.endswith('.jpg'):
            img = Image.open(os.path.join(path, file))
            width, height = img.size
            print(f"File: {file}, Resolution: {width}x{height} pixels")
            image_resolutions.append((file, width, height))
    
    return image_resolutions

def mov_images(image, width, height, root='./Dir'):
    if width < 3000 & height< 4000:  
        destination = os.path.join(root, 'low_res', os.path.basename(image))
    elif width < 5000 & height< 6017:  
        destination = os.path.join(root, 'Medium_res', os.path.basename(image))
    else:
        destination = os.path.join(root, 'High_res', os.path.basename(image))
    
    shutil.move(image, destination)



            

create_folder()


directory = os.getenv('FILE_DIRECTORY')

#print(f"Directory: {directory}")
get_resolution(directory)
image_data = get_resolution(directory)
for image, width, height in image_data:
    mov_images(os.path.join(directory, image), width, height)

