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
                onClicked: 
                    stackview.pop();
                
            }

        }

        Row {
            spacing: 30
            x: 330
            y: 500
            anchors {
                top: parent.top
                horizontalCenter: parent.horizontalCenter
                topMargin:300
            }

            Button {
                width: 128
                height: 160

                background: Rectangle {
                    
                    color: "white"
                    
                }

                onClicked: {
                    weightsesnsorPopup.open()
                    s.z = root.z + 1
                    s.visible = true
                    s.opacity = 0.8
                    stackview.push(test)
                }
        

                Image {
                    source: "/home/mahnaz/akam/ui_aptinet/assets/weightsensor.png"
                    width: 64
                    height: 64
                    x: 34
                    y: 30
                }


                Column {
                    spacing: 5
                    y: 100

                    Text {
                        text: "Weight"
                        width: 70
                        height: 20
                        x: 40
                        font.family: "Archivo"
                        color: "#6D6D6D"
                        font.pixelSize: 16
                    }

                    Text {
                        text: "Sensor"
                        width: 70
                        height: 20
                        x: 40
                        font.family: "Archivo"
                        color: "#6D6D6D"
                        font.pixelSize: 16
                    }
                }

            }

            Button {
                width: 128
                height: 160

                background: Rectangle {
                    
                    color: "white"
                    
                }
                onClicked: {
                    sensorPopup.open()
                    w.z = root.z + 1
                    w.visible = true
                    w.opacity = 0.8
                }

                Image {
                    source: "/home/mahnaz/akam/ui_aptinet/assets/scanner.png" 
                    height: 64
                    x: 25
                    y: 30
                }

                Text {
                    text: "Scanner"
                    width: 70
                    height: 20
                    x: 34
                    y: 124
                    color: "#6D6D6D"
                    font.pixelSize: 18
                }
            }

            Button {
                width: 128
                height: 160
                onClicked: {
                    serverPopup.open()
                    b.z = root.z + 1
                    b.visible = true
                    b.opacity = 0.8
                    stackview.push(lights)
                }

                background: Rectangle {
                    
                    color: "white"
                    
                }

                Image {
                    source: "/home/mahnaz/akam/ui_aptinet/assets/lights.png" 
                    width: 64
                    height: 64
                    x: 24
                    y: 30
                }

                Text {
                    text: "Lights"
                    width: 52
                    height: 20
                    x: 33
                    y: 124
                    color: "#6D6D6D"
                    font.pixelSize: 18
                }
            }

            Button {
                width: 128
                height: 160

                background: Rectangle {
                    
                    color: "white"
                    
                }

                Image {
                    source: "/home/mahnaz/akam/ui_aptinet/assets/sound.png"
                    width: 72
                    height: 60
                    x: 34
                    y: 30
                }

                Text {
                    text: "Sound"
                    width: 52
                    height: 20
                    x: 33
                    y: 124
                    color: "#6D6D6D"
                    font.pixelSize: 18
                    
                }
            }
        }
    
    LightsPopup {
        id: serverPopup
    }

    ScannerPopup {
        id: sensorPopup
    }

    WeightsensorPopup {
        id: weightsesnsorPopup
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

    Rectangle {
        id: w
        color: "gray"
        width: 1280
        height: 708
        visible: true
        opacity: 0
        x: 0
        y: 92

        FastBlur {

            anchors.fill: w
            source: q
            radius: 70
        }
    }

    Rectangle {
        id: s
        color: "gray"
        width: 1280
        height: 708
        visible: true
        opacity: 0
        x: 0
        y: 92

        FastBlur {

            anchors.fill: s
            source: q
            radius: 70
        }
    }

    Component {
        id:test
        WeightsensorPopup {}
    }

    Component {
        id: lights
        LightsPopup{}
    }
    
    }

    



    

