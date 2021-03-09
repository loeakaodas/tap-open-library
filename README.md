# tap-open-library

This is a [Singer](https://singer.io) tap that produces JSON-formatted data
following the [Singer
spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

This tap:

- Pulls raw data from [Open Library](https://openlibrary.org/developers/api)
- Extracts the following resources:
  - [Recent Changes](https://openlibrary.org/dev/docs/api/recentchanges)
- Outputs the schema for each resource
- Incrementally pulls data based on the input state

## Usage

Git clone the repo:

```bash
$ git clone https://github.com/loeakaodas/tap-open-library.git
```

Create and activate a virtual environment for the tap:

```bash
$ cd tap-open-library
$ python3 -m venv ~/.virtualenvs/tap-open-library
$ source ~/.virtualenvs/tap-open-library/bin/activate
```

Install the package:

```bash
(tap-open-library) $ pip install -e .
```

Run the tap in `discovery` mode:

```bash
$ tap-open-library --config sameple_config.json --discover
```

Alternatively the output of `discovery` mode can be saved for use in `sync` mode:

```bash
$ tap-open-library --config sameple_config.json --discover > new_catalog.json
```

To run the tap in `sync` mode use the included `sample_config.json` and `catalog.json` file:

```bash
$ tap-open-library --config sameple_config.json --catalog catalog.json
```

---

Copyright &copy; 2018 Stitch
