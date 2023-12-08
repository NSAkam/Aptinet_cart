import sys
from PySide2.QtCore import Qt 
from PySide2.QtGui import QGuiApplication,QFontDatabase,QFont
from PySide2.QtQml import QQmlApplicationEngine,qmlRegisterType,QQmlDebuggingEnabler

from logic import Logic
from Services.camera import CameraWorker
from Helpers.cameraHelper import CameraHelper



if __name__ == "__main__":
    # debug = QQmlDebuggingEnabler()
    app = QGuiApplication(sys.argv)
    app.setOverrideCursor(Qt.BlankCursor)

    id = QFontDatabase.addApplicationFont("../Assets/Archivo/Archivo-Regular.ttf")
    app.setFont(QFont(QFontDatabase.applicationFontFamilies(id)[0]))
    
    qmlRegisterType(Logic, "KAST.Logic" , 1, 0 ,"Logic")
    
    engine = QQmlApplicationEngine()



    cworker = CameraWorker()
    engine.rootContext().setContextProperty("cameraProvider",cworker)
    camera = CameraHelper(cworker)
    engine.addImageProvider("KCameraProvider", camera)
    cworker.start()


    ctx = engine.rootContext()
    
    qml_file = "../views/main.qml"
    engine.load(str(qml_file))
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())


    # PySide2.QtCore.QCoreApplication.instance()
    # os.execl(sys.executable, sys.executable, *sys.argv)
    # print(status)