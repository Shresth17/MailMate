from textual.app import App, ComposeResult
from textual.events import Mount
from textual.widgets import Static,Collapsible, Footer, Label, Markdown, DataTable, TextArea, Button
from textual.containers import ScrollableContainer, Vertical
from textual.widgets import Static,Collapsible, Footer, Label, Markdown, DataTable
from textual.containers import ScrollableContainer
from textual.reactive import reactive
from utils.events import *
from utils.llm_query import *



Rows=[("Event" , "Time")]

all_events = get_events()

all_mails = get_mails()
all_mails.sort(key=lambda x: x["time"], reverse=True)

for event in all_events:
    Rows.append((event["Event"],event["Time"]))

def shorten_text(text: str, max_length: int = 19) -> str:
    """Shorten text to max_length."""
    if len(text) <= max_length:
        return text
    return text[:max_length] + ".."

shortened_rows = [(shorten_text(row[0]),row[1]) for row in Rows]

Rows = shortened_rows

class TableApp(Static):
    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*Rows[0])
        table.add_rows(Rows[1:])

