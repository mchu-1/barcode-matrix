# main.py

import argparse
from pathlib import Path
from visualize import *

def parse_args() -> argparse.Namespace:
    """
    Parse settings file for model.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, help="Input directory", required=True)
    parser.add_argument("-o", "--output", type=str, help="Output directory", default="./out")
    parser.add_argument("-c", "--config", type=str, help="Config file", default="./config.yaml")
    parser.add_argument("-t", "--transform", type=str, help="Transform", default=False)

    args = parser.parse_args()

    return args

def generate_matrices_from_directory(input_d, output_d, config_f: str, transform: bool = False) -> None:
    """
    Generate matrices from FASTQ files in directory.
    Plot matrices and save to output directory.
    """
    # Get all FASTQ files in directory
    input_d = Path(input_d)
    fastq_files = input_d.glob("*.fastq")

    # Get names of fastq files
    fastq_names = [fastq_file.stem.split("_")[0] for fastq_file in fastq_files]

    # Generate matrices and write to output directory
    for fastq_file, fastq_name in zip(fastq_files, fastq_names):
        print(f"Generating matrix for {fastq_file} ...")
        A = generate_matrix(fastq_file, config_f)
        print(f"Visualizing matrix for {fastq_file} ...")
        G = visualize_matrix(A, transform)
        G.savefig(f"{output_d}/{fastq_name}.png")

    print("Done.")


if __name__ == "__main__":
    args = parse_args()
    generate_matrices_from_directory(args.input, args.output, args.config, args.transform)







