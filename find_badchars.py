#!/usr/bin/python3
from colorama import Fore, Back, Style
import re
import time

input_file = 'archivo.in'
#output_file = 'archivo.out'
badchars_all = 'badchars_all'
array_all_badchars = []
array_bof_badchars = []
found_badchars =[]


def show_array_content(this_array):
	for element in this_array:
		print(Fore.RED + 'Badchar to compare ➤➤ '+ Style.RESET_ALL + Fore.BLUE +element + Style.RESET_ALL)
		time.sleep(0.01)


def transform_badchar_toarray():
	with open(badchars_all, 'r') as f:
		lines = f.readlines()

		for line in lines:
			simple_bad_char = ''
			for index, line_char in enumerate(line):

				if (index  % 4 == 0):
					#print(' comenzar nuevo')
					# New char
					if simple_bad_char != '':
						# guardar 
						array_all_badchars.append(simple_bad_char)

					simple_bad_char = ''
					simple_bad_char += line_char
				else:
					#print(' continuar')
					# Same char
					simple_bad_char += line_char

		show_array_content(array_all_badchars)


def compare_and_generate():
	actual_index = 0
	for x_index, x_badchar in enumerate(array_all_badchars):
		bof_badchar = array_bof_badchars[actual_index]
		print(Fore.GREEN + 'BoF: '+Style.RESET_ALL +bof_badchar)
		print(Fore.MAGENTA + 'Array: '+Style.RESET_ALL +x_badchar )

		if bof_badchar.lower() != x_badchar[2:4].lower():
			print(Back.RED + 'Badchar Found ➤➤'+ Style.RESET_ALL + " " +Fore.WHITE +x_badchar + Style.RESET_ALL)
			time.sleep(2)
			found_badchars.append(x_badchar)
		else:
			actual_index += 1

	print(Back.BLUE + """
						 ✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘
						 ✘✘✘ Badchars Identificados ✘✘✘
						 ✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘
		""" + Style.RESET_ALL)
	time.sleep(2)
	show_array_content(found_badchars)


def main():
	transform_badchar_toarray()
	with open(input_file, 'r') as f:
		lines = f.readlines()

		for line in lines:
			new_line = re.sub(' +', ' ', line)
			words = new_line.split(' ')
			# pprint(words)
			badchars = words[1]

			# print(badchars)

			badchar_4 = badchars[0:2]
			badchar_3 = badchars[2:4]
			badchar_2 = badchars[4:6]
			badchar_1 = badchars[6:8]

			array_bof_badchars.append(badchar_1)
			array_bof_badchars.append(badchar_2)
			array_bof_badchars.append(badchar_3)
			array_bof_badchars.append(badchar_4)

	# show_array_content(array_bof_badchars)
	# pprint(array_bof_badchars)
	compare_and_generate()

def banner():
	print("""
        .--.       .--.
    _  `    \     /    `  _
     `\.===. \.^./ .===./`
            \/`"`\/
         ,  | BuG |  ,
        / `\|;-.-'|/` \
       /    |::\  |    \
    .-' ,-'`|:::; |`'-, '-.
        |   |::::\|   | 
        |   |::::;|   |
        |   \:::://   |
        |    `.://'   |
       .' by          `.
    _,'     SniferL4bs  `,_
       www.sniferl4bs.com

 	En busca de los badchars 2019 - BoF OSCP """)
	print(Fore.GREEN + "Fichero con el dump de Inmmunity: "+ Style.RESET_ALL + input_file)
	print(Fore.GREEN + "Fichero con los badchars: "+ Style.RESET_ALL +badchars_all)
	time.sleep(3)

if __name__ == '__main__':
	banner()
	main()
