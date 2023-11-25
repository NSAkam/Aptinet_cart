import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import "../Utiles"
import "../Components"
//import KAST.Logic 1.0



Item {
    id:barcode_scanned

    signal cancel()
    signal pass()

    property QtObject tanzimat

    anchors.fill: parent
    ViewSettings{
        id:viewset
    }

    Rectangle{
        id:rect_move
        color: "#4696FA"
        x:32
        y:125
        width: 826
        height: 72
        radius: 4
        visible: true
        Text {
            text: qsTr("Place selected item in cart")
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            color: "white"
            font.pixelSize: 24
            font.bold: true
        }
    }

    Rectangle{
        id:rect_dontmove
        color: "#F05A28"
        x:32
        y:125
        width: 826
        height: 72
        radius: 4
        visible: false
        Text {
            text: qsTr("Please don’t move !")
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            color: "white"
            font.pixelSize: 24
            font.bold: true
            Image {
                source: "../../Assets/Warning.png"
                anchors.right: parent.left
                anchors.verticalCenter: parent.verticalCenter
                anchors.rightMargin: 10
            }
        }
    }
    Rectangle{
        x:32
        y:221
        width: 826
        height: 200
        color: "White"
        Image {
            source: "../../Assets/product.png"
            width: 135
            height: 135
            x:33
            y:33

        }
        Text {
            text: qsTr("Nutella Hazelnut Spread with Cocoa, 750g")
            x:232
            y:32
            font.pixelSize:24
        }
        Text {
            text: qsTr("-9%")
            x:639
            y:146
            font.pixelSize: 24
            color: "#F08C5A"
        }
        Text {
            text: qsTr("$ 9.99")
            x:699
            y:146
            font.pixelSize: 32
            color: "#F05A28"
        }
        Text {
            text: qsTr("The original hazelnut and cocoa spread that has been on the breakfast \ntables of millions worldwide.")
            color: "#1D1D1D"
            font.pixelSize: 16
            x: 232
            y: 70
            lineHeight: 1.5
            font.letterSpacing: 0.64
        }
    }
    Text {
        text: qsTr("You have 7 seconds to put the item in the cart..")
        x:216
        y:481
        font.pixelSize: 20
        color: "#6D6D6D"
    }

    Button {
        x: 694
        y: 469
        width: 164
        height: 46
        background:
            Rectangle {
            anchors.fill: parent
            color: "transparent"
            border.color: viewset.primaryColor
            border.width: 1
            radius: 4
        }

        Text {
            text: qsTr("Cancel")
            font.pixelSize: 20
            lineHeight: Font.Normal
            font.letterSpacing: 1.28
            color: "#F08C5A"
            x: 48
            y: 12
            horizontalAlignment: Text.AlignHCenter
            MouseArea{
                anchors.fill: parent
                onClicked: {
                    barcode_scanned.cancel()
                }
            }
        }
    }


    CircularProgressBar {
        id: progress1
        lineWidth: 10
        x: 678 + 50
        y: 496 + 50
        value: 0.0
        size: 150
        secondaryColor: "#e0e0e0"
        primaryColor: "#F08C5A"

        Text {
            text: parseInt((progress1.value * 100) / 14)
            anchors.centerIn: parent
            font.pointSize: 20
            color: progress1.primaryColor
            onTextChanged: {
                if(text == "8"){
                    barcode_scanned.pass()
                }
                if(text =="5")
                {
                    rect_move.visible = false
                    rect_dontmove.visible = true
                }
            }
        }
    }
    Timer{
        interval: 1000
        onTriggered: {
            progress1.value += 0.14285
        }
        running: true
        repeat: true
    }
}
