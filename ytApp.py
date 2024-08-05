import json

def print_header(title):
    """Print a header with a decorative border."""
    border = '=' * len(title)
    print(f"\n{border}\n{title}\n{border}")

def print_message(message, status="INFO"):
    """Print a message with a decorative status label."""
    status_labels = {
        "INFO": "[INFO]",
        "SUCCESS": "[SUCCESS]",
        "ERROR": "[ERROR]"
    }
    label = status_labels.get(status, "[INFO]")
    print(f"{label} {message}")

def add_vid(videos):
    """Add a new video to the list and save the changes."""
    print_header("Add New Video")
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_vids(videos)
    print_message("Video added successfully.", "SUCCESS")

def del_vid(videos):
    """Delete a video from the list based on user input."""
    print_header("Delete Video")
    list_vid(videos)
    try:
        index = int(input("Enter the number of the video to delete: ")) - 1
        if 0 <= index < len(videos):
            del videos[index]
            save_vids(videos)
            print_message("Video deleted successfully.", "SUCCESS")
        else:
            print_message("Invalid index.", "ERROR")
    except ValueError:
        print_message("Invalid input. Please enter a number.", "ERROR")

def load_vid():
    """Load the list of videos from a file."""
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def list_vid(videos):
    """List all videos with their indices."""
    print_header("List of Videos")
    if not videos:
        print_message("No videos found.", "INFO")
        return
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name: {video['name']}, Time: {video['time']}")

def save_vids(videos):
    """Save the list of videos to a file."""
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def upd_vid(videos):
    """Update a video's details based on user input."""
    print_header("Update Video")
    list_vid(videos)
    try:
        index = int(input("Enter the number of the video to update: ")) - 1
        if 0 <= index < len(videos):
            new_name = input("Enter new video name: ")
            new_time = input("Enter new video time: ")
            videos[index] = {'name': new_name, 'time': new_time}
            save_vids(videos)
            print_message("Video updated successfully.", "SUCCESS")
        else:
            print_message("Invalid index.", "ERROR")
    except ValueError:
        print_message("Invalid input. Please enter a number.", "ERROR")

def main():
    """Main function to run the app loop."""
    videos = load_vid()
    while True:
        print_header("YouTube Manager App")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video details")
        print("4. Delete a YouTube video")
        print("5. Exit app")
        print("\n")
        choice = input("Enter your choice: ")
        
        match choice:
            case '1':
                list_vid(videos)
            case '2':
                add_vid(videos)
            case '3':
                upd_vid(videos)
            case '4':
                del_vid(videos)
            case '5':
                print_message("Exiting app.", "SUCCESS")
                break
            case _:
                print_message("Invalid choice! Please enter a number between 1 and 5.", "ERROR")

if __name__ == "__main__":
    main()
