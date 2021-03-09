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

---

Copyright &copy; 2018 Stitch
