import os

# Directory containing the videos
directory = r'C:\Users'

# Iterate over files in the directory
for count, filename in enumerate(os.listdir(directory)):
    # Check if the file is a .mp4 file
    if filename.endswith('.mp4'):
        # Generate the new filename
        new_filename = f"AWS Interview Questions {count + 1}.mp4"
        # Construct the full path for both old and new filenames
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)
        # Rename the file
        os.rename(old_path, new_path)
