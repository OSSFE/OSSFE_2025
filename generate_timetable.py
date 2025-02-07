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

CLOSING_TALK_DURATION_MIN = 10
CLOSING_TALK_DURATION_SEC = CLOSING_TALK_DURATION_MIN * 60


type_to_duration = {
    "plenary": PLENARY_TALK_DURATION_SEC,
    "oral": TALK_DURATION_SEC,
    "poster": None,
    "opening": OPENING_TALK_DURATION_SEC,
    "closing": CLOSING_TALK_DURATION_SEC,
    "panel": None,  # only one panel discussion
}

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

> [!WARNING]  
> This is work in progress. This schedule contains fake abstracts for now. The abstracts are not yet reviewed.

Here you will find the abstracts for the OSSFE 2025 conference

# Presentations
{tables}

# Posters {poster_time_slot}
{posters}
"""
)

table_template = dedent(
    """\
## Session {session_id}: {time_slot}

Room: {room}

Chair: {chair}

{table}
"""
)


class TimeSlot(NamedTuple):
    """
    Rooms: MIT, APACHE, GNU, BSD
    types : plenary, oral, poster, opening, closing, panel
    """

    start: datetime.datetime
    end: datetime.datetime
    room: str
    type: str
    chair: str

    def num_presentations(self):
        if type_to_duration[self.type] is None:
            return 1
        duration = self.end - self.start
        return int(duration.total_seconds() / type_to_duration[self.type])

    def __str__(self):
        start_minute = str(self.start.minute).zfill(2)
        end_minute = str(self.end.minute).zfill(2)
        num_presentations = f"Number of presentations: {self.num_presentations()}"
        return f"{self.start.hour}:{start_minute} - {self.end.hour}:{end_minute} (EST) \n{num_presentations}"


def session_to_time(session_id: str):
    if session_id == "S_Opening":
        return TimeSlot(
            start=datetime.datetime(2025, 3, 18, 7, 00),
            end=datetime.datetime(2025, 3, 18, 7, 10),
            room="MIT",
            type="opening",
            chair="TBC",
        )
    elif session_id == "S_Closing":
        return TimeSlot(
            start=datetime.datetime(2025, 3, 18, 15, 10),
            end=datetime.datetime(2025, 3, 18, 15, 20),
            room="MIT",
            type="closing",
            chair="TBC",
        )
    elif session_id == "S_P1":
        return TimeSlot(
            start=datetime.datetime(2025, 3, 18, 7, 10),
            end=datetime.datetime(2025, 3, 18, 8, 10),
            room="MIT",
            type="plenary",
            chair="TBC",
        )
    elif session_id == "S_A":
        return TimeSlot(
            start=datetime.datetime(2025, 3, 18, 8, 30),
            end=datetime.datetime(2025, 3, 18, 9, 30),
            room="MIT",
            type="oral",
            chair="TBC",
        )
    elif session_id == "S_B":
        return TimeSlot(
            start=datetime.datetime(2025, 3, 18, 8, 30),
            end=datetime.datetime(2025, 3, 18, 9, 30),
            room="Apache",
            type="oral",
            chair="TBC",
        )
    elif session_id == "S_poster":
        return TimeSlot(
            start=datetime.datetime(2025, 3, 18, 9, 30),
            end=datetime.datetime(2025, 3, 18, 10, 40),
            room="GNU",
            type="poster",
            chair="TBC",
        )
    elif session_id == "S_demos":
        return TimeSlot(
            start=datetime.datetime(2025, 3, 18, 9, 30),
            end=datetime.datetime(2025, 3, 18, 10, 40),
            room="GNU",
            type="poster",
            chair="TBC",
        )
    elif session_id == "S_Panel":
        return TimeSlot(
            start=datetime.datetime(2025, 3, 18, 10, 40),
            end=datetime.datetime(2025, 3, 18, 11, 20),
            room="MIT",
            type="panel",
            chair="TBC",
        )
    elif session_id == "S_P2":
        return TimeSlot(
            start=datetime.datetime(2025, 3, 18, 11, 20),
            end=datetime.datetime(2025, 3, 18, 11, 50),
            room="MIT",
            type="plenary",
            chair="TBC",
        )
    elif session_id == "S_C":
        return TimeSlot(
            start=datetime.datetime(2025, 3, 18, 12, 50),
            end=datetime.datetime(2025, 3, 18, 13, 50),
            room="MIT",
            type="oral",
            chair="TBC",
        )
    elif session_id == "S_D":
        return TimeSlot(
            start=datetime.datetime(2025, 3, 18, 12, 50),
            end=datetime.datetime(2025, 3, 18, 13, 50),
            room="Apache",
            type="oral",
            chair="TBC",
        )
    elif session_id == "S_E":
        return TimeSlot(
            start=datetime.datetime(2025, 3, 18, 14, 10),
            end=datetime.datetime(2025, 3, 18, 15, 10),
            room="MIT",
            type="oral",
            chair="TBC",
        )
    elif session_id == "S_F":
        return TimeSlot(
            start=datetime.datetime(2025, 3, 18, 14, 10),
            end=datetime.datetime(2025, 3, 18, 15, 10),
            room="Apache",
            type="oral",
            chair="TBC",
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
        "Decision",
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

    panel_session = {
        "Abstract ID": "Panel",
        "Name": "Panel",
        "Title": "Panel discussion",
        "Abstract": "Join us for a panel discussion",
        "List of authors and affiliation": "TBD",
        "Recommendation": "oral",
        "slot_id": "S_Panel",
        "session_id": "S_Panel",
    }

    df = pd.concat(
        [df, pd.DataFrame([opening_talk, closing_talk, panel_session])],
        ignore_index=True,
    )

    # remove all linebreaks that would cause the markdown to break
    df = df.replace(r"\n", " ", regex=True)

    df_presentation = df[df["Decision"] == "oral"].copy()
    df_poster = df[df["Decision"] == "poster"].copy()

    df_presentation.loc[:, "slot_number"] = (
        df_presentation["slot_id"].str.extract(r"(\d+)").astype(int)
    )

    # Group by day and session
    grouped = df_presentation.sort_values(by=["session_id", "slot_number"]).groupby(
        "session_id", sort=True
    )

    # sort by time
    grouped = sorted(grouped, key=lambda x: session_to_time(x[0]).start)

    # Create a table for each group
    tables = []
    for session, group in grouped:
        data = []
        time_slot = session_to_time(session)

        for idx, (_, item) in enumerate(group.iterrows(), start=1):
            # filename is last-name of author + first word of title
            last_name = item["List of authors and affiliation"].split(",")[0].split()[0]
            first_word_title = item["Title"].replace("-", " ").split()[0]
            filename = f"{last_name}-{first_word_title}.md".lower()

            # remove invalid characters
            filename = (
                filename.replace(" ", "")
                .replace("/", "")
                .replace(":", "")
                .replace(",", "")
            )

            title = f'[{item["Title"]}](abstracts/{filename})'
            presenter = item["Name"]

            # breakpoint()
            talk_id = item["slot_id"]
            data.append({"ID": talk_id, "Title": title, "Presenter": presenter})

        df_table = pd.DataFrame(data)
        table = df_table.to_markdown(index=False)
        tables.append(
            table_template.format(
                session_id=session.replace("S_", ""),
                time_slot=time_slot,
                room=time_slot.room,
                chair=time_slot.chair,
                table=table,
            )
        )

    data = []
    for index, (_, item) in enumerate(df_poster.iterrows(), start=1):
        # filename is last-name of author + first word of title
        last_name = item["List of authors and affiliation"].split(",")[0].split()[0]
        first_word_title = item["Title"].replace("-", " ").split()[0]
        filename = f"{last_name}-{first_word_title}.md".lower()

        # remove invalid characters
        filename = (
            filename.replace(" ", "").replace("/", "").replace(":", "").replace(",", "")
        )

        title = f'[{item["Title"]}](abstracts/{filename})'
        presenter = item["Name"]
        data.append({"ID": index, "Title": title, "Presenter": presenter})

    df_posters_md = pd.DataFrame(data)
    posters_md = df_posters_md.to_markdown(index=False)

    (Path("book") / "README.md").write_text(
        template.format(
            tables="\n\n".join(tables),
            posters=posters_md,
            poster_time_slot=session_to_time("S_poster"),
        )
    )


if __name__ == "__main__":
    main()
