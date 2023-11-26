import sys
from PySide2.QtCore import Qt 
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine,qmlRegisterType,QQmlDebuggingEnabler
# from Services.battery import BatteryWorker
from logic import Logic


if __name__ == "__main__":
    # debug = QQmlDebuggingEnabler()
    app = QGuiApplication(sys.argv)
    app.setOverrideCursor(Qt.BlankCursor)
    qmlRegisterType(Logic, "KAST.Logic" , 1, 0 ,"Logic")
    
    engine = QQmlApplicationEngine()

    ctx = engine.rootContext()
    qml_file = "../views/Main.qml"
    engine.load(str(qml_file))
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())


    # PySide2.QtCore.QCoreApplication.instance()
    # os.execl(sys.executable, sys.executable, *sys.argv)
    # print(status)