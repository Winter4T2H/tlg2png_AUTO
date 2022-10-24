# tlg2png_AUTO
import os
import subprocess
import tempfile

PROCESS_NOW   = "[Info   ] "
PROCESS_ERROR = "[ERROR  ] "
PROCESS_LINE  = "===================================="
print(PROCESS_NOW + "\"tlg2png_AUTO\" Made by Winter4T2H.")
TLGAUTO_PATH = os.path.dirname(os.path.realpath(__file__))
try:
	os.mkdir(TLGAUTO_PATH+"\\export\\")
except FileExistsError:
	pass
# print(TLGAUTO_PATH)
# print(PROCESS_NOW + "Init completed.") #BREAKPOINT_INIT

def main(): #main loop
	PROCESS_NOW = "[Main   ] "
	print(PROCESS_NOW + PROCESS_LINE)
	print(PROCESS_NOW + "Please select tool (1:pimg, 2:tlg): ",end="")
	inp = input(); inp = inp.replace(" ","")
	if (inp == '1'):
		pass
	else:
		print(PROCESS_ERROR + "Invalid input.")
	pass

## pimg tools
# TO-DO

# tlg tools

def TLG_transfer():
	PROCESS_NOW = "[t-TRA  ] "

	TEMPDIR_PATH = tempfile.mkdtemp(suffix=None, prefix=None, dir=TLGAUTO_PATH)
	tempfile.tempdir=TEMPDIR_PATH
	print(tempfile.gettempdir())
	fileDir = r".\\"
	fileExt = r".tlg"
	global fileEs 
	fileEs = [_ for _ in os.listdir(fileDir) if _.endswith(fileExt)]

	if not fileEs:
		print(PROCESS_ERROR + "Cannot find any .tlg file in directory. (Is tlg2png_AUTO.exe in the same directory of .tlg?)")
		exit()
	else:
		print(PROCESS_NOW + "Files found:")
		for get_files_in_array in fileEs:
			print(PROCESS_NOW + "    -" + get_files_in_array)

	for get_files_in_array in fileEs:
		name = get_files_in_array.split('.')
		filename = name[0].split('/')
		f = open(get_files_in_array, "rb")
		fp = tempfile.NamedTemporaryFile(suffix=".tlg",delete=False)
		for get_indep_file_lines in f.readlines():
			fp.write(get_indep_file_lines)
		f.close(); fp.close()
		print(PROCESS_NOW+"temp file for \""+get_files_in_array+"\" created, name= "+fp.name)
		print(PROCESS_NOW+ "Calling tlg2png.exe...")
		subprocess.run(["tlg2png.exe", fp.name, TLGAUTO_PATH+"\\export\\"+"tempexport.png"])
		os.replace("./export/tempexport.png", "./export/"+filename[0]+".png")
		os.remove(fp.name)
	print(PROCESS_NOW+"Removing temp dir...")
	os.rmdir(TEMPDIR_PATH)
	print(PROCESS_NOW+"All tasks completed. Goodbye.")

#while True():
#	main()

TLG_transfer()
