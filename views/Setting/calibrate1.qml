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
                source: "file://../assets/AuthenticationBackground.png"
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
                source: "file://../assets/aptinet.png"
                x: 550
                y: 32
                width: 180
                height: 21
            }

            Image {
                    source: "file://../assets/smartcart.png"
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
                    source: "file://../assets/back.png"
                    x: 28
                    y: 28
                    width: 40
                    height: 38
                }
            }

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

        //     Image {
        //     source: "file://../assets/menu.png"
        //     width: 9
        //     height: 16
        //     x: 216
        //     y: 30.5   
        // }
    }
        }

    Rectangle {
            width: 256
            height: 70
            color: "white"
            x: 323.98
            y: 336
            layer.enabled: true
            layer.effect: DropShadow {
            horizontalOffset: 1
            verticalOffset: 1
            radius: 10
            samples: 16
            color: "#d3d3d3"
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



    

