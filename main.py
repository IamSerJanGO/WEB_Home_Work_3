from pathlib import Path
import argparse
from shutil import copy2
from threading import Thread
import logging
from time import sleep  # Імпортуємо sleep для використання

parser = argparse.ArgumentParser(description='Folder sorted')
parser.add_argument('--source', '-s',  help="Source folder", required=True)
parser.add_argument('--output', '-o',  help="Output folder", default='new_folder')

args = vars(parser.parse_args())

source = Path(args.get('source'))
output = Path(args.get('output'))

folders = []

def parse_folder(path: Path):  
    for elem in path.iterdir():
        if elem.is_dir():
            folders.append(elem)
            parse_folder(elem) 

def copy_file(path: Path):
    for elem in path.iterdir():
        if elem.is_file():
            pref = elem.suffix
            if pref:
                pref_path = output / pref[1:]  
                try:
                    pref_path.mkdir(exist_ok=True, parents=True)
                    copy2(elem, pref_path / elem.name)  
                except OSError as e:
                    logging.error(e)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(threadName)s %(message)s")
    folders.append(source)
    parse_folder(source)
    sleep(3)
    thread = []
    for folder in folders:
        th = Thread(target=copy_file, args=(folder,))
        th.start()
        thread.append(th)

    [th.join() for th in thread]
    print('The end')
