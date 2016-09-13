import argparse
import os
import shutil

from astroplan import download_IERS_A
from astropy.utils import data


def download_all_files(data_folder=None):
    download_IERS_A()

    if data_folder is None:
        data_folder = "{}/astrometry/data".format(os.getenv('PANDIR'))

    for i in range(4214, 4219):
        fn = 'index-{}.fits'.format(i)
        dest = "{}/{}".format(data_folder, fn)

        if not os.path.exists(dest):
            url = "http://data.astrometry.net/4200/{}".format(fn)
            df = data.download_file(url)
            try:
                shutil.move(df, dest)
            except OSError as e:
                print("Problem saving. (Maybe permissions?): {}".format(e))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('--folder', help='Folder to place astrometry data')

    args = parser.parse_args()

    if args.folder and not os.path.exists(args.folder):
        print("{} does not exist.".format(args.folder))

    download_all_files(data_folder=args.folder)
