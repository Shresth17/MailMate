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

