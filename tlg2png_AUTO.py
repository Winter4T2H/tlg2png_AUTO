# tlg2png_AUTO
import os
import subprocess

PROCESS_NOW   = "[Info   ] "
PROCESS_ERROR = "[ERROR  ] "
print(PROCESS_NOW + "\"tlg2png_AUTO\" Made by Winter4T2H.")
print(PROCESS_NOW + "====================================")

def get():
	PROCESS_NOW = "[p-GET  ] "
	fileDir = r".\\"
	fileExt = r".pimg"
	global fileEs 
	fileEs = [_ for _ in os.listdir(fileDir) if _.endswith(fileExt)]
	if not fileEs:
		print(PROCESS_ERROR + "Cannot find any .pimg file in directory. (Is tlg2png_AUTO.exe in the same directory of .pimg?)")
		exit()
	else:
		print(PROCESS_NOW + "Files found:")
		for get_files_array in fileEs:
			print(PROCESS_NOW + "    -" + get_files_array)
		print(PROCESS_NOW + "Do you wish to extract all above .pimg to png? (Y/n): ",end="")
		#inp = input(); inp = inp.replace(" ","")
		#if (inp == 'y' or inp == 'yes'):
		#	pass
		#else:
		#	print(PROCESS_NOW + "Exiting...")
		#	exit()
	return 0
def transfer():
	PROCESS_NOW = "[p-TRA  ] "
	for i in fileEs:
		subprocess.run(["ls", "-l", "/dev/null"], capture_output=True)
	return 0
def DEBUG_transfer():
	PROCESS_NOW = "[d-TRA  ] "
	print(PROCESS_NOW, end="")
	subprocess.run("tlg2png.exe")

#get()
#transfer()
DEBUG_transfer()