import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import "../Utiles"
import "../Components"
//import KAST.Logic 1.0

Item {
    id:manualBarcode_Panel
    ViewSettings{
        id:viewset
    }

    signal cancle();
    signal ok();
    property bool showlastproduct: false


    property QtObject tanzimat

    anchors.fill: parent

    Component.onCompleted: {
        txt_ManualBarcodeInput.forceActiveFocus()
        numpad.inputtext = txt_ManualBarcodeInput

    }

    Rectangle
    {
        id:rect1
        x:126
        y:96
        width: 639
        height: 72
        radius: 4
        color: "#F05A28"
        Label{
            text: "Please enter the item barcode"
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            font.bold: true
            font.pixelSize: 24
            color: "white"
        }
    }

    Rectangle{
        x:126
        y:188
        color: "White"
        width: 276
        height: 340
        radius: 4
        Numpad {
            id:numpad
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
        }
    }

    Rectangle{
        x:422
        y:188
        color: "White"
        width: 343
        height: 340
        Image {
            source: "file://../Assets/Union.png"
            anchors.horizontalCenter: parent.horizontalCenter
            y:24
        }
        Rectangle{
            x:24
            y:112
            width: 295
            height: 56
            color: "#F1F1F1"
            radius: 4
            TextInput{
                id:txt_ManualBarcodeInput
                anchors.fill: parent
                font.pixelSize: 18
                layer.enabled: true
                horizontalAlignment: TextInput.AlignHCenter
                verticalAlignment:  TextInput.AlignVCenter
                font.family: viewset.danaFuNumFont
                property string placeholderText: " "

                onFocusChanged: {
                    numpad.inputtext = txt_ManualBarcodeInput
                }
                Text {
                    text: txt_ManualBarcodeInput.placeholderText
                    color: "#C6C5CE"
                    visible: !txt_ManualBarcodeInput.text
                    font.pixelSize: 18
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    font.family: viewset.danaFuNumFont
                }
            }
        }
        KButton{
            ishover: false
            btn_color: viewset.secondaryColor
            text: "Confirm >"
            x:24
            y:192
            borderRadius: 4
            btn_borderWidth: 0
            onClicked: {
                tanzimat.shoppage.insertManualBarcodeClicked(txt_ManualBarcodeInput.text)
                manualBarcode_Panel.ok()

            }
        }
        KButton{
            ishover: false
            btn_color: viewset.primaryColor
            text: "Cancel"
            x:24
            y:272
            borderRadius: 4
            btn_borderWidth: 0
        }
    }
}