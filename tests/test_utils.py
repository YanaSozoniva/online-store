from unittest.mock import patch
from src.utils import read_json, create_objects_json

import pytest

@pytest.fixture
def path_json():
    return r'C:\Users\user\Desktop\skyPro\online store\data\products.json'


@patch("src.utils.json.load")
def test_read_json(mock_reader, path_json, json_data):
    """Тестирует успешное открытие файла"""
    mock_reader.return_value = json_data
    result = read_json(path_json)
    assert result == json_data
    mock_reader.assert_called_once()


@patch("src.utils.json.load")
def test_read_json_zero(mock_reader, path_json):
    """Тестирует пустой файл"""
    mock_reader.return_value = []
    result = read_json(path_json)
    assert result == []
    mock_reader.assert_called_once()


def test_read_json_not_found_file():
    """Тестирует, если файл не найден"""
    path_file = ""
    assert read_json(path_file) == "Файл не найден"


def test_create_objects_json(json_data):
    """Тестирования успешного преобразования в класс"""

    result = create_objects_json(json_data)
    assert result[0].name == 'Смартфоны'
    assert result[0].count_products == 5
    assert result[0].products[0]
