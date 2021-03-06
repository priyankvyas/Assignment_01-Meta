import csv

# A rectangle object to represent the rectangles in out problem.
class Rectangle:
    def __init__(self, id, width, height, xpos, ypos):
        self.id = id
        self.width = width
        self.height = height
        self.xpos = xpos
        self.ypos = ypos
# Quickly print off this rectangles current values.
    def print(self):
        print("ID: " + str(self.id) + "\nDimensions: (" + str(self.width) + ", " + str(self.height) + ")" + "\nCoordinates: (" + str(self.xpos) + ", " + str(self.ypos) + ")")

# Function fo
def get_rectangles(file_name):
    rectangles = []
    with open(file_name, 'r', encoding='utf-8-sig') as csv_file:
        reader = csv.reader(csv_file)
        line_count = 0
        for row in reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                rectangles.append(Rectangle(row[0], row[1], row[2], 0,0))
    return rectangles
