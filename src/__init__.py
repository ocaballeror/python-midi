from .containers import Pattern, Track
from .fileio import read_midifile, write_midifile


def get_subclasses(base):
    subs = set(base.__subclasses__())
    recursive = set(e for a in subs for e in get_subclasses(a))
    subs.update(recursive)
    return subs


def populate_eventregistry():
    from .events import AbstractEvent, Event, MetaEvent, NoteEvent
    from .events import MetaEventWithText, EventRegistry
    events = get_subclasses(AbstractEvent).difference(
        {AbstractEvent, Event, MetaEvent, NoteEvent, MetaEventWithText}
    )
    for event in events:
        EventRegistry.register_event(event)


populate_eventregistry()
