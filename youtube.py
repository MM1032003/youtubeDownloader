import pyperclip, pytube, os


url = pyperclip.paste()


if not ('youtube.com' in url) and not ('youtu.be' in url):
    print("Please, Enter YouTube Link")
    exit()


print("Do You Wanna Download The Audio Or Video ? ")

if input().lower().startswith("a"):
    download_type   = 'audio'
else:
    download_type   = 'video'    


try:
    print("Where Do You Want To Save Your Downloaded Files (Empty To Download At Current Dir)...")
    save_to_path    = input()
    yt_obj          = pytube.YouTube(url)

    print("Available Formats : ")
    if download_type == 'audio':
        audio   = True
    else:
        audio   = False

    for stream in (yt_obj.streams.filter(only_audio=audio)):
        print("\t"+str(stream))

    print("\nEnter the itag number to download video of that format: ")
    itag    = input()
    
    stream  = yt_obj.streams.get_by_itag(itag)
    
    print(f"Downloading {yt_obj.title}... To {os.path.abspath(save_to_path)}")
    
    stream.download(save_to_path)
    input("Press Enter To Exit...")



except Exception as ex:
    print("Error : " + str(ex))
    input("Enter To Exit...")
