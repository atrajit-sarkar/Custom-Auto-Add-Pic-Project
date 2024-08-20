import os
from PIL import Image
from exif import Image as ExifImage

# Variables for a Particular Location:
taget_lat=69.6969696969 # Add latitude here according to your location
target_long=69.69696969 # Add logitude here according to yor location
thresold=0.005          # Change thresold according to your need

# Variable for Arraging Photos:
target_image_folder="your path to the folder"  # Your main folder path goes here
location_based_folder_name="Your Location Based Folder name"  # Your Location Based folder name should go here

# Here is a example of your directiry:
# Make a folder named MyPhotoAlbum and inside that make a folder named Azad_hind_gym
# Inside the MyPhotoAlbum upload all your photos and your code should auto add photos of the Azad hind gym inside the folder Azad_hind_gym
# MyPhotoAlbum
#     |-  your all photos....(files)
#     |-  Azad_hind_gym(folder)

 
# Function To match the photo Location:
def match_cord(lat,long):
    if abs(target_long-long)<thresold and abs(taget_lat-lat)<thresold:
        return True

# List out all your images inside the target_image_folder 
list_of_images=os.listdir(target_image_folder)

# Main Code:
if __name__=="__main__":
    for image in list_of_images:
        if not os.path.isdir(fr"{target_image_folder}\{image}"):
            with open(fr'{target_image_folder}\{image}', 'rb') as img_file:
                img = ExifImage(img_file)
            list_of_meta_data=img.list_all()
            if not img.has_exif:
                print("No EXIF metadata found")
            else:
                try:
                    gps_lat=img.gps_latitude[0]+(img.gps_latitude[1]/60)+(img.gps_latitude[2]/3600)
                    gps_long=img.gps_longitude[0]+(img.gps_longitude[1]/60)+(img.gps_longitude[2]/3600)
                    
                    if match_cord(gps_lat,gps_long):
                        os.rename(fr"{target_image_folder}\{image}",fr"{target_image_folder}\{location_based_folder_name}\{image}")
                    

                except Exception as e:
                    print(e)
            
