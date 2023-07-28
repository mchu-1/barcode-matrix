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
    parser.add_argument("-t", "--transform", type=str, help="Transform", default=True)

    args = parser.parse_args()

    return args

def generate_matrices_from_directory(input_d, output_d, config_f: str, transform: bool = True) -> None:
    """
    Generate matrices from FASTQ files in directory.
    Plot matrices and save to output directory.
    """
    # Get all FASTQ files in directory
    input_d = Path(input_d)
    fastq_files = input_d.glob("*.fastq")
    # Convert to list of strings
    fastq_files = [str(fastq_file) for fastq_file in fastq_files]

    # Generate matrices and write to output directory
    for fastq_file in fastq_files:
        fastq_name = fastq_file.split("/")[-1].split(".")[0].split("_")[0]
        print(f"Generating matrix for {fastq_file} ...")
        A = generate_matrix(fastq_file, config_f)
        print(f"Visualizing matrix for {fastq_file} ...")
        G = visualize_matrix(A, transform)
        # Save figure with height 1000 px, transparent background
        G.savefig(f"{output_d}/{fastq_name}.png", dpi=500, transparent=True)
        # Clear plot
        plt.clf()

    print("Done.")


if __name__ == "__main__":
    args = parse_args()
    generate_matrices_from_directory(args.input, args.output, args.config, args.transform)







