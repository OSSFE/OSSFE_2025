from typing import NamedTuple
from enum import IntEnum, auto
from textwrap import dedent
import pandas as pd
import datetime
from pathlib import Path


PLENARY_TALK_DURATION_MIN = 30
PLENARY_TALK_DURATION_SEC = PLENARY_TALK_DURATION_MIN * 60

TALK_DURATION_MIN = 20
TALK_DURATION_SEC = TALK_DURATION_MIN * 60

OPENING_TALK_DURATION_MIN = 10
OPENING_TALK_DURATION_SEC = OPENING_TALK_DURATION_MIN * 60

template = dedent(
    """---
title: "OSSFE conference 2025 - March 18th"
authors:
  - name: James Dark
    affiliations:
      - Plasma Science and Fusion Centre, MIT
    email: ossfe2025@gmail.com
  - name: Rémi Delaporte-Mathurin
    affiliations:
      - Plasma Science and Fusion Centre, MIT
    email: ossfe2025@gmail.com
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../template
---

Here you will find the abstracts for the OSSFE 2025 conference

# Presentations
{tables}

# Posters
{posters}
"""
)

table_template = dedent(
    """\
## {session_id}: {time_slot}

Chair: TBA

{table}
"""
)


class TimeSlot(NamedTuple):
    """
    Rooms: MIT, APACHE, GNU, BSD
    """

    start: datetime.datetime
    end: datetime.datetime
    room: str

    def num_presentations(self):
        duration = self.end - self.start
        return int(duration.total_seconds() / TALK_DURATION_SEC)

    def __str__(self):
        start_minute = str(self.start.minute).zfill(2)
        end_minute = str(self.end.minute).zfill(2)
        num_presentations = f"Number of presentations: {self.num_presentations()}"
        return f"{self.start.hour}:{start_minute} - {self.end.hour}:{end_minute}\n{num_presentations}"


def session_to_time(session_id: str):
    if session_id == "S_Opening":
        return TimeSlot(
            start=datetime.datetime(2025, 3, 18, 7, 00),
            end=datetime.datetime(2025, 3, 18, 7, 10),
            room="MIT",
        )
    elif session_id == "S_Closing":
        return TimeSlot(
            start=datetime.datetime(2025, 3, 18, 15, 10),
            end=datetime.datetime(2025, 3, 18, 15, 20),
            room="MIT",
        )
    elif session_id == "S_P1":
        return TimeSlot(
            start=datetime.datetime(2025, 3, 18, 7, 10),
            end=datetime.datetime(2025, 3, 18, 8, 10),
            room="MIT",
        )
    elif session_id == "S_A":
        return TimeSlot(
            start=datetime.datetime(2025, 3, 18, 8, 30),
            end=datetime.datetime(2025, 3, 18, 9, 30),
            room="MIT",
        )
    elif session_id == "S_B":
        return TimeSlot(
            start=datetime.datetime(2025, 3, 18, 8, 30),
            end=datetime.datetime(2025, 3, 18, 9, 30),
            room="Apache",
        )
    elif session_id == "S_poster":
        return TimeSlot(
            start=datetime.datetime(2025, 3, 18, 9, 30),
            end=datetime.datetime(2025, 3, 18, 10, 40),
            room="GNU",
        )
    elif session_id == "S_demos":
        return TimeSlot(
            start=datetime.datetime(2025, 3, 18, 9, 30),
            end=datetime.datetime(2025, 3, 18, 10, 40),
            room="GNU",
        )
    elif session_id == "S_panel":
        return TimeSlot(
            start=datetime.datetime(2025, 3, 18, 10, 40),
            end=datetime.datetime(2025, 3, 18, 11, 20),
            room="MIT",
        )
    elif session_id == "S_P2":
        return TimeSlot(
            start=datetime.datetime(2025, 3, 18, 11, 20),
            end=datetime.datetime(2025, 3, 18, 11, 50),
            room="MIT",
        )
    elif session_id == "S_C":
        return TimeSlot(
            start=datetime.datetime(2025, 3, 18, 12, 50),
            end=datetime.datetime(2025, 3, 18, 13, 50),
            room="MIT",
        )
    elif session_id == "S_D":
        return TimeSlot(
            start=datetime.datetime(2025, 3, 18, 12, 50),
            end=datetime.datetime(2025, 3, 18, 13, 50),
            room="Apache",
        )
    elif session_id == "S_E":
        return TimeSlot(
            start=datetime.datetime(2025, 3, 18, 14, 10),
            end=datetime.datetime(2025, 3, 18, 15, 10),
            room="MIT",
        )
    elif session_id == "S_F":
        return TimeSlot(
            start=datetime.datetime(2025, 3, 18, 14, 10),
            end=datetime.datetime(2025, 3, 18, 15, 10),
            room="Apache",
        )

    raise ValueError(f"Unknown session {session_id}")


