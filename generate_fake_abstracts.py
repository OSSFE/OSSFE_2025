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
            return "S_poster"  # Handle cases where there are more abstracts than expected

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
        "Horodateur",
        "Name",
        "Email",
        "Are you a student and if so would you like to enter the best student poster/presentation competition?",
        "Type of submission",
        "Topic",
        "Title",
        "Abstract",
        "List of authors and affiliation",
        "How does this submission relate to open-source?",
        "Link to open-source software repository (if applicable)",
        "Do you agree to the following conditions to submit your abstract to the OSSFE 2025 Conference?",
        "Notes",
        "Name of reviewer",
        "Open source (1 or 0)",
        "Fusion relevant? (1 or 0)",
        "Permissive license (1 or 0)",
        "Open-source stack (1 or 0)",
        "Documentation (0 to 1)",
        "Scientific and technical relevant (?/3)",
        "Total score",
        "Recommendation",
        "slot_id",
        "session_id"
    ]
    with path.open("w") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(args["N"]):
            num_authors = fake.random_int(1, 5)
            empty_ref_list = fake.random_int(0, 1)
            data = {
                "Abstract ID": fake.uuid4(),
                "Horodateur": fake.date_time(),
                "Name": fake.name(),
                "Email": fake.email(),
                "Are you a student and if so would you like to enter the best student poster/presentation competition?": fake.boolean(),
                "Type of submission": fake.word(),
                "Topic": fake.word(),
                "Title": fake.sentence(),
                "Abstract": fake.text(),
                "List of authors and affiliation": authors(fake, num_authors) + ", " + affiliations(fake, num_authors),
                "How does this submission relate to open-source?": fake.text(),
                "Link to open-source software repository (if applicable)": fake.url(),
                "Do you agree to the following conditions to submit your abstract to the OSSFE 2025 Conference?": "Yes",
                "Notes": fake.sentence(),
                "Name of reviewer": fake.name(),
                "Open source (1 or 0)": fake.random_element(elements=[0, 1]),
                "Fusion relevant? (1 or 0)": fake.random_element(elements=[0, 1]),
                "Permissive license (1 or 0)": fake.random_element(elements=[0, 1]),
                "Open-source stack (1 or 0)": fake.random_element(elements=[0, 1]),
                "Documentation (0 to 1)": fake.random_element(elements=[0, 1]),
                "Scientific and technical relevant (?/3)": fake.random_int(min=0, max=3),
                "Total score": fake.random_int(min=0, max=10),
                "Recommendation": "oral" if abstract_id_to_session_id(i) != "S_poster" else "poster",
                "slot_id": fake.word(),
                "session_id": abstract_id_to_session_id(i)
            }
            writer.writerow(data)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
