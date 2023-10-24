import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import QtQuick.Window 2.0
import "../Components"
import "../Containers"
import "../Utiles"

Popup {
    property alias notiftext: notiftext.text

    id: root
    width: 1280
    height: 800
    modal: true
    focus: true

    background:
        Rectangle {
        color: "black"
        opacity: 0.4
        x: 0
        y: 0
        width: parent.width
        height: parent.height
    }

    Rectangle {
        x: 818 + 390
        y: 32
        radius: 4
        color: "white"
        width: 40
        height: 40

        Image {
            source: "../../Assets/alarm.png"
            width: 18
            height: 20
            anchors.centerIn: parent
        }
    }

    Rectangle {
        id: notifrect
        width: 678 + notiftext.width/6
        height: 252
        radius: 4
        y: 274
//        x: 106 + 390/2
        anchors.horizontalCenter: parent.horizontalCenter

        Image {
            source: "../../Assets/popupwarning.png"
            width: 99
            height: 88
            y: 48
            anchors.horizontalCenter: parent.horizontalCenter
        }

        Text {
            id: notiftext
            text: qsTr("Please put the product you scanned into the cart!")
            anchors.horizontalCenter: parent.horizontalCenter
            horizontalAlignment: Text.AlignHCenter
            y: 168
            color: "black"
            font.pixelSize: 24
            font.weight: Font.DemiBold
//            font.letterSpacing: 0.8
        }
    }

}