def main():

    columns_to_keep = [
        "Abstract ID",
        "Name",
        "Email",
        "Topic",
        "Title",
        "Abstract",
        "List of authors and affiliation",
        "Link to open-source software repository (if applicable)",
        "Recommendation",
        "slot_id",
        "session_id",
    ]

    df = pd.read_csv("abstract_testing.csv", usecols=columns_to_keep)

    # add opening and closing talk to the dataframe
    opening_talk = {
        "Abstract ID": "Opening",
        "Name": "Remi Delaporte-Mathurin",
        "Title": "Welcome to OSSFE 2025",
        "Abstract": "Welcome to the 2025 edition of the Open Source Software for Fusion Energy conference",
        "List of authors and affiliation": "Remi Delaporte-Mathurin, Plasma Science and Fusion Center, MIT",
        "Recommendation": "oral",
        "slot_id": "S_Opening",
        "session_id": "S_Opening",
    }

    closing_talk = {
        "Abstract ID": "Closing",
        "Name": "Remi Delaporte-Mathurin",
        "Title": "Closing remarks",
        "Abstract": "Thank you for attending the 2025 edition of the Open Source Software for Fusion Energy conference",
        "List of authors and affiliation": "Remi Delaporte-Mathurin, Plasma Science and Fusion Center, MIT",
        "Recommendation": "oral",
        "slot_id": "S_Closing",
        "session_id": "S_Closing",
    }

    df = pd.concat([df, pd.DataFrame([opening_talk, closing_talk])], ignore_index=True)

    # remove all linebreaks that would cause the markdown to break
    df = df.replace(r"\n", " ", regex=True)

    df_presentation = df[df["Recommendation"] == "oral"]
    df_poster = df[df["Recommendation"] == "poster"]

    # Group by day and session
    grouped = df_presentation.groupby(
        "session_id",
        sort=True,
    )

    # sort by time
    grouped = sorted(grouped, key=lambda x: session_to_time(x[0]).start)

    grouped_dict = {session_id: group for session_id, group in grouped}

    # Create a table for each group
    tables = []
    for session, group in grouped:
        print(session)
        data = []
        time_slot = session_to_time(session)

        for idx, (_, item) in enumerate(group.iterrows(), start=1):
            # filename is last-name of author + first word of title
            last_name = item["List of authors and affiliation"].split(",")[0].split()[0]
            first_word_title = item["Title"].replace("-", " ").split()[0]
            filename = f"{last_name}-{first_word_title}.md".lower()
    
            title = f'[{item["Title"]}](abstracts/{filename})'
            presenter = item["Name"]

            # breakpoint()
            talk_id = f"{session.replace('S_', '')}{idx}"
            data.append({"ID": talk_id, "Title": title, "Presenter": presenter})

        df_table = pd.DataFrame(data)
        table = df_table.to_markdown(index=False)
        tables.append(table_template.format(session_id=session.replace("S_", ""), time_slot=time_slot, table=table))

    data = []
    for index, (_, item) in enumerate(df_poster.iterrows(), start=1):
        filename = f"{item["Title"].replace(" ", "-").lower()}.md"
        title = f'[{item["Title"]}](abstracts/{filename})'
        presenter = item["Name"]
        data.append({"ID": index, "Title": title, "Presenter": presenter})

    df_posters_md = pd.DataFrame(data)
    posters_md = df_posters_md.to_markdown(index=False)

    (Path("book") / "README.md").write_text(
        template.format(tables="\n\n".join(tables), posters=posters_md)
    )


if __name__ == "__main__":
    main()
