import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.12
import QtQuick.Window 2.14





Item {
    id: root
    visible: true
    width: 1280
    height: 800


    Image {     id: q
        source: "../../Assets/AuthenticationBackground.png"
        anchors.fill: parent
        opacity: 1
    }

    FastBlur {

        anchors.fill: q
        source: q
        radius: 70
    }

    Rectangle {
        width: 1280
        height: 92
        color: "#F05A28"
        x: 0
        y: 0

        Text {
            text: "Required Tips"
            color: "white"
            font.family: "Archivo"
            font.pixelSize: 32
            width: 228
            height: 36
            x: 526
            y: 28
            font.bold: true
        }

    }

    Rectangle {
        color: "white"
        width: 96
        height: 96
        radius: 4
        x: 170
        y: 224

        Image {
            source: "../../Assets/basket1.png"
            width: 48
            height: 48
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
        }
        Rectangle{
            id:rect1
            width:499
            height: parent.height
            anchors.left: parent.right
            anchors.leftMargin: -5
            color: "white"
            opacity: 0
            Text {
                text: qsTr("Make sure the cart is empty.")
                anchors.verticalCenter: parent.verticalCenter
                anchors.horizontalCenter: parent.horizontalCenter
                font.pixelSize: 32
            }
            Behavior on opacity{
                NumberAnimation{duration :500}
            }
        }
    }

    Rectangle {
        color: "white"
        width: 96
        height: 96
        radius: 4
        x: 170
        y: 352

        Image {
            source: "../../Assets/basket2.png"
            width: 48
            height: 48
            x: 24
            y: 24
        }
        Rectangle{
            id:rect2
            width:845
            height: parent.height
            anchors.left: parent.right
            anchors.leftMargin: -5
            color: "white"
            opacity: 0
            Text {
                text: qsTr("Don’t move the cart when add or remove products.")
                anchors.verticalCenter: parent.verticalCenter
                anchors.horizontalCenter: parent.horizontalCenter
                font.pixelSize: 32
            }
            Behavior on opacity{
                NumberAnimation{duration :1500}
            }
        }
    }

    Rectangle {
        color: "white"
        width: 96
        height: 96
        radius: 4
        x: 170
        y: 480

        Image {
            source: "../../Assets/basket3.png"
            width: 48
            height: 48
            x: 24
            y: 24
        }
    }

    Timer{
        running: true
        interval: 3000
        repeat: true
        onTriggered: {
            if(rect1.opacity === 0)
            {
                rect1.opacity = 1
            }
            else if(rect1.opacity === 1 && rect2.opacity === 0)
            {
                rect2.opacity = 1
            }
        }
    }
}




