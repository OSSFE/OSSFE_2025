from typing import Sequence
import argparse
from pathlib import Path
from faker import Faker
import csv


def authors(fake: Faker, n: int) -> str:
    authors = []
    for i in range(n):
        authors.append(fake.name())
    return ", ".join(authors)


def affiliations(fake: Faker, n: int) -> str:
    affiliations = []
    for i in range(n):
        affiliations.append(fake.company())
    return ", ".join(affiliations)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("path", type=Path)
    parser.add_argument("N", type=int, default=10)
    args = vars(parser.parse_args(argv))

    fake = Faker()
    fake.seed_instance(4321)

    path = Path(args["path"]).with_suffix(".csv")

    fieldnames = [
        "Username",
        "Abstract title",
        "Abstract text",
        "Name of authors (including presenter, comma-separated list)",
        "Affiliation of co-authors (including presenter, comma-separated list)",
        "Reference list",
    ]
    with path.open("w") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(args["N"]):
            num_authors = fake.random_int(1, 5)
            empty_ref_list = fake.random_int(0, 1)
            data = {
                "Username": fake.email(),
                "Abstract title": fake.sentence(),
                "Abstract text": fake.text(),
                "Name of authors (including presenter, comma-separated list)": authors(fake, num_authors),
                "Affiliation of co-authors (including presenter, comma-separated list)": affiliations(
                    fake, num_authors
                ),
                "Reference list": fake.text() if not empty_ref_list else "",
            }
            writer.writerow(data)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
