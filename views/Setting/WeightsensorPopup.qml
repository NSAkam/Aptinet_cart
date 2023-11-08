import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.12
import QtQuick.Window 2.14


Popup {
    id: weightsesnsorPopup
    background: Item {}


    Rectangle {
        width: 525
        height: 387
        color: "white"
        x: 378
        y: 200

        Text {
            text: "Please put the weight in cart"
            width: 445
            height: 44
            x: 40
            y: 40
            color: "black"
            font.pixelSize: 32
        }
        
        Image {
            source: "../assets/bag1.png"
            width: 49.97
            height: 56.52
            x: 40
            y: 122.24
            z: 100
        }

        Image {
            source: "../assets/bag2.png"
            width: 40.14
            height: 45.05
            x: 76.86
            y: 133.71
            z: 0
        }

        Rectangle {
            width: 343
            height: 56
            color: "#F7F7F7"
            x: 141
            y: 122.5

            Rectangle {
                width: 56
                height: 56
                x: 287
                y: 0
                color: "#D9D9D9"

                Text {
                    text: "gr"
                    width: 24
                    height: 20
                    x: 18
                    y: 16
                    color: "#6D6D6D"
                    font.pixelSize: 24
                }
            }
        }

        Button {
            width: 241
            height: 72
            background: Rectangle {
                color: "#4696FA"
                radius: 2

                Text {
                    text: "Confirm"
                    width: 97
                    height: 48
                    x: 72
                    y: 22
                    color: "white"
                    font.pixelSize: 24
                }
            }
            x: 243
            y: 217
        }

        Button {
            width: 187
            height: 72
            background: Rectangle {
                color: "#F08C5A"
                radius: 2

                Text {
                    text: "Calibrate"
                    width: 106
                    height: 48
                    x: 49
                    y: 20
                    color: "white"
                    font.pixelSize: 24
                }

                Image {
                    source: "../assets/whiteflash.png"
                    width: 9
                    height: 16
                    x: 24
                    y: 28
                }
            }
            x: 40
            y: 217
        }

        Text {
            text: "Calibration Date"
            width: 152
            height: 22
            x: 40
            y: 333
            color: "black"
            font.pixelSize: 20
            font.family: "Archivo"
        }

        Text {
            text: "2023/02/03"
            width: 107
            height: 22
            x: 281
            y: 333
            color: "#6D6D6D"
            font.pixelSize: 20
            font.family: "Archivo"
        }

        Text {
            text: "Expired"
            width: 73
            height: 22
            x: 412
            y: 333
            color: "#F08C5A"
            font.pixelSize: 20
            font.family: "Archivo"
        }
    }
}
