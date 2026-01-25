import sys
from pathlib import Path
def comment_out_test_calls(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as infile, \
         open(output_file, "w", encoding="utf-8") as outfile:

        for line in infile:
            stripped = line.rstrip("\n")

            # Check if the line ends with "_test()" (ignoring trailing spaces)
            if stripped.rstrip().endswith("_test()"):
                # Preserve indentation
                indentation = stripped[:len(stripped) - len(stripped.lstrip())]
                outfile.write(f"{indentation}# {stripped.lstrip()}\n")
            else:
                outfile.write(line)


if __name__ == "__main__":
    if False and len(sys.argv) != 3:
        print("Usage: python comment_tests.py <input_file.py> <output_file.py>")
        sys.exit(1)

    input_file = "coding-qns.py"
    output_file = "coding-qns-commented.py"

    #input_path = Path(sys.argv[1])
    #output_path = Path(sys.argv[2])

    comment_out_test_calls(input_path, output_path)
