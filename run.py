from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os

import midv500


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset_dir", required=True, help="Path to store dataset.")
    parser.add_argument(
        "--convert_to_coco",
        action="store_true",
        help="Create annotation in coco format",
    )
    args = parser.parse_args()

    # Download and unzip midv500 and midv2019 dataset
    dataset_dir = args.dataset_dir
    midv500.download_dataset(dataset_dir)

    # Set directory for coco annotations to be saved
    for d in os.listdir(dataset_dir):
        src = dataset_dir + d + "/"
        dst = dataset_dir + d + "/"
        midv500.convert_to_coco(src, dst, d)


if __name__ == "__main__":
    main()
