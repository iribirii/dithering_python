# Dithering in python

Dithering in python is a small script that only does that, styling a picture with 1-bit bayer ordered dithering or color bayer ordered dithering.

## Installation

Clone the github repository:
```bash
git clone https://github.com/iribirii/dithering_python.git
```

## Usage
```python
python dithering_python.py [-h][-c][-r RESIZE_X RESIZE_Y][-s SCALE_FACTOR][-b BAYER] file
```
## Options and examples

The script has some different options that you can choose.
- The dimension of the **bayer** matrix that will be used for the style (1, 2, 3 or 4)
- Black&White style or **color**.
- **Resize** the image with X and Y selected values
- **Scale** the image by a factor. <1 for a more *pixel-art* kind of result.

### Black and white examples
B&W gradient with bayer dimension 2, 3 and 4:

![bnw b2](/examples/black_and_white/bnw_bayer2.png) ![bnw b3](/examples/black_and_white/bnw_bayer3.png) ![bnw b4](/examples/black_and_white/bnw_bayer4.png)

### Color examples:
RGB spectrum with bayer dimension 2, 3 and 4:

![c b2](/examples/color/color_bayer2.png) ![c b3](/examples/color/color_bayer3.png) ![c b4](/examples/color/color_bayer4.png)

## Animation example:

![animation](/examples/animation/animation.gif)

## Contributing
Any pull requests are wolcome. 

## License
[MIT](https://choosealicense.com/licenses/mit/)
