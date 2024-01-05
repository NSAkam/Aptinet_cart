import QtQuick 2.15
import QtQuick.Window 2.12
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0


ApplicationWindow {
    id:mainwindow
    width: 1280
    height: 800
    visible: true

    Image {
        id: background
        source: "/home/aptinet/Splash.png"
        anchors.fill: parent
    }
}