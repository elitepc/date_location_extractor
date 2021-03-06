# Date Location Extractor

date_location_extractor is a date_location extractor that retrieves dates and locations found in a list of strings. The input can either be a json file with a list or you can use a list directly

## Install & Setup

Grab the package using `pip` (this will take a few minutes)
```bash
pip install date-location-extractor
```

Dater Location Extractor uses the following dependencies:
- datetime
- dateutil
- geotext
- datefinder
- ast
- os

## Basic Usage

Import the module, give some text or a URL, and presto.
```python
from date_location_extractor import DateLocationExtractor

date_location_extractor = DateLocationExtractor()
print(date_location_extractor.get_date_location_from_json_file("list_to_parse.json", use_simple_parser=True))
```

* `use_simple_parser` _does not use datefinder and uses the simple dateutil parser_

The result is a list of dictionaries, e.g:
```json
[{"address": "San Juan Costa Rica", "date_iso": "2009-11-27", "ranking": 1.0, "normalized_address": {"City": "San Juan", "Country": "CR"}}]
````
Without loading a file:
```python
from date_location_extractor import DateLocationExtractor

date_location_extractor = DateLocationExtractor()
print(date_location_extractor.get_date_location_from_list(["13 May 2009", "12/15/2010"]))
print(date_location_extractor.get_date_location_from_list_with_parser(["13 May 2009", "12/15/2010"]))
```

The ranking algorithm has the following weights set:

- RANKING_WEIGHT_HAS_DATE = 0.3
- RANKING_WEIGHT_HAS_DAY = 0.2
- RANKING_WEIGHT_HAS_COUNTRY = 0.3
- RANKING_WEIGHT_HAS_CITY = 0.2