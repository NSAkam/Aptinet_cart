import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import "../Utiles"
import "../Components"
import KAST.Logic 1.0



Item {
    id:barcode_scanned

    property Logic obj_LogicContainerBarcodeScanned

    signal cancel()
    signal pass()
    Image {
        source: "../../Assets/StackBackground.png"
        anchors.fill: parent
    }

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
            text: obj_LogicContainerBarcodeScanned.lang.txt_Place_selected_item_in_cart
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
            text: obj_LogicContainerBarcodeScanned.lang.txt_Please_dont_move
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
            source: obj_LogicContainerBarcodeScanned.shopPage.newProduct.pic
            width: 135
            height: 135
            x:33
            y:33

        }
        Text {
            text: obj_LogicContainerBarcodeScanned.shopPage.newProduct.name
            x:232
            y:32
            font.pixelSize:24
        }
        Text {
            text: obj_LogicContainerBarcodeScanned.shopPage.newProduct.rate
            x:245
            y:145
            font.pixelSize: 18
        }
        Image {
            id:star1
            source: "../../Assets/star.png"
            x:275
            y:146
        }
        Image {
            id:star2
            source: "../../Assets/star.png"
            anchors.left: star1.right
            anchors.leftMargin: 7
            y:146
        }
        Image {
            id:star3
            source: "../../Assets/star.png"
            anchors.left: star2.right
            anchors.leftMargin: 7
            y:146
        }
        Image {
            id:star4
            source: "../../Assets/star.png"
            anchors.left: star3.right
            anchors.leftMargin: 7
            y:146
        }
        Image {
            id:star5
            source: "../../Assets/star.png"
            anchors.left: star4.right
            anchors.leftMargin: 7
            y:146
        }
        Text {
            text: obj_LogicContainerBarcodeScanned.shopPage.newProduct.savingQML
            x:539 - 40
            y:146
            font.pixelSize: 24
            color: "#36EB00"
        }
        Text {
            text: obj_LogicContainerBarcodeScanned.shopPage.newProduct.finalPriceQML
            x:599 - 40
            y:146
            font.pixelSize: 32
            color: "#F05A28"
        }
        Text {
            text: obj_LogicContainerBarcodeScanned.shopPage.newProduct.description
            color: "#1D1D1D"
            font.pixelSize: 16
            x: 232
            y: 70
            width: parent.width - x
            lineHeight: 1.5
            font.letterSpacing: 0.
            wrapMode: Text.WordWrap
        }
    }
    Text {
        text: obj_LogicContainerBarcodeScanned.lang.txt_You_have_seconds_to_put_the_item_in_the_cart
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
            text: obj_LogicContainerBarcodeScanned.lang.txt_Cancel
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
                    obj_LogicContainerBarcodeScanned.shopPage.cancel_newProductClicked()
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
                    timer1.running = false
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
        id:timer1
        interval: 1000
        onTriggered: {
            progress1.value += 0.14285
        }
        running: true
        repeat: true
    }
}
