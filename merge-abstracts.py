import argparse
from typing import Sequence
from pathlib import Path
from pypdf import PdfWriter

here = Path(__file__).parent


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input", type=Path, default=None)
    parser.add_argument("-o", "--output", type=Path, default=None)
    args = vars(parser.parse_args(argv))

    if args["input"] is None:
        input_folder = here / "book" / "_build" / "exports"
    else:
        input_folder = args["input"]

    if args["output"] is None:
        output_file = here / "book" / "_build" / "exports" / "all-abstracts.pdf"
    else:
        output_file = Path(args["output"]).with_suffix(".pdf")

    if not input_folder.exists():
        print(f"{input_folder} does not exist")
        return 1
    output_file.parent.mkdir(parents=True, exist_ok=True)
    abstracts = filter(
        lambda x: not (x.stem.startswith("readme") or x.stem.startswith("all-abstracts")),
        input_folder.glob("*.pdf"),
    )

    merger = PdfWriter()
    for f in [input_folder / "readme.pdf"] + list(abstracts):
        merger.append(f)

    merger.write(output_file)
    print("Saved to: ", output_file)
    merger.close()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())