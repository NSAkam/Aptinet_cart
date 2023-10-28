import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.12
import QtGraphicalEffects 1.12
import "../Components"

Item {

    property alias imagesource: pic.source
    property alias textcontent: txt.text


    Rectangle {
        id: mainrect
        width: 96
        height: 96
        color: "white"
        radius: 4

        Image {
            id: pic
            source: "../../Assets/blankbasket.png"
            anchors.centerIn: parent
        }

        DropShadow {
            anchors.fill: parent
            cached: true
            horizontalOffset: 0
            verticalOffset: 8
            radius: 16.0
            y: 5
            samples: 30
            color: "#0000000A"
            smooth: true
            source: parent
            visible: shadow?true:false

        }

    }

    Rectangle {
        id: textrect
        height: mainrect.height
        width: 500 + txt.width/6
        x: parent.width + 96
        y: parent.y
        color: /*Qt.rgba(255, 255, 255, 0.7)*/ "red"
        opacity: 0.1
        Behavior on width{
            NumberAnimation{
                duration: 10000
            }
        }

        Text {
            id: txt
            text: qsTr("Required Tips")
            font.pixelSize: 32
            font.weight: Font.DemiBold
            lineHeight: Font.Normal
            font.letterSpacing: 1.28
            color: "#6D6D6D"
            anchors.horizontalCenter: parent.horizontalCenter
            horizontalAlignment: Text.AlignHCenter
            y: 30
            MouseArea {
                anchors.fill: parent
                onClicked: {
                    textrect.opacity = 1
                }
            }
//            x: 32
//            anchors.verticalCenter: parent.verticalCenter
//            anchors.centerIn: parent
        }

    }

//    Timer {
//        id: timer
//        running: true
//        triggeredOnStart: true
//        onTriggered: textrect.opacity = 1
//    }

}
