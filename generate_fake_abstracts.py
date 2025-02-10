from typing import Sequence
import argparse
from pathlib import Path
from faker import Faker
import csv

slot_ids = [
    "P1",
    "P2",
    "P3",
    "A1",
    "A2",
    "A3",
    "B1",
    "B2",
    "B3",
    "C1",
    "C2",
    "C3",
    "D1",
    "D2",
    "D3",
    "E1",
    "E2",
    "E3",
    "F1",
    "F2",
    "F3",
]


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


def abstract_id_to_session_id(abstract_id: int) -> str:
    if abstract_id <= 2:
        return "S_P1"
    elif abstract_id == 3:
        return "S_P2"
    else:
        session_index = (abstract_id - 4) // 3
        session_ids = ["S_A", "S_B", "S_C", "S_D", "S_E", "S_F"]
        if session_index < len(session_ids):
            return session_ids[session_index]
        else:
            return (
                "S_poster"  # Handle cases where there are more abstracts than expected
            )


def abstract_id_to_slot_id(abstract_id: int) -> str:
    if abstract_id <= 20:
        return slot_ids[abstract_id]
    else:
        return "poster"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("path", type=Path)
    parser.add_argument("N", type=int, default=10)
    args = vars(parser.parse_args(argv))

    fake = Faker()
    fake.seed_instance(4321)

    path = Path(args["path"]).with_suffix(".csv")

    fieldnames = [
        "Abstract ID",
        "Name",
        "Email",
        "Type of submission",
        "Topic",
        "Title",
        "Abstract",
        "List of authors and affiliation",
        "Link to open-source software repository (if applicable)",
        "Recommendation",
        "Decision",
        "slot_id",
    ]
    with path.open("w") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(args["N"]):
            num_authors = fake.random_int(1, 5)
            data = {
                "Abstract ID": int(i + 1),
                "Name": fake.name(),
                "Email": fake.email(),
                "Type of submission": fake.word(),
                "Topic": fake.word(),
                "Title": fake.sentence(),
                "Abstract": fake.text(),
                "List of authors and affiliation": "; ".join(
                    [f"{fake.name()}, {fake.company()}" for _ in range(num_authors)]
                ),
                "Link to open-source software repository (if applicable)": fake.url(),
                "Recommendation": (
                    "oral"
                    if abstract_id_to_session_id(i + 1) != "S_poster"
                    else "poster"
                ),
                "Decision": (
                    "oral"
                    if abstract_id_to_session_id(i + 1) != "S_poster"
                    else "poster"
                ),
                "slot_id": abstract_id_to_slot_id(i),
            }
            writer.writerow(data)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
