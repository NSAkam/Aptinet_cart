
import QtQuick 2.15
import QtQuick.Window 2.12
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0


Popup {
    id: dataEntryPopup

    Rectangle {
        width: 639
       height: 72
       color: "#F05A28"
       x: 548
       y: 192
       radius: 4

       Text {
        text: "Please enter the item barcode "
        color: "white"
        font.pixelSize: 24
        font.family: "Archivo"
        font.bold: true
        x: 120
        y: 12
       }
    }

    Rectangle {
        width: 343
        height: 348
        color: "white"
        x: 844
        y: 284
        radius: 4

        Image {
            source: "../../Assets/barcodeimage.png"
            width: 295
            height: 63
            x: 24
            y: 24
        }

        Button {
            width: 295
            height: 64
            x: 24
            y: 192
            background: Rectangle {
                color: "#4696FA"
                radius: 4
            }

            Text {
                text: "Confirm          >"
                width: 92
                height: 26
                color: "white"
                font.pixelSize: 24
                x: 98
                y: 19
            }
        }

        Button {
            width: 295
            height: 64
            x: 24
            y: 272
            background: Rectangle {
                color: "#F5AF8C"
                radius: 4
            }

            Text {
                text: "Cancel"
                width: 92
                height: 26
                color: "white"
                font.pixelSize: 24
                x: 98
                y: 19
            }
        }
    }

    Rectangle {
        width: 276
        height: 348
        color: "white"
        x: 548
        y: 284
        radius: 4
    }

    function toggleRectangles() {
            dataEntryPopup.visible = !dataEntryPopup.visible;
        }
}
