# base_path = os.path.dirname(__file__)
#
# full_path = os.path.join(base_path, 'data', 'example.txt')

with open(r"data\example.txt", "r") as file:
    print(file.read())
