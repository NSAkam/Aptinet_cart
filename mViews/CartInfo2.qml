import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.12
import QtQuick.Window 2.14






Item {
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

            Button {
                width: 92
                height: 92
                x: 0
                y: 0
                onClicked: {
                    stackview.pop();
                }
                background: Rectangle {
                    color: "#EDEDED"
                }

                Image {
                    source: "/home/mahnaz/akam/ui_aptinet/assets/back.png"
                    x: 28
                    y: 28
                    width: 40
                    height: 38
                }
            }

        }

        Rectangle {
        width: 672
        height: 104
        color: "white"
        x: 304
        y: 312
        layer.enabled: true
            layer.effect: DropShadow {
            horizontalOffset: 1
            verticalOffset: 1
            radius: 10
            samples: 16
            color: "#d3d3d3"
        }

        Text {
            text: "Software Version"
            font.pixelSize: 20
            font.family: "Archivo"
            color: "black"
            width: 160
            height: 22
            x: 24
            y: 24
        }

        Text {
            text: "2.8 is available"
            font.pixelSize: 20
            font.family: "Aechivo"
            color: "#9D9D9D"
            width: 139
            height: 22
            x: 24
            y: 58
        }

        Rectangle {
            width: 244
            height: 50
            x: 404
            y: 27

            Button {
                width: 244
                height: 50
                background: Rectangle {
                color: "white"
                border.color: "#4696FA"
                border.width: 2
                }
            }

            Text {
                text: "Download and Install"
                color: "#4696FA"
                width: 196
                height: 22
                x: 24
                y: 14
                font.pixelSize: 20
            }
        }

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
    
    }

    



    

