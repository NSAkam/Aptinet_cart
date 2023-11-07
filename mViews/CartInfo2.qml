import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.12
import QtQuick.Window 2.14




<<<<<<< HEAD:mViews/calibrate1.qml
=======


>>>>>>> b056f0334a0a1517df55c9885375e31df01ec07e:mViews/CartInfo2.qml
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
<<<<<<< HEAD:mViews/calibrate1.qml
                // onClicked: stackview.pop()
=======
                onClicked: {
                    stackview.pop();
                }
>>>>>>> b056f0334a0a1517df55c9885375e31df01ec07e:mViews/CartInfo2.qml
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

<<<<<<< HEAD:mViews/calibrate1.qml
    Button {
        // background: Item{}
        width: 384
        height: 70
        onClicked: {
            toggleButtons();
        }
        background: Rectangle {
            width: 384
            height: 70
            color: "white"
            x: 195.98
            y: 336
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
=======
>>>>>>> b056f0334a0a1517df55c9885375e31df01ec07e:mViews/CartInfo2.qml
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
    
    }

    



    

