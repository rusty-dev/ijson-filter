from itertools import count, chain
import collections

# python2-3 compatible xrange
try:
    xrange
except NameError:
    xrange = range


class ContainerEnd(Exception):
    """Raised when item consumption reaches the end of a container."""
    pass


def consume_item(events):
    """Consume and yield events from a single item in JSON stream."""
    try:
        prefix, event, value = item = next(events)
        end_event = None
        end_prefix = prefix
        yield item
        if event.startswith('start_'):
            end_event = event.replace('start', 'end')
        elif event.startswith('end_'):
            raise ContainerEnd()
        elif event == 'map_key':
            for map_value in consume_item(events):
                yield map_value
            raise StopIteration()
        else:
            raise StopIteration()

        while (prefix, event) != (end_prefix, end_event):
            prefix, event, value = item = next(events)
            yield item
    except StopIteration:
        pass


def consume_items(events, limit=20):
    """Consume a whole array and yield a limited amount of events from it."""
    start_prefix, start_event, start_value = next(events)
    end_prefix = start_prefix
    end_event = start_event.replace('start', 'end')

    reverse = limit < 0
    limit = abs(limit)

    rows = collections.deque(maxlen=limit)
    if reverse:
        boundary = count()
    else:
        boundary = xrange(limit)

    try:
        for i in boundary:
            rows.append(list(consume_item(events)))
        # consume the rest of the container if there's anything left.
        while True:
            for event in consume_item(events):
                pass
    except ContainerEnd:
        pass

    # yield a container start event.
    yield start_prefix, start_event, None

    for item in rows:
        for event in item:
            yield event

    # yield a container end event.
    yield end_prefix, end_event, None


class JsonEventFilter(object):
    def __init__(self, events, filters=None):
        self.events = events
        self.filters = filters if filters else {}

    def __iter__(self):
        return self.iter(self.events, self.filters)

    def iter(self, events, filters):
        while True:
            prefix, event, value = item = next(events)
            if prefix in filters:
                if event == 'start_array':
                    new_filters = dict(filters)
                    n = new_filters.pop(prefix)
                    for item in self.iter(consume_items(chain((item,), events), n), new_filters):
                        yield item
                elif event == 'map_key':
                    if not filters[prefix].match(value):
                        self.discard(consume_item(chain((item,), events)))
                    else:
                        yield item
                else:
                    yield item
            else:
                yield item

    def discard(self, iterator):
        collections.deque(iterator, 0)
