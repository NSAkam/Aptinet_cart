import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.12
import QtQuick.Window 2.14






ApplicationWindow{
    id: root
    visible: true
    width: 1280
    height: 800


    Image {     id: q
                source: "../assets/AuthenticationBackground.png"
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
                source: "../assets/aptinet.png"
                x: 550
                y: 32
                width: 180
                height: 21
            }

            Image {
                    source: "../assets/smartcart.png"
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
                background: Rectangle {
                    color: "#EDEDED"
                }

                Image {
                    source: "../assets/back.png"
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
        radius: 4
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
            color: "black"
            x: 24
            y: 24
        }

        Text {
            text: "2.8 is available"
            font.pixelSize: 20
            color: "#9D9D9D"
            x: 24
            y: 58
        }

         Button {
            width: 244
            height: 50
            x: 404
            y: 27
            background: Rectangle {
                color: "white"
                radius: 2
                border.color: "#4696FA"
                border.width: 1
                

            Text {
                text: "Download and install"
                width: 196
                height: 22
                x: 24
                y: 14
                color: "#4696FA"
                font.pixelSize: 20
            }
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



    

