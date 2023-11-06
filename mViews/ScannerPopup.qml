import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.12
import QtQuick.Window 2.14


Popup {
    id: sensorPopup
    background: Item {}

     Rectangle {
            width: 375
            height: 402
            x: 453
            y: 166
            color: "white"
            layer.enabled: true
            layer.effect: DropShadow {
            horizontalOffset: 1
            verticalOffset: 1
            radius: 10
            samples: 16
            color: "#d3d3d3"
        }


            Image {
                source: "/home/mahnaz/akam/ui_aptinet/assets/subtract.png"
                width: 295
                height: 101
                x: 40
                y: 176
            }

            Image {
                source: "/home/mahnaz/akam/ui_aptinet/assets/barcode2.png"
                width: 259
                height: 64
                x: 58
                y: 195
            }

            Image {
                source: "/home/mahnaz/akam/ui_aptinet/assets/line2.png"
                width: 295
                height: 6
                x: 40
                y: 224
            }

            Rectangle {
                width: 295
                height: 56
                color: "#F7F7F7"
                x: 40
                y: 306
            }
        }

        ColumnLayout {
            spacing: 0
            x: 492
            y: 180

            Text {
                Layout.fillWidth: true
                text: "Please scan the"
                font.pixelSize: 32
                color: "black"
                x: 492
                y: 180
            }

            Text {
                Layout.fillWidth: true
                text: "item barcode"
                font.pixelSize: 32
                color: "black"
                x: 492
                y: 180
            }
    }


        }
