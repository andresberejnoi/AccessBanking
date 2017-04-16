import yaml

def load_config(file):
	with open(file, 'r') as ymlfile:
		cfg = yaml.load(ymlfile)
	return cfg


if __name__ == "__main__":
	print (load_config())
