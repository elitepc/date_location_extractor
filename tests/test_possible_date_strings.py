import pytest
from datetime import datetime
from date_location_extractor import DateLocationExtractor

today = datetime.today()


@pytest.mark.parametrize(
    ("input_list", "expected_list_output"),
    [
        (["May 2009"],
         [{"address": "", "date_iso": "2009-05-{}".format(today.day), "ranking": 0.3,
           'normalized_address': {'City': '', 'Country': ''}}]),
        (["Portland United States of America, 03/05/2009"],
         [{"address": "Portland United States of America", "date_iso": "2009-03-05", "ranking": 0.5,
           'normalized_address': {'City': '', 'Country': ''}}]),
        (["Portland United States of America, May 2009"], [
            {"address": "Portland United States of America", "date_iso": "2009-05-{}".format(today.day),
             "ranking": 0.3,
             'normalized_address': {'City': '', 'Country': ''}}]),
    ],
)
def test_main_case_examples(input_list, expected_list_output):
    date_location_extractor = DateLocationExtractor()
    list_output = date_location_extractor.get_date_location_from_list(input_list)
    assert list_output[0] == expected_list_output[0]


@pytest.mark.parametrize(
    ("input_list", "expected_list_output"),
    [
        (["San Juan Costa Rica, 11/27/2009"],
         [{"address": "San Juan Costa Rica", "date_iso": "2009-11-27", "ranking": 1.0,
           'normalized_address': {'City': 'San Juan', 'Country': 'CR'}}]),
        (["Melbourne Australia, 09/20/2012"],
         [{"address": "Melbourne Australia", "date_iso": "2012-09-20", "ranking": 0.5,
           'normalized_address': {'City': '', 'Country': ''}}]),
        (["04/05/2014"], [{"address": "", "date_iso": "2014-04-05", "ranking": 0.5,
                           'normalized_address': {'City': '', 'Country': ''}}]),
        (["2003-05-31T00:00:00Z"], [{"address": "", "date_iso": "2003-05-31", "ranking": 0.5,
                                     'normalized_address': {'City': '', 'Country': ''}}]),
        (["23 March 2015"], [{"address": "", "date_iso": "2015-03-23", "ranking": 0.5,
                              'normalized_address': {'City': '', 'Country': ''}}]),
        (["12 September 2015"], [{"address": "", "date_iso": "2015-09-12", "ranking": 0.5,
                                  'normalized_address': {'City': '', 'Country': ''}}]),
        (["01/10/2008"], [{"address": "", "date_iso": "2008-01-10", "ranking": 0.5,
                           'normalized_address': {'City': '', 'Country': ''}}]),
        (["01 July 2016"], [{"address": "", "date_iso": "2016-07-01", "ranking": 0.5,
                             'normalized_address': {'City': '', 'Country': ''}}]),
        (["12 April 2015"], [{"address": "", "date_iso": "2015-04-12", "ranking": 0.5,
                              'normalized_address': {'City': '', 'Country': ''}}]),
        (["09 October 2015"], [{"address": "", "date_iso": "2015-10-09", "ranking": 0.5,
                                'normalized_address': {'City': '', 'Country': ''}}]),
        (["08/02/2014"], [{"address": "", "date_iso": "2014-08-02", "ranking": 0.5,
                           'normalized_address': {'City': '', 'Country': ''}}]),
        (["01/30/2011"], [{"address": "", "date_iso": "2011-01-30", "ranking": 0.5,
                           'normalized_address': {'City': '', 'Country': ''}}]),
        (["01 March 2015"], [{"address": "", "date_iso": "2015-03-01", "ranking": 0.5,
                              'normalized_address': {'City': '', 'Country': ''}}]),
        ([" Oberhausen"], [{"address": "Oberhausen", "date_iso": "", "ranking": 0.5,
                            'normalized_address': {'City': 'Oberhausen', 'Country': 'DE'}}])
    ],
)
def test_cases_from_unstructured_dataset(input_list, expected_list_output):
    date_location_extractor = DateLocationExtractor()
    list_output = date_location_extractor.get_date_location_from_list(input_list)
    assert list_output[0] == expected_list_output[0]


@pytest.mark.parametrize(
    ("input_list", "expected_list_output"),
    [
        ("not a list", "string_list should be a list"),
        ([1], "every element of string_list should be a string")
    ],
)
def test_exceptions(input_list, expected_list_output):
    date_location_extractor = DateLocationExtractor()
    with pytest.raises(TypeError) as excinfo:
        date_location_extractor.get_date_location_from_list(input_list)
    assert expected_list_output in str(excinfo.value)


@pytest.mark.parametrize(
    ("input_list", "expected_list_output"),
    [
        (["May 2009"],
         [{"address": "", "date_iso": "2009-05-{}".format(today.day), "ranking": 0.3,
           'normalized_address': {'City': '', 'Country': ''}}]),
        (["Portland United States of America, 03/05/2009"],
         [{"address": "Portland United States of America", "date_iso": "2009-03-05", "ranking": 0.5,
           'normalized_address': {'City': '', 'Country': ''}}]),
        (["Portland United States of America, May 2009"], [
            {"address": "Portland United States of America", "date_iso": "2009-05-{}".format(today.day),
             "ranking": 0.3,
             'normalized_address': {'City': '', 'Country': ''}}]),
    ],
)
def test_main_case_examples_parser(input_list, expected_list_output):
    date_location_extractor = DateLocationExtractor()
    list_output = date_location_extractor.get_date_location_from_list_with_parser(input_list)
    assert list_output[0] == expected_list_output[0]
