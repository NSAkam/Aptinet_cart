import unittest
from downloader import Downloader
from unittest.mock import MagicMock, Mock, patch
from PySide2.QtCore import Signal,QEventLoop
from PySide2 import QtNetwork
from PySide2.QtNetwork import QNetworkReply


class TestUploader(unittest.TestCase):
    def setUp(self) -> None:
        self.downloader = Downloader()

    def test_setCurrentProgress_is_signal(self):
        self.assertIsInstance(self.downloader.setCurrentProgress, Signal)

    def test_succeeded_is_signal(self):
        self.assertIsInstance(self.downloader.succeeded, Signal)

    def test_downloadFinished(self):

        reply = Mock(spec=QNetworkReply)
        reply.readAll.return_value = b"Sample data"
        self.downloader.loop = QEventLoop()
        self.downloader.loop.quit = MagicMock()
        self.downloader.succeeded = MagicMock()
        self.downloader.downloadFinished(reply=reply)

        self.downloader.succeeded.emit.assert_called_once()
        self.assertTrue(self.downloader.succeeded.emit)

        self.downloader.loop.quit.assert_called_once()


    def test_progressbar_with_valid_input(self):
        self.downloader.progressbar(10, 20)
        self.assertTrue(self.downloader.setCurrentProgress.emit)

    def test_progressbar_with_invalid_input(self):
        self.downloader.progressbar(-10, -20)

    def test_run(self):
        manager = MagicMock(spec=QtNetwork.QNetworkAccessManager)
        reply = MagicMock(spec=QNetworkReply)
        manager.get.return_value = reply

        with patch('downloader.QEventLoop', spec=QEventLoop) as loop, \
                patch('downloader.QtNetwork.QNetworkAccessManager', return_value=manager), \
                patch('PySide2.QtNetwork.QNetworkAccessManager.finished') as finished:

            self.downloader.run()

        self.assertIsInstance(manager.get.return_value, QNetworkReply)
        loop.return_value.exec_.assert_called_once()
        manager.get.assert_called_once()
        reply.downloadProgress.connect.assert_called_with(self.downloader.progressbar)
        manager.finished.connect.assert_called_with(self.downloader.downloadFinished)
        manager.finished.connect.assert_called_once()
        reply.downloadProgress.connect.assert_called_with(self.downloader.progressbar)
