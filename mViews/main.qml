import QtQuick 2.15
import QtQuick.Window 2.12
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0



Window {
    id:mainwindow
    width: 1280
    height: 800
    visible: true
    color: "white"

    property alias stackview: stackview

    StackView
    {
        id:stackview
        anchors.fill: parent
        initialItem: "Setting.qml"
    }
}