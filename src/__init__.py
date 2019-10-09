from .containers import *
from .events import *
from struct import unpack, pack
from .util import *
from .fileio import *


def get_subclasses(base):
    subs = set(base.__subclasses__())
    recursive = set(e for a in subs for e in get_subclasses(a))
    subs.update(recursive)
    return subs


def populate_eventregistry():
    events = get_subclasses(AbstractEvent).difference(
        {AbstractEvent, Event, MetaEvent, NoteEvent, MetaEventWithText}
    )
    for event in events:
        EventRegistry.register_event(event)


populate_eventregistry()
