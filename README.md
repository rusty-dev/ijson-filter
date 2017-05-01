## ijson-filter

Iterative JSON filtering tool based on [ijson](https://github.com/isagalaev/ijson).

Loading, filtering and output is performed without loading the whole file into memory, allowing filtering of large JSON files.

Build Status: [![Build Status](https://travis-ci.org/rusty-dev/ijson-filter.svg)](https://travis-ci.org/rusty-dev/ijson-filter)

#### Installation:

```bash
pip install ijson-filter
```

**ijson** is using **YAJL2** library for fast parsing, so it's highly recommended that you install it as well.
It will still work without **YAJL2**, but significantly slower.

#### Usage:
```
Usage: ijson-filter [OPTIONS] [INPUT]

  Streaming JSON filter.

Options:
  -o, --output FILENAME          Output filename, defaults to STDOUT.
  -f, --filter JSON_PATH_FILTER  Filter a JSON path, format:
                                 "PREFIX_PATH[=INT|~REGEX]" Examples: get last
                                 50 elements of data.rows - "data.rows=-50",
                                 get only data.rows and data.description keys
                                 - "data~(rows|description)"
  -v, --verbose                  Verbose output.
  --help                         Show this message and exit.
```


#### Examples:
*data.json*:
```json
{
	"name": "Primary data set #1",
    "table": {
    	"description": "Users",
        "rows": [
        	{ "name": "User1", ... },
            ...
        ]
    }
}
```


* Limit the number of items in __rows__ field to 50 last items, of *data.json* file and output to __STDOUT__:
```bash
$ ijson-filter -f "table.rows=-50" input.json
```

* Remove fields that contain a number in __table__ object (using regular expressions) of *data.json* and output to *filtered.json*:

```bash
$ ijson-filter -f 'table~[^\d]+' data.json -o filtered.json
```

* Filter output from unix commands and chain it to other commands *(limit array to first 3 objects)*:
```bash
$ echo '[1,2,3,4,5]' | ijson-filter -f 3 | python -m json.tool
[
    1,
    2,
    3
]
```
