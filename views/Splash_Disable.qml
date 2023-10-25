import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.12
import QtGraphicalEffects 1.12

Item {
    id: root

    anchors.fill: parent


    property alias taptostartbtn: taptostartbutton

    Image {
        id: bg
        source: "Resources/BG.png"
        anchors.fill: root

        Rectangle {
            color: Qt.rgba(0, 0, 0, 0.75)
            anchors.fill: bg
        }

    }

    FastBlur {
        id: bgblur
        anchors.fill: bg
        source: bg
        radius: 100
    }

    Image {
        id: logo
        source: "Resources/start_logo.png"
        x: 381
        y: 256
        width: 518
        height: 240.16
    }


    Button {
        id: taptostartbutton
        width: 374
        height: 179
        x: 906
        y: 621

        background:
            Rectangle {
            color: "transparent"
        }

        Text {
            id: taptostarttext
            text: qsTr("Tap to start")
            x: 86
            y: 72
            color: Qt.rgba(245, 175, 140, 0.2)
            font.family: "Archivo"
            font.pixelSize: 32
            font.weight: Font.Bold
            font.letterSpacing: 0.04 * 32
            horizontalAlignment: Text.AlignLeft
        }

        Image {
            id: arrow
            source: "Resources/arrow_taptostart.png"
            width: 11
            height: 18
            x: 299
            y: 88
        }
    }



}

