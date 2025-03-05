from typing import NamedTuple
from textwrap import dedent
import pandas as pd
from datetime import datetime, timezone, timedelta
from pathlib import Path


# Define EDT as UTC-4 (fixed offset, does not adjust for DST)
edt = timezone(timedelta(hours=-4), name="EDT")

PLENARY_TALK_DURATION_MIN = 30
PLENARY_TALK_DURATION_SEC = PLENARY_TALK_DURATION_MIN * 60

TALK_DURATION_MIN = 20
TALK_DURATION_SEC = TALK_DURATION_MIN * 60

type_to_duration = {
    "plenary": PLENARY_TALK_DURATION_SEC,
    "oral": TALK_DURATION_SEC,
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

Here you will find the schedule and abstracts for the OSSFE 2025 conference

# Schedule
{tables}
"""
)

template_list_of_posters = dedent(
    """---
title: "List of posters"
---

Here you will find the posters for the OSSFE 2025 conference

The poster session will take place at {poster_time_slot}

In Poster room 1 (Abstract ID's POS-1-31):
{posters_1}

In Poster room 2 (Abstract ID's POS-32-62):
{posters_2}

"""
)

table_template = dedent(
    """\
## Session {session_id}: {time_slot}

Room: {room}

*Chair*: {chair}

Number of presentations: {num_presentations}

{table}
"""
)

opening_session = dedent(
    """\
## 🎉 Welcome statement by the organising committee: {time_slot}

Room: {room}

Presenter: Remi Delaporte-Mathurin
"""
)

closing_session = dedent(
    """\
## 🏆 Awards ceremony and closing remarks: {time_slot}

Room: {room}

Presenter: Remi Delaporte-Mathurin
"""
)

poster_session = dedent(
    """\
## 🖼️  Poster Session: {time_slot}

The poster session will be split between two rooms with:

### Abstract ID's POS-1-31:

Room: {room_1}

### Abstract ID's POS-32-62:

Room: {room_2}

A full list of the posters and their abstracts can be found in the [List of posters](list_of_posters.md)
"""
)

demo_session = dedent(
    """\
## 🛠️ Tutorial Session: {time_slot}

Room: {room}

A series of tutorials will be available to attend for the following packages:

{demos}
"""
)

panel_session = dedent(
    """\
## 🗣️ Panel Session: {time_slot}

Room: {room}

*Chair*: {chair}

A panel session will be held with the following members:
{table}
"""
)

break_template = dedent(
    """\
## ☕ Break: {time_slot}

Take the opportunity to make yourself tea or coffee and network with other attendees in the lobby!
"""
)

lunch_template = dedent(
    """\
## 🍽️ Lunch break: {time_slot}

Or dinner break for Europe! Or breakfast for the West Coast!

The Gather Town will remain open for networking during the break!

"""
)


class TimeSlot:
    """
    Rooms: Talk room 1, Talk room 2, breakout room, Poster room 1, Poster room 2
    types : plenary, oral
    """

    start: datetime
    end: datetime
    room: str
    type: str
    chair: str

    num_presentations: int

    @property
    def num_presentations(self):
        if type_to_duration[self.type] is None:
            return 1
        duration = self.end - self.start
        return int(duration.total_seconds() / type_to_duration[self.type])

    def __init__(self, start, end, room=None, type=None, chair=None):
        self.start = start
        self.end = end
        self.room = room
        self.type = type
        self.chair = chair

    def __str__(self):
        start_minute = str(self.start.minute).zfill(2)
        end_minute = str(self.end.minute).zfill(2)
        return f"{self.start.hour}:{start_minute} - {self.end.hour}:{end_minute} ({self.end.tzinfo})"


def session_to_time(session_id: str):
    if session_id == "S_Opening":
        return TimeSlot(
            start=datetime(2025, 3, 18, 7, 00, tzinfo=edt),
            end=datetime(2025, 3, 18, 7, 10, tzinfo=edt),
            room="Talk room 1",
            type="opening",
            chair="TBC",
        )
    elif session_id == "S_Closing":
        return TimeSlot(
            start=datetime(2025, 3, 18, 15, 10, tzinfo=edt),
            end=datetime(2025, 3, 18, 15, 20, tzinfo=edt),
            room="Talk room 1",
            type="closing",
            chair="TBC",
        )
    elif session_id == "S_P1":
        return TimeSlot(
            start=datetime(2025, 3, 18, 7, 10, tzinfo=edt),
            end=datetime(2025, 3, 18, 8, 10, tzinfo=edt),
            room="Talk room 1",
            type="plenary",
            chair="TBC",
        )
    elif session_id == "S_A":
        return TimeSlot(
            start=datetime(2025, 3, 18, 8, 30, tzinfo=edt),
            end=datetime(2025, 3, 18, 9, 30, tzinfo=edt),
            room="Talk room 1",
            type="oral",
            chair="TBC",
        )
    elif session_id == "S_B":
        return TimeSlot(
            start=datetime(2025, 3, 18, 8, 30, tzinfo=edt),
            end=datetime(2025, 3, 18, 9, 30, tzinfo=edt),
            room="Talk room 2",
            type="oral",
            chair="TBC",
        )
    elif session_id == "S_poster_1":
        return TimeSlot(
            start=datetime(2025, 3, 18, 9, 30, tzinfo=edt),
            end=datetime(2025, 3, 18, 10, 40, tzinfo=edt),
            room="Poster room 1",
        )
    elif session_id == "S_poster_2":
        return TimeSlot(
            start=datetime(2025, 3, 18, 9, 30, tzinfo=edt),
            end=datetime(2025, 3, 18, 10, 40, tzinfo=edt),
            room="Poster room 2",
        )
    elif session_id == "S_demos":
        return TimeSlot(
            start=datetime(2025, 3, 18, 9, 30, tzinfo=edt),
            end=datetime(2025, 3, 18, 10, 40, tzinfo=edt),
            room="Breakout room",
            type="poster",
            chair="TBC",
        )
    elif session_id == "S_Panel":
        return TimeSlot(
            start=datetime(2025, 3, 18, 10, 40, tzinfo=edt),
            end=datetime(2025, 3, 18, 11, 20, tzinfo=edt),
            room="Talk room 1",
            type="panel",
            chair="Jonathan Shimwell, Proxima Fusion",
        )
    elif session_id == "S_P2":
        return TimeSlot(
            start=datetime(2025, 3, 18, 11, 20, tzinfo=edt),
            end=datetime(2025, 3, 18, 11, 50, tzinfo=edt),
            room="Talk room 1",
            type="plenary",
            chair="TBC",
        )
    elif session_id == "S_C":
        return TimeSlot(
            start=datetime(2025, 3, 18, 12, 50, tzinfo=edt),
            end=datetime(2025, 3, 18, 13, 50, tzinfo=edt),
            room="Talk room 1",
            type="oral",
            chair="TBC",
        )
    elif session_id == "S_D":
        return TimeSlot(
            start=datetime(2025, 3, 18, 12, 50, tzinfo=edt),
            end=datetime(2025, 3, 18, 13, 50, tzinfo=edt),
            room="Talk room 2",
            type="oral",
            chair="Nathan Cummings, UKAEA",
        )
    elif session_id == "S_E":
        return TimeSlot(
            start=datetime(2025, 3, 18, 14, 10, tzinfo=edt),
            end=datetime(2025, 3, 18, 15, 10, tzinfo=edt),
            room="Talk room 1",
            type="oral",
            chair="TBC",
        )
    elif session_id == "S_F":
        return TimeSlot(
            start=datetime(2025, 3, 18, 14, 10, tzinfo=edt),
            end=datetime(2025, 3, 18, 15, 10, tzinfo=edt),
            room="Talk room 2",
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
        "poster_id",
    ]

    df = pd.read_csv("abstracts.csv", usecols=columns_to_keep)

    # remove all linebreaks that would cause the markdown to break
    df = df.replace(r"\n", " ", regex=True)

    df_presentation = df[df["Decision"] == "oral"].copy()
    df_poster = df[df["Decision"] == "poster"].copy()
    df_demo = df[df["Decision"] == "demo"].copy()

    df_presentation.loc[:, "slot_number"] = (
        df_presentation["slot_id"].str.extract(r"(\d+)").astype(int)
    )

    # extract session from slot_id (e.g. S_A, S_P1)
    df_presentation.loc[:, "session_id"] = "S_" + df_presentation[
        "slot_id"
    ].str.extract(r"(\D+)")

    # where slot_id is P1 or P2, change session_id to S_P1
    # where slot_id is P3 change session_id to S_P2

    df_presentation.loc[df_presentation["slot_id"].str.contains("P1"), "session_id"] = (
        "S_P1"
    )
    df_presentation.loc[df_presentation["slot_id"].str.contains("P2"), "session_id"] = (
        "S_P1"
    )
    df_presentation.loc[df_presentation["slot_id"].str.contains("P3"), "session_id"] = (
        "S_P2"
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

            author_affiliation_list = item["List of authors and affiliation"].split(";")
            parts = (
                author_affiliation_list[0].strip().split(",", 1)
            )  # Split only at the first comma
            institution_of_first_author = parts[1].strip()

            data.append(
                {
                    "ID": talk_id,
                    "Title": title,
                    "Presenter": presenter,
                    "Institution": institution_of_first_author,
                }
            )

        df_table = pd.DataFrame(data)
        table = df_table.to_markdown(index=False)
        tables.append(
            table_template.format(
                session_id=session.replace("S_", ""),
                time_slot=time_slot,
                room=time_slot.room,
                chair=time_slot.chair,
                num_presentations=time_slot.num_presentations,
                table=table,
            )
        )

    # create item for opening session
    S_opening_time_slot = session_to_time("S_Opening")
    opening_session_str = opening_session.format(
        time_slot=S_opening_time_slot,
        room=S_opening_time_slot.room,
    )
    tables.insert(0, opening_session_str)

    # create item for closing session
    S_closing_time_slot = session_to_time("S_Closing")
    tables.append(
        closing_session.format(
            time_slot=S_closing_time_slot,
            room=S_closing_time_slot.room,
        )
    )

    # create item for poster session
    S_poster_1_time_slot = session_to_time("S_poster_1")
    S_poster_2_time_slot = session_to_time("S_poster_2")
    poster_session_str = poster_session.format(
        time_slot=S_poster_1_time_slot,
        room_1=S_poster_1_time_slot.room,
        room_2=S_poster_2_time_slot.room,
    )
    tables.insert(4, poster_session_str)

    # create item for demos session
    S_demos_time_slot = session_to_time("S_demos")

    data = []
    for index, (_, item) in enumerate(df_demo.iterrows(), start=1):
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

        institution_of_first_author = ""
        try:
            author_affiliation_list = item["List of authors and affiliation"].split(";")
            parts = (
                author_affiliation_list[0].strip().split(",", 1)
            )  # Split only at the first comma
            institution_of_first_author = parts[1].strip()
        except:
            pass
        data.append(
            {
                "ID": f"T{index}",
                "Title": title,
                "Presenter": presenter,
                "Institution": institution_of_first_author,
            }
        )
    df_table = pd.DataFrame(data)
    table = df_table.to_markdown(index=False)
    demo_session_str = demo_session.format(
        time_slot=S_demos_time_slot,
        room=S_demos_time_slot.room,
        demos=table,
    )
    tables.insert(5, demo_session_str)

    # create item for panel session
    S_panel_time_slot = session_to_time("S_Panel")
    presenters = [
        "[Paul Wilson](bios/wilson.md)",
        "[Martin Yagi](bios/yagi.md)",
        "[David Bernhodlt](bios/bernholdt.md)",
        "[Matt Vernacchia](bios/vernacchia.md)",
        "[Aiden Fowler](bios/fowler.md)",
    ]
    affiliations = [
        "[University of Wisconsin-Madison](https://www.wisc.edu/)",
        "[First Light Fusion](https://firstlightfusion.com/)",
        "[ORNL](https://www.ornl.gov/)",
        "[CFS](https://cfs.energy/)",
        "[MIT](https://www.mit.edu/)",
    ]
    assert len(presenters) == len(affiliations), "Number of presenters and affiliations must be equal"
    panel_data = []
    for presenter, affiliation in zip(presenters, affiliations):
        panel_data.append({"Presenter": presenter, "Affiliation": affiliation})

    panel_df_table = pd.DataFrame(panel_data)
    panel_table = panel_df_table.to_markdown(index=False)
    panel_session_str = panel_session.format(
        time_slot=S_panel_time_slot,
        room=S_panel_time_slot.room,
        chair=S_panel_time_slot.chair,
        table=panel_table,
    )
    tables.insert(6, panel_session_str)

    # create items for breaks
    break_1_time_slot = TimeSlot(
        start=datetime(2025, 3, 18, 8, 10, tzinfo=edt),
        end=datetime(2025, 3, 18, 8, 30, tzinfo=edt),
    )
    break_2_time_slot = TimeSlot(
        start=datetime(2025, 3, 18, 13, 50, tzinfo=edt),
        end=datetime(2025, 3, 18, 14, 10, tzinfo=edt),
    )
    tables.insert(2, break_template.format(time_slot=break_1_time_slot))
    tables.insert(11, break_template.format(time_slot=break_2_time_slot))

    # create item for lunch
    lunch_time_slot = TimeSlot(
        start=datetime(2025, 3, 18, 11, 50, tzinfo=edt),
        end=datetime(2025, 3, 18, 12, 50, tzinfo=edt),
    )
    tables.insert(9, lunch_template.format(time_slot=lunch_time_slot))

    # Handle posters

    # Separate into two groups based on 'slot_id'
    df_poster_1 = df_poster[df_poster["slot_id"] == "poster_1"]
    df_poster_2 = df_poster[df_poster["slot_id"] == "poster_2"]

    # sort by poster_id
    df_poster_1 = df_poster_1.sort_values(by=["poster_id"])
    df_poster_2 = df_poster_2.sort_values(by=["poster_id"])

    def create_markdown_table(df_poster):
        data = []

        for _, item in df_poster.iterrows():

            # Extract last name and first word of title
            last_name = item["List of authors and affiliation"].split(",")[0].split()[0]
            first_word_title = item["Title"].replace("-", " ").split()[0]
            filename = f"{last_name}-{first_word_title}.md".lower()

            # Remove invalid characters
            filename = (
                filename.replace(" ", "")
                .replace("/", "")
                .replace(":", "")
                .replace(",", "")
            )

            title = f'[{item["Title"]}](abstracts/{filename})'
            presenter = item["Name"]
            institution_of_first_author = ""
            poster_id = item["poster_id"]
            try:
                author_affiliation_list = item["List of authors and affiliation"].split(
                    ";"
                )
                parts = (
                    author_affiliation_list[0].strip().split(",", 1)
                )  # Split only at the first comma
                institution_of_first_author = parts[1].strip()
            except:
                pass
            data.append(
                {
                    "ID": f"{poster_id}",  # Assign unique ID
                    "Title": title,
                    "Presenter": presenter,
                    "Affilaition": institution_of_first_author,
                }
            )

        df_posters_md = pd.DataFrame(data)
        posters_md = df_posters_md.to_markdown(index=False)

        return posters_md

    # Generate markdown tables
    posters_md_1 = create_markdown_table(df_poster_1)
    posters_md_2 = create_markdown_table(df_poster_2)

    (Path("book") / "README.md").write_text(
        template.format(
            tables="\n\n".join(tables),
        )
    )
    (Path("book") / "list_of_posters.md").write_text(
        template_list_of_posters.format(
            poster_time_slot=session_to_time("S_poster_1"),
            posters_1=posters_md_1,
            posters_2=posters_md_2,
        )
    )


if __name__ == "__main__":
    main()
