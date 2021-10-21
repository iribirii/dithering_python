'''
Dither style for any picture

Author: Inigo Iribarren
Date: 30-03-2020

Usage:
    dither_python.py [-c COLOR] [-b BAYER SIZE] [-s SCALE] [-r RESIZE_X RESIZE_Y] filename.ex

'''

from PIL import Image
import numpy as np
import argparse

def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='dither_python',
        description='Creates a copy of a selected image using bayer dithering style'
    )
    parser.add_argument(
        'file',
        type=str,
        help='Picture that will be transformed.'
    )
    parser.add_argument(
        '-c',
        '--color',
        action='store_true', help='Makes the dithering in color instead of B&W'
    )
    parser.add_argument(
        '-r',
        '--resize',
        default=(),
        nargs='+',
        type=int,
        help='New size of the ouput image.'
    )
    parser.add_argument(
        '-s',
        '--scale',
        default=1.0,
        type=float,
        help='Scale factor for the ouput image.'
    )
    parser.add_argument(
        '-b',
        '--bayer',
        default=2,
        type=int,
        help='Dimmensino of the bayer matrix.'
    )
    

    return parser.parse_args()

def get_bayer(dimmension):
    '''Returns a bayer matrix

    Returns a bayer matrix of N dimmension that will be used as a template for
    the dithering transformation.
    '''

    # Dimmension 1 has to be fixed cause that is 'dirty'
    if dimmension == 1:
        bayer = [
            [127, 127],
            [127, 127]
        ]
    elif dimmension == 2:
        bayer = [
            [ 51, 153],
            [204, 102]
        ]
    elif dimmension == 3:
        bayer = [
            [ 25, 150,  75],
            [200, 125, 225],
            [100, 175,  50]
        ]
    elif dimmension == 4:
        bayer = [
            [ 15, 135,  45, 165],
            [195,  75, 225, 105],
            [ 60, 180,  30, 150],
            [240, 120, 210,  90]
        ]
    else:
        print('ERROR: not a valid bayer dimmension')
        exit()

    return bayer

def dither_bw(data, bayer):
    '''Substitues in black and white, pixel by pixels, all the image using the bayer matrix
    '''
    o_data = np.zeros(data.shape)

    for x in range(0, data.shape[0]):
        for y in range(0, data.shape[1]):
            if data[x,y] > bayer[x%len(bayer)][y%len(bayer)]:
                o_data[x,y] = 255
            else:
                o_data[x,y] = 0

    return o_data

def dither_color(data, bayer):
    '''Substitues in color, pixel by pixels, all the image using the bayer matrix
    '''
    o_data = np.zeros(data.shape)

    for x in range(0, data.shape[0]):
        for y in range(0, data.shape[1]):
            for color in range(0, data.shape[2]):
                if data[x,y,color] > bayer[x%len(bayer)][y%len(bayer)]:
                    o_data[x,y,color] = 255
                else:
                    o_data[x,y,color] = 0

    return o_data

def main():

    # Parse arguments
    args = cli()

    # Get the bayer matrix
    b_matrix = get_bayer(args.bayer)

    # Read image 
    if not args.color:
        img = Image.open(args.file).convert('L')
    else:
        img = Image.open(args.file).convert('RGB')

    # Resize if necessary
    if args.resize:
        w = args.size[0]
        h = args.size[1]
    else:
        w, h = img.size

    # Scales the image by factor S
    o_w = int(w * args.scale)
    o_h = int(h * args.scale)
    img = img.resize((o_w, o_h), Image.NEAREST)

    # Transform img to array
    d_img = np.array(img)

    # Transform pixel by pixel
    if not args.color:
        d_new = dither_bw(d_img, b_matrix)
    if args.color:
        d_new = dither_color(d_img, b_matrix)
    
    # New image based on dithered data
    img_new = Image.fromarray(d_new.astype(np.uint8))

    # Saves the new image
    o_name = args.file.split('.')[0] + '_bayer' + str(args.bayer) + '.png'
    img_new.save(o_name)
    

if __name__ == '__main__':
    main()


