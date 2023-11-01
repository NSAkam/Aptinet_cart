import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.12
import QtQuick.Window 2.14



Window {
    id: root
    visible: true
    width: 1280
    height: 800
   

    Image {     id: q
                source: "/home/mahnaz/akam/ui_aptinet/assets/akam.png" 
                anchors.fill: parent
                opacity: 0.7
    

                Rectangle {
                    width: parent.width
                    height: parent.height
                    color: "white" 
                    opacity: 0.7
                    anchors.fill: parent
            }
        }

    FastBlur {

            anchors.fill: q
            source: q
            radius: 70
        }


        Rectangle {
            width: parent.width
            height: 92 
            color: "white"

            Image {
                source: "/home/mahnaz/akam/ui_aptinet/assets/aptinet.png"
                x: 550
                y: 32
                width: 180
                height: 21
            }

            Image {
                    source: "/home/mahnaz/akam/ui_aptinet/assets/smartcart.png"
                    x: 578
                    y: 65
                    width: 124
                    height: 12
            }

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
            verticalOffset: 3
            radius: 10
            samples: 16
            color: "gray"
        }

            Image {
                source: "/home/mahnaz/akam/ui_aptinet/assets/union.png"
                width: 170
                height: 170
                x: 75
                y: 79
            }

            Image {
                source: "/home/mahnaz/akam/ui_aptinet/assets/barcode.png"
                width: 95
                height: 95
                x: 113
                y: 116
            }

            Image {
                source: "/home/mahnaz/akam/ui_aptinet/assets/line.png"
                width: 170
                height: 12
                x: 75
                y: 158
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
            verticalOffset: 3
            radius: 10
            samples: 16
            color: "gray"
        }

        Rectangle {
            id: myrectangel
            width: 295
            height: 56
            x: 24
            y: 24
            color: "#F7F7F7"
            // InnerShadow {
            //     cached: true
            //     horizontalOffset: 0
            //     verticalOffset: 0
            //     radius: 16
            //     samples: 32
            //     color: "#b0000000"
            //     smooth: true
            //     source: myrectangel

                Text {
                    text: "Username"
                    width: 99
                    height: 22
                    x: 24
                    y: 15
                    color: "#BDBDBD"
                    font.pixelSize: 20
                    font.family: "Archivo"
                }
            // }
        }

        Rectangle {
            width: 295
            height: 56
            x: 24
            y: 92
            color: "#F7F7F7"

            Text {
                    text: "Membership code"
                    width: 171
                    height: 22
                    x: 24
                    y: 15
                    color: "#BDBDBD"
                    font.pixelSize: 20
                    font.family: "Archivo"
                }
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

            Image {
                source: "/home/mahnaz/akam/ui_aptinet/assets/flash2.png"
                width: 9
                height: 16
                x: 254
                y: 24
            }

            Text {
                    text: "Confirm"
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

        }