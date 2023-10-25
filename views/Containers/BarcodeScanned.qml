import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import "../Utiles"
import "../Components"
//import KAST.Logic 1.0



Item {
    id:barcode_scanned

    property QtObject tanzimat

    anchors.fill: parent
    ViewSettings{
        id:viewset
    }

    Rectangle{
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
            source: "../../Assets/Product.png"
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
//    KBorderButton{
//        text: "Cancel"
//        btn_color: "transparent"
//        color: "transparent"
//        x: 694
//        y: 469
//        width: 164
//        height: 46
//    }

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
//            font.weight: Font.DemiBold
            lineHeight: Font.Normal
            font.letterSpacing: 1.28
            color: "#F08C5A"
//            anchors.horizontalCenter: parent.horizontalCenter
            x: 48
            y: 12
            horizontalAlignment: Text.AlignHCenter
        }
    }

    KProgress {
        value: 3
        x: 778 - 30
        y: 596 - 30
        height: 140
        from: 0
        to: 7
        reverse: true
        titleFontSize: 10
//        lineWidth: 50
        fontSize: 10
        fromAngle: (Math.PI / 180) * 270
        toAngle: (Math.PI / 180) * 270 + 360
        kprogressBackgroundColor: "white"
        kprogressColor: "#F08C5A"
        title: parseInt(value)
    }

}
