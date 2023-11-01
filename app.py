import os
import argparse
from PIL import Image


# receiver 
class ImgModifier:
    def convert(self, img_name:str, quality:int=100, format:str="WEBP", output:str='/', output_filename:str=None):
        try:
            open_image = Image.open(img_name)
            output_dir = self.__dir_maker(output_path=output)

            exact_filename = os.path.basename(img_name)

            image_new_name=''
            if output_filename is None:
                image_new_name = exact_filename.split('.')[0]+'.'+ format.lower()
            else:
                image_new_name = output_filename+'.'+format.lower()
                

            open_image.save(output_dir+image_new_name, format ,quality=quality)
            print(f'[+] {exact_filename} converted to {image_new_name}')
            print('')
        except Exception as e:
            print('[-] An exception occurred.')
            print(img_name)
            print(e)
            print('')
    
    def __dir_maker(self, output_path:str):
        filter_path = output_path if output_path[len(output_path)-1] == '/' else output_path+'/'

        if filter_path == '/':
            absolute_path = os.path.dirname(__file__)
            relative_path = "output"
            full_path = os.path.join(absolute_path, relative_path)

            if not os.path.exists(full_path):
                os.mkdir(full_path)

            filter_path = 'output/'
        return filter_path


# interface
class Command:
    def __init__(self) -> None:
        pass
    
    def execute(self):
        pass


# Concrete command classes
class ImgFormatter(Command):
    def __init__(self, receiver, img_name:str='*', quality:int=100, format:str='WEBP', output:str='/', output_filename:str=None) -> None:
        self.receiver = receiver
        self.img_name = img_name
        self.quality = quality
        self.format = format
        self.output = output 
        self.output_filename = output_filename

    def execute(self):
        self.receiver.convert(img_name=self.img_name, quality=self.quality, format=self.format, output=self.output, output_filename=self.output_filename)
    
    def __repr__(self) -> str:
        return f'Image - {self.img_name}'
        

class MassImgFormatter(Command):
    def __init__(self, receiver, path:str='*', quality:int=100, format:str='WEBP', accepted_format=['jpg','jpeg','png','webp'],  output:str='/') -> None:
        self.receiver = receiver
        self.path = path
        self.quality = quality
        self.format = format
        self.accepted_format = accepted_format
        self.output = output 

    def execute(self):
        files = self.__find_files(directory=self.path)
        for file in files:
            if self.__format_finder(file) in self.accepted_format:
                print(f'[+] {os.path.basename(file)} - file format are matched.')
                self.receiver.convert(img_name=file, quality=self.quality, format=self.format, output=self.output)
            else:
                print(f'[-] {os.path.basename(file)} - format are not matched. Accepted file formats are - {self.accepted_format}')
                print('')
    

    def __find_files(self, directory):
        file_list = []
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                file_list.append(file_path)
        return file_list
    
    def __format_finder(self, fullpath):
        lower_format = os.path.basename(fullpath).split('.')[1].lower()
        return lower_format
    
    def __repr__(self) -> str:
        return f'Path - {self.path}'


# Invoker
class Invoker:
    def __init__(self) -> None:
        self.history = []
    
    def compute(self, command):
        result = command.execute()
        self.history.append(command)
        return self.history


def app():

    print("""
    +-------------------------------+
    |                               |
    |       Img Formatter PY        |
    |           v1.0.1              |
    +-------------------------------+
    """)

    parser = argparse.ArgumentParser(description='Format your image using simple python script. v1.0.1')

    parse_single_image = parser.add_argument_group('Command for single image')
    parse_single_image.add_argument('-n', '--name', type=str, default='*', help='Your image name with extension and path. If you have absolute path.')
    parse_single_image.add_argument('-of', '--output-filename', type=str, default=None, help='Set your output filename.')

    parse_mass_image = parser.add_argument_group('Command for multiple images')
    parse_mass_image.add_argument('-p', '--path', type=str, default=None, help='Write specific directory for all image convert inside that directory')
    parse_mass_image.add_argument('-af', '--accepted-format', type=str, nargs='+', default=None, help='Put your all accepted file format list like - png jpg webp')

    parse_basic = parser.add_argument_group('All common command.')
    parse_basic.add_argument('-f', '--format', type=str, default='WEBP', choices=['jpg','jpeg','png','webp'], help='Select image format type.')
    parse_basic.add_argument('-q', '--quality', type=int, default=100,  help='Put here number of percentage for quality.')
    parse_basic.add_argument('-o', '--output', type=str, default='/', help='Write your image output path.')

    args = parser.parse_args()

    # receiver
    img_modifier = ImgModifier()

    invoker = Invoker()

    if args.path is None:
        command = ImgFormatter(
            receiver = img_modifier, 
            img_name = args.name if args.name is not None else None,
            quality = args.quality if args.quality is not None else 100, 
            format = args.format.upper() if args.format is not None else 'WEBP',
            output = args.output if args.output is not None else '/',
            output_filename = args.output_filename if args.output_filename is not None else None
            )
        result = invoker.compute(command=command)
        print(f'[+] Done - {result}')
    else:
        command = MassImgFormatter(
            receiver = img_modifier, 
            path = args.path if args.path is not None else '',
            quality = args.quality if args.quality is not None else 100, 
            format = args.format.upper() if args.format is not None else 'WEBP',
            output = args.output if args.output is not None else '/',
            accepted_format = args.accepted_format if args.accepted_format is not None else ['jpg','jpeg','png','webp']
        )
        result = invoker.compute(command=command)
        print(f'[+] Done - {result}')

        


if __name__ == '__main__':
    app()