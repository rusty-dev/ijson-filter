import simplejson as json


class ObjectWriter(object):
    def __init__(self, output):
        self.containers = [False]
        self.key = False
        self.output = output

    def _write(self, s):
        self.output.write(s)

    def event(self, event, value):
        if self.key:
            self.key = False
        elif not event.startswith('end') and self.containers[-1]:
            self._write(',')
        else:
            self.containers[-1] = True

        if event == 'map_key':
            self.key = True
            self._write(json.dumps(value))
            self._write(':')
        elif event == 'start_map':
            self.containers.append(False)
            self._write('{')
        elif event == 'start_array':
            self.containers.append(False)
            self._write('[')
        elif event == 'end_array':
            self.containers.pop()
            self._write(']')
        elif event == 'end_map':
            self.containers.pop()
            self._write('}')
        else:
            self._write(json.dumps(value))
