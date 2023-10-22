import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import QtQuick.Window 2.0
import QtQuick.Controls.Styles 1.4
import QtGraphicalEffects 1.0
import "Components"
import "Containers"
import "Utiles" as Util

Item {

    width: 1280
    height: 800

    Util.ViewSettings{
        id:viewset
    }

    Image {
        source: "../Assets/AuthenticationBackground.png"
        anchors.fill: parent
    }

    Rectangle {
        color: "#A37A544D"
        anchors.fill: parent
        opacity: 0.3
    }

    Rectangle{
        width: parent.width
        height: 92
        x:0
        y:0
    }

    Item{
        id:top_Panel
        width: parent.width
        height: 92
        Rectangle{
            width: parent.width
            height: parent.height
            x:0
            y:0
            Rectangle{
                width: 50
                height: 50
                color: viewset.primaryColor
                x:421
                y:25
                radius: width /2
            }
            Text {
                text: qsTr("user Email")
                color: "#6D6D6D"
                width: 148
                height: 15
                font.pixelSize: 14
                x:478
                y:40
            }
            Image {
                source: "../Assets/Help.png"
                width: 57
                height: 57
                x:1156
                y:25
            }
            Image {
                source: "../Assets/Notification.png"
                width: 57
                height: 57
                x:1208
                y:25
            }

        }
    }

    Item{
        id:leftPanel
        width: 390
        height: parent.height

        Rectangle {
            id:rect_leftPanel
            color: "white"
            anchors.fill: parent
            width: 390
            height: 800
            x: 0
            y: 0

        }

//        DropShadow {
//            anchors.fill: rect_leftPanel
//            horizontalOffset: 8
//            verticalOffset: 0
//            radius: 1
//            samples: 1
//            color: Qt.rgba(0, 0, 0, 0.04)
//        }

        Image {
            source: "../Assets/AptinetText.png"
            x:0
            y:0
        }
        Image {
            id: img_UserCaptured
            source: "../Assets/UserImage.png"
            width: 326
            height: 184
            x:32
            y:105
        }

        Text {
            id: mycarttext
            text: qsTr("My Cart")
            font.pixelSize: 24
            font.bold: true
            x: 32
            y: 330
            color: "gray"
        }

        Rectangle {
            id: quantitycircle
            width: 40
            height: 40
            radius: width
            color: viewset.secondaryColor
            x: 145
            y: 326

            Text {
                id: quantitytext
                text: qsTr("14")
                font.pixelSize: 20
                color: "white"
                anchors.centerIn: parent
                font.bold: true
            }
        }

    }

    Item {
        id:main_Panel

        StackView
        {
            id:stackviewContainer
            width: 890
            height: 708
            x:390
            y:92
            initialItem:checkout
            onDepthChanged: {
//                obj_LogicContainer.shoppage.stackviewDepthChanged(stackviewContainer.depth)
            }
        }
    }

    Component {
        id: checkout
        Checkoutpage {

        }
    }

}
