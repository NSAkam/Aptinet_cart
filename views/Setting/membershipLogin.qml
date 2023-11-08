import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.12
import "../Components"



Item {
    id: root
    visible: true
    width: 1280
    height: 800


    Image {
        id: q
        source: "file://../Assets/AuthenticationBackground.png"
        anchors.fill: parent
    }




    Rectangle {
        width: 687
        height: 72
        color: "#4696FA"
        x: 296
        y: 212
        radius: 6

        Text {
            text: "Please scan the membership card"
            width: 413
            height: 48
            color: "white"
            font.pixelSize: 24
            x: 137
            y: 20
            font.family: "Archivo"
            font.weight: Font.Bold
        }
    }

    Rectangle {
        width: 320
        height: 328
        color: "white"
        x: 300
        y: 304

        layer.enabled: true
        layer.effect: DropShadow {
            horizontalOffset: 3
            verticalOffset: 0
            radius: 15
            samples: 19
            color: "#BDBDBD"
        }

        Image {
            source: "file://../assets/Qr.png"
            width: 170
            height: 170
            x: 75
            y: 79
        }
    }

    Rectangle {
        width: 343
        height: 328
        color: "white"
        x: 641
        y: 304

        layer.enabled: true
        layer.effect: DropShadow {
            horizontalOffset: 3
            verticalOffset: 0
            radius: 15
            samples: 19
            color: "#BDBDBD"
        }

        TextInput {
            id: myrectangel
            width: 295
            height: 56
            x: 24
            y: 24
            // InnerShadow {
            //     cached: true
            //     horizontalOffset: 0
            //     verticalOffset: 0
            //     radius: 16
            //     samples: 32
            //     color: "#b0000000"
            //     smooth: true
            //     source: myrectangel

//            Text {
//                text: "Username"
//                width: 99
//                height: 22
//                x: 24
//                y: 15
//                color: "#BDBDBD"
//                font.pixelSize: 20
//                font.family: "Archivo"
//            }
            // }
        }

        TextInput {
            width: 295
            height: 56
            x: 24
            y: 92

        }

        Button {
            width: 295
            height: 64
            background: Rectangle {
                color: "#4696FA"
                radius: 6
            }
            x: 24
            y: 168


            Text {
                text: "Confirm >"
                width: 92
                height: 26
                x: 100
                y: 17
                color: "white"
                font.pixelSize: 25
                font.family: "Archivo"

            }
        }

        Button {
            width: 295
            height: 64
            background: Rectangle {
                color: "#F5AF8C"
                radius: 6
            }
            x: 24
            y: 248

            Text {
                text: "Back"
                width: 49
                height: 22
                x: 123
                y: 17
                color: "white"
                font.pixelSize: 25
                font.family: "Archivo"

            }
        }
    }
    TopNav{

    }
}
