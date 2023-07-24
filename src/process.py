# process.py

"""Process sequencing data from FASTQ file."""

def get_sequences_from_file(input_f: str) -> list[str]:
    """
    Get sequences from FASTQ file.
    """
    if input_f.split(".")[-1] != "fastq":
        raise ValueError("Input file should be in FASTQ format")

    sequences = []
    print(f"Accessing sequencing file {input_f} ...")
    with open(input_f, "r") as sequencing_f:
        marker = 0
        for line in sequencing_f:
            if marker == 1:
                new_sequence = line.rstrip()
                sequences.append(new_sequence)
                marker = 0
            elif line[0] == "@":
                marker = 1
                continue
            else:
                continue

    return sequences