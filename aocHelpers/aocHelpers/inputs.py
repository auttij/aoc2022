import logging

def read_str(filepath):
	logging.info(f"reading file: {filepath}")
	with open(filepath) as fp:
		return "".join(fp.readlines())

def read_file_to_arr(filepath):
	logging.info(f"reading file: {filepath}")
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(line.strip())
	return arr

def read_file_to_int_arr(filepath):
	logging.info(f"reading file: {filepath}")
	arr = []
	with open(filepath) as fp:
		lines = fp.readlines()
		for line in lines:
			arr.append(int(line.strip()))
	return arr