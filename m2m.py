import os
import platform
import time
from colorama import Fore, Style
from tqdm import tqdm

def convert_again():
    response = input(Fore.CYAN + "\n Do you want to convert another MP4 file? Enter 'y'' for Yes or 'n' for No: " + Style.RESET_ALL)
    if response.lower() == "y":
        convert_mp4_to_mp3()
    elif response.lower() == "n":
        print(Fore.YELLOW + "\n Exiting the code..." + Style.RESET_ALL)
    else:
        print(Fore.RED + "\n Invalid input! Please enter 'y' or 'n'." + Style.RESET_ALL)
        convert_again()

def convert_mp4_to_mp3():
    os.system("clear")

    print(Fore.CYAN + """
	.-..-.        .-.   .---.   .-..-.      .----.
	: `' :       .'.'   `--. :  : `' :      `--  ;
	: .. :.---. .'.'_     ,' ',' : .. :.---.  .' '
	: :; :: .; `:_ ` :  .'.'_'   : :; :: .; ` _`,`.
	:_;:_;: ._.'  :_:   :____;  :_;:_;: ._.'`.__.'
		: :                         : :
		:_;                         :_;

    """ + Style.RESET_ALL)

    # Prompt user to input the path of the input MP4 file
    mp4_file = input(Fore.CYAN + " Enter the path of the MP4 file: " + Style.RESET_ALL)

    # Check if the input file exists
    if not os.path.isfile(mp4_file):
        print(Fore.RED + "\n Input file does not exist!" + Style.RESET_ALL)
        convert_again()

    # Prompt user to input the name for the output MP3 file
    mp3_file = input("\n" + Fore.CYAN + " Enter name for the output file (without .mp3): " + Style.RESET_ALL)
    if not mp3_file:
        print(Fore.RED + "\n Invalid output file name!" + Style.RESET_ALL)
        convert_again()

    # Determine the output directory on Android
    output_dir = "/sdcard/Mp42Mp3"

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Construct the output MP3 file path
    output_file = os.path.join(output_dir, mp3_file + ".mp3")

    # Convert the MP4 file to MP3 using ffmpeg
    command = f"ffmpeg -i '{mp4_file}' '{output_file}'"

    print(Fore.YELLOW + "\n Converting the MP4 file to MP3...\n" + Style.RESET_ALL)

    # Add progress bar animation
    for _ in tqdm(range(10), desc="Converting", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}"):
        time.sleep(0.5)

    os.system(command)
    os.system("clear")

    print(Fore.GREEN + "\n  ✅ Conversion complete! The MP3 file is saved in the 'Mp42Mp3' folder." + Style.RESET_ALL)
    convert_again()

convert_mp4_to_mp3()
