import os
import shutil



dir_list = ['C:\\Users\\soma\\AppData\\Local\\Temp\\',
			'C:\\Users\\soma\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\',
			'C:\\Users\\soma\\AppData\\Local\\Opera Software\\Opera Stable\\Cache']
for path in dir_list:
	data = os.path.join(os.path.abspath(os.path.dirname(__file__)), path)
	try:
		print(shutil.rmtree(data, True))
	except:
		pass
os.system('shutdown /s')
