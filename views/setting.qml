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
                source: "Assets/akam.png" 
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
                source: "Assets/aptinet.png"
                x: 550
                y: 32
                width: 180
                height: 21
            }

            Image {
                    source: "Assets/smartcart.png"
                    x: 578
                    y: 65
                    width: 124
                    height: 12
            }

        }

        Row {
            spacing: 30
            x: 248
            y: 155
            anchors {
                top: parent.top
                horizontalCenter: parent.horizontalCenter
                topMargin:232 
            }

            Button {
                width: 128
                height: 160

                background: Rectangle {
                    
                    color: "white"
                    
                }
        

                Image {
                    source: "Assets/server.png"
                    width: 64
                    height: 64
                    x: 34
                    y: 30
                }

                Text {
                    text: "server"
                    width: 70
                    height: 20
                    x: 42
                    y: 124
                    font.family: "Archivo"
                    color: "gray"
                }
            }

            Button {
                width: 128
                height: 160

                background: Rectangle {
                    
                    color: "white"
                    
                }

                Image {
                    source: "Assets/wifi.png" 
                    height: 64
                    x: 25
                    y: 30
                }

                Text {
                    text: "Wi-Fi"
                    width: 56
                    height: 20
                    x: 45
                    y: 124
                    color: "gray"
                }
            }

            Button {
                width: 128
                height: 160

                background: Rectangle {
                    
                    color: "white"
                    
                }

                Image {
                    source: "Assets/data.png" 
                    width: 64
                    height: 64
                    x: 34
                    y: 30
                }

                Text {
                    text: "Data Entry"
                    width: 56
                    height: 20
                    x: 33
                    y: 124
                    color: "gray"
                }
            }

            Button {
                width: 128
                height: 160

                background: Rectangle {
                    
                    color: "white"
                    
                }

                Image {
                    source: "Assets/calibrate.png"
                    width: 64
                    height: 64
                    x: 34
                    y: 30
                }

                Text {
                    text: "Calibrate"
                    x: 33
                    y: 124
                    width: 56
                    height: 20
                    color: "gray"
                }
            }
        }

        Row {
            spacing: 30
            x: 339
            y: 425

            Button {
                width: 128
                height: 160
                
                background: Rectangle {
                    
                    color: "white"
                    
                }

                Image {
                    source: "Assets/device.png"
                    width: 64
                    height: 64
                    x: 34
                    y: 30
                }

                Text {
                    text: "Device Test"
                    width: 70
                    height: 20
                    x: 30
                    y: 124
                    font.family: "Archivo"
                    color: "gray"
                }
            }

            Button {
                width: 128
                height: 160
                background: Rectangle {
                    
                    color: "white"
                    
                }

                Image {
                    source: "Assets/cartinfo.png" 
                    height: 64
                    x: 32
                    y: 30
                }

                Text {
                    text: "Cart Info"
                    width: 56
                    height: 20
                    x: 38
                    y: 124
                    color: "gray"
                }
            }

            Button {
                width: 128
                height: 160

                background: Rectangle {
                    
                    color: "#BDBDBD"
                    
                }

                Image {
                    source: "Assets/back.png" 
                    width: 64
                    height: 64
                    x: 34
                    y: 30
                }

                Text {
                    text: "Back"
                    width: 56
                    height: 20
                    x: 50
                    y: 124
                    color: "gray"
                }
            }

            Button {
                width: 128
                height: 160

                background: Rectangle {
                    
                    color: "#6D6D6D"
                    
                }

                Image {
                    source: "Assets/turnoff.png"
                    width: 64
                    height: 64
                    x: 33
                    y: 30
                }

                Text {
                    text: "Turn Off"
                    x: 35
                    y: 124
                    width: 56
                    height: 20
                    color: "#1D1D1D"
                }
            }

        }
    Rectangle {
        id: b
        color: "gray"
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