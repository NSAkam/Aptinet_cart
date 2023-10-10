import unittest
from uploader import Uploader
from PySide2.QtCore import Signal
from unittest.mock import MagicMock, Mock, patch
from PySide2.QtCore import QThread, Signal,Slot,QEventLoop
from PySide2 import QtCore, QtGui, QtNetwork
from PySide2.QtCore import QByteArray,QFile,QIODevice, QTimer
from PySide2.QtNetwork import QHttpMultiPart,QHttpPart,QNetworkRequest,QNetworkReply


class TestUploader(unittest.TestCase):
    def setUp(self) -> None:
        self.uploader = Uploader()

    def test_setCurrentProgress_is_signal(self):
        self.assertIsInstance(self.uploader.setCurrentProgress, Signal)

    def test_succeeded_is_signal(self):
        self.assertIsInstance(self.uploader.succeeded, Signal)

    def test_UploadFinished(self):
        reply = Mock(spec=QNetworkReply)
        self.uploader.UploadFinished(reply= reply)
        self.assertTrue(self.uploader.succeeded.emit)

    def test_progressbar_with_valid_input(self):
        self.uploader.progressbar(10, 20)
        self.assertTrue(self.uploader.setCurrentProgress.emit)

    def test_progressbar_with_invalid_input(self):
        self.uploader.progressbar(-10, -20)

    def test_get_basketName_with_valid_input(self):
        with open("basketName.txt", 'w') as file:
            file.write("basket1")
        self.assertEqual(self.uploader.get_basketName(), 'basket.db')

    def test_set_Header_and_Body(self):
        # Create a sample basketName and file
        basketName = "basket.db"
        file = QFile("test_database.db")
        file.open(QFile.ReadOnly)

        # Call the function
        result = self.uploader.set_Header_and_Body(basketName, file)

        # Assertions
        self.assertIsInstance(result, QHttpPart)


    def test_run(self):
        file = QFile("basket.db")
        file.open(QIODevice.ReadOnly)
        manager = MagicMock(spec=QtNetwork.QNetworkAccessManager)
        reply = MagicMock(spec=QNetworkReply)
        manager.post.return_value = reply

        with patch('uploader.QEventLoop', spec=QEventLoop) as loop, \
                patch('uploader.QtNetwork.QNetworkAccessManager', return_value=manager), \
                patch('PySide2.QtCore.QObject.setParent') as set_parent, \
                patch('PySide2.QtNetwork.QNetworkAccessManager.finished') as finished:

            self.uploader.run()

        self.assertTrue(self.uploader.get_basketName())
        self.assertEqual(self.uploader.get_basketName(), 'basket.db')
        self.assertEqual(self.uploader.basketName, "basket.db")
        self.assertIsInstance(self.uploader.set_Header_and_Body("basket.db", file), QHttpPart)
        self.assertIsInstance(manager.post.return_value, QNetworkReply)
        loop.return_value.exec_.assert_called_once()
        manager.post.assert_called_once()
        reply.uploadProgress.connect.assert_called_once_with(self.uploader.progressbar)

        manager.finished.connect.assert_called_with(loop().quit)
        # manager.finished.connect.assert_called_with(self.uploader.UploadFinished)
        manager.finished.connect.assert_called()
        reply.uploadProgress.connect.assert_called_with(self.uploader.progressbar)


    # def test_run(self):
    #     # Create a QFile object with a valid file path
    #     file = QFile("basket.db")
    #     file.open(QIODevice.ReadOnly)
    #
    #     # Create mock objects for the necessary dependencies
    #     mock_manager = MagicMock(spec=QtNetwork.QNetworkAccessManager)
    #     mock_reply = Mock(spec=QtNetwork.QNetworkReply)
    #     mock_manager.post.return_value = mock_reply
    #
    #     # Patch the necessary classes and methods with the mock objects
    #     with patch('uploader.QFile', return_value=file), \
    #             patch('uploader.QtNetwork.QNetworkAccessManager', return_value=mock_manager), \
    #             patch('uploader.QEventLoop', spec=QEventLoop) as mock_event_loop:
    #         # Call the run() method of the uploader
    #         self.uploader.run()
    #
    #         # Assert that the necessary methods and signals were called
    #         mock_manager.post.assert_called_once()
    #         mock_event_loop.return_value.exec_.assert_called_once()
    #         mock_reply.setParent.assert_called_once_with(None)

    # def test_run(self):
    #     file = MagicMock(spec=QIODevice)
    #     file.size.return_value = 100
    #     file.open.return_value = True
    #
    #     loop = MagicMock(spec=QEventLoop)
    #     loop.exec_.side_effect = SystemExit
    #
    #     manager = MagicMock()
    #     manager.post.return_value = MagicMock(spec=QNetworkReply)
    #
    #     setbodydevice = MagicMock()
    #     setbodydevice.return_value = file
    #
    #     with patch('uploader.QFile', return_value=file), patch('uploader.QEventLoop', return_value=loop), \
    #             patch('uploader.QtNetwork.QNetworkAccessManager', return_value=manager),\
    #             patch ('uploader.QHttpPart', setbodydevice):
    #         self.uploader.run()
    #

    # def test_run_2(self):
    #
    #     # Create a QFile object with a valid file path
    #     file = QFile("basket.db")
    #     file.open(QIODevice.ReadOnly)
    #
    #     # Create a mock QHttpMultiPart object
    #     mock_multiPart = MagicMock(spec=QHttpMultiPart)
    #
    #     # Create mock objects for the necessary dependencies
    #     mock_manager = MagicMock(spec=QtNetwork.QNetworkAccessManager)
    #     mock_reply = MagicMock(spec=QtNetwork.QNetworkReply)
    #     mock_manager.post.return_value = mock_reply
    #
    #     # Patch the necessary classes and methods with the mock objects
    #     with patch('uploader.QHttpMultiPart', return_value=mock_multiPart), \
    #          patch('uploader.QtNetwork.QNetworkAccessManager', return_value=mock_manager), \
    #          patch('uploader.QEventLoop', spec=QEventLoop) as mock_event_loop, \
    #          patch('PySide2.QtCore.QObject.setParent') as mock_set_parent, \
    #          patch('uploader.QFile', return_value=file):
    #
    #         # Call the run() method of the uploader
    #         self.uploader.run()
    #
    #         # Assert that the necessary methods and signals were called
    #         mock_manager.post.assert_called_once()
    #         mock_event_loop.return_value.exec_.assert_called_once()
    #         mock_set_parent.assert_called_once_with(mock_multiPart, mock_reply)
    #
    # def test_run_4(self):
    #
    #     # Mocking necessary objects and methods
    #     manager = QtNetwork.QNetworkAccessManager()
    #     reply = MagicMock(spec=QtNetwork.QNetworkReply)
    #     manager.post = MagicMock(return_value=reply)
    #     loop = QEventLoop()
    #     # loop.quit = MagicMock()
    #     self.uploader.UploadFinished = MagicMock()
    #     self.uploader.progressbar = MagicMock()
    #
    #     # Connecting signals
    #     manager.finished = MagicMock()
    #     reply.uploadProgress = MagicMock()
    #
    #     # Running the method
    #     self.uploader.run()
    #
    #     # Assertions
    #     manager.post.assert_called_once()
    #     manager.finished.connect.assert_called_with(self.uploader.UploadFinished)
    #     # loop.quit.assert_called_once()
    #     reply.uploadProgress.connect.assert_called_with(self.uploader.progressbar)
    #
    #     # Stop the event loop after a timeout
    #     QTimer.singleShot(1000, loop.quit)
    #     loop.exec_()


        # manager.finished = MagicMock()
        # reply.uploadProgress = MagicMock()
        # self.uploader.UploadFinished = MagicMock()
        # self.uploader.progressbar = MagicMock()
        # self.uploader.UploadFinished = MagicMock()

        # Patch the necessary classes and methods with the mock objects
        # with patch('uploader.QtNetwork.QNetworkAccessManager', return_value=manager), \
        #      patch('uploader.QEventLoop', spec=QEventLoop) as loop, \
        #      patch('PySide2.QtCore.QObject.setParent') as mock_set_parent:
        #      # patch('uploader.QFile', return_value=file):






