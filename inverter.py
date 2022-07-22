import numpy
from PIL import Image
import argparse

def open_image (image_name):
    image = Image.open(image_name)
    return numpy.array(image)
    
def invert_image (input_image, radius_part = 0.17):
    result_image = input_image.copy()

    center_x = int((input_image.shape[0]) / 2)
    center_y = int((input_image.shape[1]) / 2)

    invertion_rad = min(input_image.shape[0], input_image.shape[1]) * radius_part

    for x in range(input_image.shape[0]):
        for y in range(input_image.shape[1]):
            if x == center_x and y == center_y:
                continue # it maps to infinity
            old_center_distance = ((float(x - center_x) ** 2) + (float(y - center_y) ** 2)) ** 0.5
            new_center_distance = invertion_rad * invertion_rad / old_center_distance
            coefficent = new_center_distance / old_center_distance
            new_x = int(((x - center_x) * coefficent) + center_x)
            new_y = int(((y - center_y) * coefficent) + center_y) # this only moves the point farther or nearer to center on the same line
            if new_x >= 0 and new_x < input_image.shape[0] and new_y >= 0 and new_y < input_image.shape[1]:
                old_px = input_image[new_x, new_y]
                result_image[x, y] = old_px
            else:
                result_image[x, y] = [0, 200, 0]
            
    return result_image
    
def save_image (image, image_name):
    image_obj = Image.fromarray(image)
    image_obj.save(image_name)
    
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description = 'Inverts an image.')
    parser.add_argument('-f', '--file', nargs='?', required=True, help='Input image')
    parser.add_argument('-r', '--radius', nargs='?', default=0.17, type=float, help='This part of image size is invertion radius')
    parser.add_argument('-o', '--output', nargs='?', default='result.jpg', help='Output file name')

    cmd_args = vars(parser.parse_args())

    input_image = open_image(cmd_args['file'])
    output_image = invert_image(input_image, cmd_args['radius'])
    save_image(output_image, cmd_args['output'])
