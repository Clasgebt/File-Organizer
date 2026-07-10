import os
import shutil

# Flow: C:\Users\YourUsername\...\...
folder_path = input("Enter the folder path you want to organize: ")

categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar.gz"],
    "Code": [".py", ".js", ".html", ".css"]
}

if not os.path.exists(folder_path):
    print("That folder doesn't exist! Double check the path.")
else:
    print("Folder found! Let's organize it 😼")
    files = os.listdir(folder_path)
    for file in files:
        full_path = os.path.join(folder_path, file)

        if os.path.isdir(full_path):
            print(f"Skipping directory: {file}")
            continue

        name, ext = os.path.splitext(file)
        print(f"File: {file} | Name: {name} | Extension: {ext}")

        # Determine the category based on the file extension
        category_found = None
        for category, extensions in categories.items():
            if ext in extensions:
                category_found = category
                break

        if category_found is None:
            category_found = "Others"

        dest_folder = os.path.join(folder_path, category_found)
        os.makedirs(dest_folder, exist_ok=True)

        try:
            shutil.move(full_path, os.path.join(dest_folder, file))
            print(f"Moved {file} to {category_found}")
        except Exception as e:
            print(f"Error moving {file}: {e}")