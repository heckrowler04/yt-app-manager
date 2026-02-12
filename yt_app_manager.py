import json

# Trying to load the data by reading the videos data
def load_video():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file) #Returns in list format[] if 'videos' is printed.
    except FileNotFoundError:
        return []
    
# Trying to save the videos data in the newly created file
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_yt_video(videos):
    print("\n")
    print("-" * 100)
    # Since the videos I'm trying to access from the load_video() method returns in the long string format, I'm trying to convert it into a list with key value pairs.
    # And since the user don't know that the video starts from 0, I'm asking it to start from 1. 
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['Name']}, Duration : {video['Time']}")#Here, I accessed the keys from the dictionary created from the add_yt_video() method.
        #This is done using ['key_name']
    print("-" * 100)

def add_yt_video(videos):
    name = input("Enter the video name: ")
    time = input("Enter video time: ")
    videos.append({"Name" : name, "Time" : time}) #"videos" is initially empty, so I'm appending the name and time into it.
    save_data_helper(videos) #Always save the updated data in this function.

def update_yt_video(videos):
    list_yt_video(videos)
    index = int(input("Enter the index of the video you want to update: ")) #Asking from the user the index where they'd like to update the value
    if 0<= index <= len(videos): #Conditions to check if the updation of the new data is possible.
        name = input("Enter the video name: ") #If yes, then ask the new data...
        time = input("Enter video time: ")
        videos[index-1] = {"Name" : name, "Time" : time} #Add the new data in the given index
        save_data_helper(videos) #Always save the data after updating it...
        print("Video updated successuflly!")
    else:
        print("Invalid index!")

def delete_yt_video(videos):
    list_yt_video(videos)
    index = int(input("Enter the index of the video you'd want to delete...:")) #Asking from the user the index where they'd like to delete the value
    if 0 < index < len(videos): #Checking the condition
        del videos[index-1] #If the condition is satisfied, then delete the value in the specified index using del keyword
        save_data_helper(videos) #Save the data after updating the value.
        print("Video deleted successfully!")
    else:
        print("Invalid index.")


def main():
    videos = load_video()
    while True:
        print("---Youtube manager app---")
        print("\n Please enter one of the choice give below ")
        print("1. List all the yt vids you've stored ")
        print("2. Add a yt video ")
        print("3. Update a yt video details ")
        print("4. Delete a yt video ")
        print("5. Exit the app ")
        choice = input("Enter the choice of yours: ")
        # print(videos)
        
        match choice:
            case '1' :
                list_yt_video(videos)
            case '2' :
                add_yt_video(videos)
            case '3' :
                update_yt_video(videos)
            case '4':
                delete_yt_video(videos)
            case '5':
                break
            case _:
                print("Enter valid choice!")
                
# Trying to check if the function called is main. If yes, then call the function.
if __name__ == "__main__":
    main()
            
