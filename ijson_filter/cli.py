import warnings
try:
    import ijson.backends.yajl2_cffi as ijson
except Exception:
    import ijson
    warnings.warn("YAJL2 library not available, using a slower pure python implementation.")
import time
import click
import logging
import re
from ijson_filter.object_writer import ObjectWriter
from ijson_filter.event_filter import JsonEventFilter


def json_path_filter(arg):
    """Parse a JSON filter argument."""
    key, sep, value = arg.strip().partition('~')
    if sep == '~':
        return key, re.compile(value)

    key, sep, value = arg.strip().rpartition('=')
    return key, int(value)


def do_filter(input_file, output_file, filters, verbose):
    logging.basicConfig(level=logging.INFO if verbose else logging.WARNING)
    logger = logging.getLogger('JSON-FILTER')
    json_filter = JsonEventFilter(ijson.parse(input_file), filters)
    writer = ObjectWriter(output_file)
    start_time = time.time()
    for prefix, event, value in json_filter:
        logger.info('%s(%s): %s' % (prefix, event.upper(), value))
        writer.event(event, value)
    logger.info('Finished in: %s seconds.' % (time.time() - start_time))


@click.command()
@click.argument('input', type=click.File('rb'), default='-')
@click.option('--output', '-o', type=click.File('wb'), default='-', help='Output filename, defaults to STDOUT.')
@click.option(
    '--filter', '-f', multiple=True, type=json_path_filter,
    help=(
        'Filter a JSON path, format: "PREFIX_PATH[=INT|~REGEX]" '
        'Examples: get last 50 elements of data.rows - "data.rows=-50", '
        'get only data.rows and data.description keys - "data~(rows|description)"'
    )
)
@click.option('--verbose', '-v', help='Verbose output.', is_flag=True)
def main(input, output, filter, verbose):
    """Iterative JSON filter."""
    do_filter(input, output, dict(filter), verbose)


if __name__ == '__main__':
    main()
