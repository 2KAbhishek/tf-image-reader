from PIL import Image
import os.path
import csv

def image_reader(csv_file = 'data/sample.csv', image_dir = 'data/' ):
    """
    Reads in a csv file and returns a list of image files and metadata.
    """
    f = open(csv_file, 'r')
    reader = csv.reader(f)
    _ = next(reader)
    image_data = []
    for row in reader:
        image_text, image_id, image_label = row[0], row[1], row[2]
        image = Image.open(os.path.join(image_dir, image_id + '.jpg'))
        image_data.append((image_text, image, image_label))
    f.close()
    return image_data

if __name__ == '__main__':
    print(image_reader())
