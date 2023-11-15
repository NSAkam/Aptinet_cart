import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.12
import QtQuick.Window 2.14
import "../Components"
import "../Setting"





Item {
    id: root
    visible: true
    width: 1280
    height: 800



    Image {
        id: q
        source: "../../Assets/AuthenticationBackground.png"
        anchors.fill: parent
    }

    Rectangle {
        width: 128
        height: 70
        radius: 4
        color: "#F08C5A"
        x: 195.98
        y: 226

        Text {
            text: "gr"
            font.family: "Archivo"
            color: "white"
            font.pixelSize: 24
            x: 52
            y: 21
        }
    }

    Button {
        width: 256
        height: 70

        background: Rectangle {
            width: 256
            height: 70
            color: "white"
            x: 323.98
            y: 226
            layer.enabled: true
            layer.effect: DropShadow {
                horizontalOffset: 1
                verticalOffset: 1
                radius: 10
                samples: 16
                color: "#d3d3d3"
            }

            Text {
                text: "Change Unit"
                font.family: "Archivo"
                color: "black"
                font.pixelSize: 20
                width: 122
                height: 22
                x: 32
                y: 24
            }

        }
    }

    Rectangle {
        width: 384
        height: 70
        x: 195.98
        y: 336

        Button {
            width: 384
            height: 70
            onClicked: {
                toggleButtons();
            }
            background: Rectangle {
                color: "white"
                layer.enabled: true
                layer.effect: DropShadow {
                    horizontalOffset: 1
                    verticalOffset: 1
                    radius: 10
                    samples: 16
                    color: "#d3d3d3"
                }

                Text {
                    text: "Enter Weight"
                    width: 127
                    height: 22
                    x: 160
                    y: 24
                    color: "black"
                    font.family: "Archivo"
                    font.pixelSize: 20
                }

                Rectangle {
                    width: 124
                    height: 62
                    color: "#F7F7F7"
                    x: 4
                    y: 4
                    layer.enabled: true
                    layer.effect: DropShadow {
                        horizontalOffset: 1
                        verticalOffset: 1
                        radius: 10
                        samples: 16
                        color: "#d3d3d3"
                    }

                }
            }

        }
    }

    Rectangle {
        width: 471
        height: 180
        color: "#F7F7F7"
        x: 612
        y: 226

        layer.enabled: true
        layer.effect: DropShadow {
            horizontalOffset: 1
            verticalOffset: 1
            radius: 10
            samples: 16
            color: "#d3d3d3"
        }

        Text {
            text: "How to Calibrating"
            width: 226
            height: 26
            x: 122.5
            y: 26
            color: "#6D6D6D"
            font.family: "Archivo"
            font.pixelSize: 24
            // font.bold: true
        }

        Image {
            source: "/home/mahnaz/akam/ui_aptinet/assets/1.png"
            width: 30
            height: 30
            x: 51
            y: 76
        }

        Column {
            spacing: -20
            y: 116

            Text {
                text: "Select"
                width: 50
                height: 44
                x: 41
                font.family: "Archivo"
                color: "#6D6D6D"
                font.pixelSize: 16
            }

            Text {
                text: "unit"
                width: 50
                height: 44
                x: 50
                font.family: "Archivo"
                color: "#6D6D6D"
                font.pixelSize: 16
            }
        }

        Image {
            source: "/home/mahnaz/akam/ui_aptinet/assets/2.png"
            width: 30
            height: 30
            x: 151.5
            y: 76
        }

        Column {
            spacing: -20
            y: 116

            Text {
                text: "Select"
                width: 50
                height: 44
                x: 140
                font.family: "Archivo"
                color: "#6D6D6D"
                font.pixelSize: 16
            }

            Text {
                text: "weight"
                width: 50
                height: 44
                x: 140
                font.family: "Archivo"
                color: "#6D6D6D"
                font.pixelSize: 16
            }
        }

        Image {
            source: "/home/mahnaz/akam/ui_aptinet/assets/3.png"
            width: 30
            height: 30
            x: 268.5
            y: 76
        }

        Column {
            spacing: -20
            y: 116

            Text {
                text: "put weight"
                width: 50
                height: 44
                x: 242
                font.family: "Archivo"
                color: "#6D6D6D"
                font.pixelSize: 16
            }

            Text {
                text: "in the cart"
                width: 50
                height: 44
                x: 242
                font.family: "Archivo"
                color: "#6D6D6D"
                font.pixelSize: 16
            }
        }

        Image {
            source: "/home/mahnaz/akam/ui_aptinet/assets/4.png"
            width: 30
            height: 30
            x: 387.5
            y: 76
        }

        Column {
            spacing: -20
            y: 116

            Text {
                text: "Hold to"
                width: 50
                height: 44
                x: 374
                font.family: "Archivo"
                color: "#6D6D6D"
                font.pixelSize: 16
            }

            Text {
                text: "realize"
                width: 50
                height: 44
                x: 374
                font.family: "Archivo"
                color: "#6D6D6D"
                font.pixelSize: 16
            }
        }
    }

    Rectangle {
        width: 471
        height: 112
        color: "#4696FA"
        x: 612
        y: 430
        radius: 3

        Text {
            text: "Hold to Realize"
            width: 184
            height: 26
            color: "white"
            x: 143.5
            y: 43
            font.pixelSize: 24
        }
    }

    Rectangle {
        width: 471
        height: 80
        color: "#F5AF8C"
        x: 612
        y: 566
        radius: 3

        Text {
            text: "Save"
            color: "white"
            width: 61
            height: 26
            x: 205
            y: 27
            font.pixelSize: 24
        }
    }

    Rectangle {
        id: rectangle1
        visible: false
        width: 252
        height: 306
        color: "white"
        x: 328
        y: 430

        layer.enabled: true
        layer.effect: DropShadow {
            horizontalOffset: 1
            verticalOffset: 1
            radius: 10
            samples: 16
            color: "#d3d3d3"
        }

        Button {
            background: Item {}
            Text {
                text: "1"
                color: "#9D9D9D"
                width: 12
                height: 44
                font.pixelSize: 40
                x: 48
                y: 23
            }
        }

        Button {
            background: Item {}
            Text {
                text: "4"
                color: "#9D9D9D"
                width: 12
                height: 44
                font.pixelSize: 40
                x: 48
                y: 95
            }
        }

        Button {
            background: Item {}
            Text {
                text: "7"
                color: "#9D9D9D"
                width: 12
                height: 44
                font.pixelSize: 40
                x: 48
                y: 167
            }
        }

        Button {
            background: Item {}
            Text {
                text: "2"
                color: "#9D9D9D"
                width: 12
                height: 44
                font.pixelSize: 40
                x: 120
                y: 20
            }
        }

        Button {
            background: Item {}
            Text {
                text: "5"
                color: "#9D9D9D"
                width: 12
                height: 44
                font.pixelSize: 40
                x: 120
                y: 95
            }
        }

        Button {
            background: Item {}
            Text {
                text: "0"
                color: "#9D9D9D"
                width: 12
                height: 44
                font.pixelSize: 40
                x: 120
                y: 239
            }
        }

        Button {
            background: Item {}
            Text {
                text: "8"
                color: "#9D9D9D"
                width: 12
                height: 44
                font.pixelSize: 40
                x: 120
                y: 167
            }
        }

        Button {
            background: Item {}
            Text {
                text: "3"
                color: "#9D9D9D"
                width: 12
                height: 44
                font.pixelSize: 40
                x: 192
                y: 20
            }
        }

        Button {
            background: Item {}
            Text {
                text: "6"
                color: "#9D9D9D"
                width: 12
                height: 44
                font.pixelSize: 40
                x: 192
                y: 90
            }
        }

        Button {
            background: Item {}
            Text {
                text: "9"
                color: "#9D9D9D"
                width: 12
                height: 44
                font.pixelSize: 40
                x: 192
                y: 167
            }
        }

        Button {
            background: Item {}

            Image {
                source: "/home/mahnaz/akam/ui_aptinet/assets/calcback.png"
                width: 35
                height: 26
                x: 34
                y: 248
            }
        }

        Button {
            background: Item {}

            Rectangle {
                width: 60
                height: 42
                color: "#4696FA"
                x: 168
                y: 240
                radius: 3

                Image {
                    source: "/home/mahnaz/akam/ui_aptinet/assets/calcflash.png"
                    width: 17
                    height: 20
                    x: 21
                    y: 11
                }
            }
        }

    }

    function toggleButtons() {
        rectangle1.visible = !rectangle1.visible;
    }




    Rectangle {
        id: b
        color: "white"
        width: 1280
        height: 708
        visible: true
        opacity: 0
        x: 0
        y: 92

        FastBlur {

            anchors.fill: b
            source: q
            radius: 70
        }
    }


    Component {
        id: calibrate
        Calibrate1{}
    }


    TopNav{
        backvisible: true
        onBackClicked: {
            stackview.pop()
        }

    }


    Rectangle {
        id:focusrect
        width: root.width
        height: root.height
        color: "black"
        opacity: 0.5
        visible: true
    }

    Rectangle {
        id:focusrectItems
        width: 471
        height: 112
        color: "#4696FA"
        x: 612
        y: 430
        radius: 3

        Button {
            width: 471
            height: 112
            x: 0
            y: 0
            onClicked: {
                focusrect.visible=false
                focusrectItems.visible=false
            }
            background: Rectangle {
                color: "#4696FA"
            }
        }

        Text {
            text: "Hold to Realize"
            width: 184
            height: 26
            color: "white"
            x: 143.5
            y: 43
            font.pixelSize: 24
        }
    }

    Rectangle {
        width: 384
        height: 112
        x: 194
        y: 430
        color: "white"

        Column {

            anchors.centerIn: parent
            Text {
                text: "Make sure the cart is empty"
                font.pixelSize: 24
                color: "#6D6D6D"
            }

            Text {
                text: "and then hold the button"
                font.pixelSize: 24
                color: "#6D6D6D"
            }

        }

    }
}










