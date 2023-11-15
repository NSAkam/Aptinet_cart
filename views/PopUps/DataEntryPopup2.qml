
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

        Rectangle{
            width: 60
            height: 60
            color: "white"
            x: 32
            y: 36

            Button {
                width: 60
                height: 60
                background: Rectangle {
                    color: "white"
                }
            Text {
                text: "1"
                width: 12
                height: 44
                x: 24
                y: 8
                font.pixelSize: 40
                color: "#9D9D9D"
            }
            }
        }

        Rectangle{
            width: 60
            height: 60
            color: "white"
            x: 32
            y: 108

            Button {
                width: 60
                height: 60
                background: Rectangle {
                    color: "white"
                }
            Text {
                text: "4"
                width: 12
                height: 44
                x: 24
                y: 8
                font.pixelSize: 40
                color: "#9D9D9D"
            }
            }
        }

        Rectangle{
            width: 60
            height: 60
            color: "white"
            x: 32
            y: 180

            Button {
                width: 60
                height: 60
                background: Rectangle {
                    color: "white"
                }
            Text {
                text: "7"
                width: 12
                height: 44
                x: 24
                y: 8
                font.pixelSize: 40
                color: "#9D9D9D"
            }
            }
        }

        Rectangle{
            width: 60
            height: 60
            color: "white"
            x: 32
            y: 252

            Button {
                width: 60
                height: 60
                background: Rectangle {
                    color: "white"
                }
            Text {
                text: "#"
                width: 12
                height: 44
                x: 24
                y: 8
                font.pixelSize: 40
                color: "#9D9D9D"
            }
        }
        }

        Rectangle{
            width: 60
            height: 60
            color: "white"
            x: 104
            y: 36

            Button {
                width: 60
                height: 60

                background: Rectangle {
                    color: "white"
                }
            Text {
                text: "2"
                width: 12
                height: 44
                x: 24
                y: 8
                font.pixelSize: 40
                color: "#9D9D9D"
            }
            }
        }

        Rectangle{
            width: 60
            height: 60
            color: "white"
            x: 104
            y: 108

            Button {
                width: 60
                height: 60
                background: Rectangle {
                    color: "white"
                }
            Text {
                text: "5"
                width: 12
                height: 44
                x: 24
                y: 8
                font.pixelSize: 40
                color: "#9D9D9D"
            }
            }
        }

        Rectangle{
            width: 60
            height: 60
            color: "white"
            x: 104
            y: 180

            Button {
                width: 60
                height: 60
                background: Rectangle {
                    color: "white"
                }
            Text {
                text: "8"
                width: 12
                height: 44
                x: 24
                y: 8
                font.pixelSize: 40
                color: "#9D9D9D"
            }
            }
        }

        Rectangle{
            width: 60
            height: 60
            color: "white"
            x: 104
            y: 252

            Button {
                width: 60
                height: 60
                background: Rectangle {
                    color: "white"
                }
            Text {
                text: "0"
                width: 12
                height: 44
                x: 24
                y: 8
                font.pixelSize: 40
                color: "#9D9D9D"
            }
            }
        }

        Rectangle{
            width: 60
            height: 60
            color: "white"
            x: 176
            y: 36

            Button {
                width: 60
                height: 60
                background: Rectangle {
                    color: "white"
                }
            Text {
                text: "3"
                width: 12
                height: 44
                x: 24
                y: 8
                font.pixelSize: 40
                color: "#9D9D9D"
            }
            }
        }

        Rectangle{
            width: 60
            height: 60
            color: "white"
            x: 176
            y: 108

            Button {
                width: 60
                height: 60
                background: Rectangle {
                    color: "white"
                }
            Text {
                text: "6"
                width: 12
                height: 44
                x: 24
                y: 8
                font.pixelSize: 40
                color: "#9D9D9D"
            }
            }
        }

        Rectangle{
            width: 60
            height: 60
            color: "white"
            x: 176
            y: 180

            Button {
                width: 60
                height: 60
                background: Rectangle {
                    color: "white"
                }

            Text {
                text: "9"
                width: 12
                height: 44
                x: 24
                y: 8
                font.pixelSize: 40
                color: "#9D9D9D"
            }
            }
        }

        Rectangle{
            width: 60
            height: 60
            color: "white"
            x: 176
            y: 180

            Button {
                width: 60
                height: 60
                background: Rectangle {
                    color: "white"
                }
            Text {
                text: "9"
                width: 12
                height: 44
                x: 24
                y: 8
                font.pixelSize: 40
                color: "#9D9D9D"
            }
            }
        }

        Rectangle{
            width: 60
            height: 60
            color: "white"
            x: 176
            y: 252

            Button {
                width: 60
                height: 60
                background: Rectangle {
                    color: "white"
                }
                Image {
                source: "../../Assets/calcback.png"
                width: 36
                height: 26
                x: 10
                y: 17
            }
            }
        }
    }

    function toggleRectangles() {
            dataEntryPopup.visible = !dataEntryPopup.visible;
        }
}
