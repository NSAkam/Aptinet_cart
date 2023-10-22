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
        color: "#F05A28"
        x:32
        y:125
        width: 826
        height: 72
        radius: 4
        Text {
            text: qsTr("Please don’t move !")
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            color: "white"
            font.pixelSize: 24
            Image {
                source: "file://../Assets/Warning.png"
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
            source: "file://../Assets/Product.png"
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
    }
    Text {
        text: qsTr("You have 7 seconds to put the item in the cart..")
        x:216
        y:481
        font.pixelSize: 20
        color: "#6D6D6D"
    }
    KButton{
        text: "Cancel"
        btn_color: "transform"

    }

}
