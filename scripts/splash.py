import sys
from PySide2.QtCore import Qt 
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine



if __name__ == "__main__":
    #QGuiApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

    app = QGuiApplication(sys.argv)
    app.setOverrideCursor(Qt.BlankCursor)

    engine = QQmlApplicationEngine()

    ctx = engine.rootContext()
    
    qml_file = "../views/sp.qml"
    # qml_file = "../views/test.qml"
    engine.load(str(qml_file))
    sys.exit()
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())


    # PySide2.QtCore.QCoreApplication.instance()
    # os.execl(sys.executable, sys.executable, *sys.argv)
    # print(status)