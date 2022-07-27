from datetime import datetime

import pytest

from services import Restructure
from os.path import exists


@pytest.fixture
def restructure28():
    restructure = Restructure(file_path='data/28days.xlsx',
                              sheet_name='input_refresh_template',
                              out_path='data/output.xlsx')
    restructure.restructure_analytics_data()
    return restructure


def test_handle_28days_range(restructure28):
    assert restructure28.number_of_days == 28


def test_start_date28(restructure):
    assert restructure.start_date == datetime(2021, 1, 1)


def test_end_date28(restructure28):
    assert restructure28.end_date == datetime(2021, 1, 28)


@pytest.fixture
def restructure30():
    restructure = Restructure(file_path='data/30days.xlsx',
                              sheet_name='input_refresh_template',
                              out_path='data/output.xlsx')
    restructure.restructure_analytics_data()
    return restructure


def test_handle_30days_range(restructure30):
    assert restructure30.number_of_days == 30


def test_start_date30(restructure):
    assert restructure.start_date == datetime(2021, 1, 1)


def test_end_date30(restructure30):
    assert restructure30.end_date == datetime(2021, 1, 30)


@pytest.fixture
def restructure31():
    restructure = Restructure(file_path='data/31days.xlsx',
                              sheet_name='input_refresh_template',
                              out_path='data/output.xlsx')
    restructure.restructure_analytics_data()
    return restructure


def test_handle_31days_range(restructure31):
    assert restructure31.number_of_days == 31


def test_start_date31(restructure):
    assert restructure.start_date == datetime(2021, 1, 1)


def test_end_date31(restructure31):
    assert restructure31.end_date == datetime(2021, 1, 31)


def test_1site():
    restructure = Restructure(file_path='data/1site.xlsx',
                              sheet_name='input_refresh_template',
                              out_path='data/output_1site.xlsx')
    restructure.restructure_analytics_data()
    assert len(restructure.result['Site ID'].unique()) == 1


def test_5sites():
    restructure = Restructure(file_path='data/5sites.xlsx',
                              sheet_name='input_refresh_template',
                              out_path='data/output_5sites.xlsx')
    restructure.restructure_analytics_data()
    assert len(restructure.result['Site ID'].unique()) == 5


def test_100sites():
    restructure = Restructure(file_path='data/100sites.xlsx',
                              sheet_name='input_refresh_template',
                              out_path='data/output_100sites.xlsx')
    restructure.restructure_analytics_data()
    assert len(restructure.result['Site ID'].unique()) == 100


@pytest.fixture
def restructure():
    restructure = Restructure(file_path='data/Analytics Template for Exercise.xlsx',
                              sheet_name='input_refresh_template',
                              out_path='data/output.xlsx')
    restructure.restructure_analytics_data()
    return restructure


def test_page_views_no_missing_data(restructure):
    assert not restructure.result['Page Views'].isnull().values.any()


def test_unique_visitors_no_missing_data(restructure):
    assert not restructure.result['Unique Visitors'].isnull().values.any()


def test_total_time_spent_no_missing_data(restructure):
    assert not restructure.result['Total Time Spent'].isnull().values.any()


def test_visits_no_missing_data(restructure):
    assert not restructure.result['Visits'].isnull().values.any()


def test_avg_time_no_missing_data(restructure):
    assert not restructure.result['Average Time Spent on Site'].isnull().values.any()


def test_output_file_created(restructure):
    assert exists(restructure.out_path)


def test_start_date(restructure):
    assert restructure.start_date == datetime(2021, 1, 1)


def test_end_date(restructure):
    assert restructure.end_date == datetime(2021, 1, 31)
