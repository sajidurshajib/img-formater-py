# 📸 Img Formatter PY v1.0.1

Img Formatter PY is a Python script that allows you to format images easily. You can format a single image or multiple images located within a specific directory. The script supports various image formats and provides options to customize the output format and quality.


## Installation
Before using Img Formatter PY, make sure to install the required packages. You can install them using pip (or pip3) with the following command:

```bash
pip3 install -r requirements.txt
```

## Usage

```bash
python3 app.py [-h] [-n NAME] [-of OUTPUT_FILENAME] [-p PATH] [-af ACCEPTED_FORMAT [ACCEPTED_FORMAT ...]]
              [-f {jpg,jpeg,png,webp}] [-q QUALITY] [-o OUTPUT]
```

### Command for Single Image:

```bash
-n, --name NAME          Your image name with extension and path. If you have an absolute path.
-of, --output-filename OUTPUT_FILENAME
                        Set your output filename.
```

### Command for Multiple Images:

```bash
-p, --path PATH          Specify a directory for converting all images inside that directory.
-af, --accepted-format ACCEPTED_FORMAT [ACCEPTED_FORMAT ...]
                        List all accepted file formats like: png jpg webp
```

### Common Commands:

```bash
-f, --format {jpg,jpeg,png,webp}
                        Select the output image format type.
-q, --quality QUALITY   Set the image quality as a percentage.
-o, --output OUTPUT     Specify the output path for the formatted image(s).
```

### Example Usage:

Format a single image:

```bash
python3 app.py -n input_image.jpg -f jpg -q 80 -o /output -of new
```

Format multiple images in a directory:

```bash
python3 app.py -p /path/to/images -af png jpg -f webp -q 70 -o /path/to/output
```

## Development Details

This project was developed using the command pattern for efficient command-line argument parsing and execution.

### Installing as a Command-Line Tool

To use Img Formatter PY as a command-line tool, move the `app.py` script to a directory in your system's PATH, such as `~/bin`. Ensure the script has executable permissions:

```bash
mv app.py ~/bin/imgformatter
chmod +x ~/bin/imgformatter
```

Now you can use `imgformatter` as a command in your terminal:

```bash
imgformatter -n input_image.jpg -f jpg -q 80 -o /output
```

