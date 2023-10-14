from PySide2 import QtCore
from PySide2.QtCore import QObject, Signal, Property
from PySide2.QtSql import QSqlDatabase, QSqlQuery, QSqlRecord, QSqlTableModel
from tests.main_codes.dal import DAL
import unittest
from unittest.mock import MagicMock, Mock, patch


class TestDAL(unittest.TestCase):
    def setUp(self) -> None:
        pass

