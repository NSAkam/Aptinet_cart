from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtQml import QQmlApplicationEngine,qmlRegisterType,QQmlDebuggingEnabler
from translator import QMLLanguageManager
import sys


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    app.setOverrideCursor(Qt.BlankCursor)
    qmlRegisterType(QMLLanguageManager, "QMLLanguageManager.binding", 1, 0, "QMLLanguageManager")
    
    engine = QQmlApplicationEngine()


    ctx = engine.rootContext()
    qml_file = "views/main.qml"
    engine.load(str(qml_file))
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
