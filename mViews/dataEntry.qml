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
            }

        }

    Rectangle {
        width: 287
        height: 344
        radius: 4
        color: "white"
        x: 120
        y: 192
        layer.enabled: true
            layer.effect: DropShadow {
            horizontalOffset: 1
            verticalOffset: 1
            radius: 10
            samples: 16
            color: "#d3d3d3"
            }

        Column {
                spacing: -20
                y: 200

            Text {
                text: "Nutella Hazelnut Spread"
                width: 239
                height: 64
                x: 30
                font.family: "Archivo"
                color: "black"
                font.pixelSize: 20
            }

            Text {
                text: "with Cocoa, 750g"
                width: 239
                height: 64
                x: 34
                font.family: "Archivo"
                color: "black"
                font.pixelSize: 20
            }
            }

        Image {
            source: "/home/mahnaz/akam/ui_aptinet/assets/nutella.png"
            width: 126
            height: 126
            x: 80
            y: 43
        }

        Text {
            text: "EAN-13:"
            font.pixelSize: 16
            width: 65
            height: 18
            x:  24
            y: 298
        }

        Text {
            text: "8 000500 012178"
            color: "#9D9D9D"
            width: 129
            height: 17
            x: 134
            y: 298.5
        }
    }

    Button {
        background: Item{}
        Rectangle {
            width: 287
            height: 62
            radius: 4
            color: "#F08C5A"
            x: 120
            y: 568

            Text {
                text: "Add QR Code"
                color: "white"
                font.pixelSize: 20
                width: 129
                height: 22
                x: 79
                y: 20
            }
        }
    }

    Rectangle {
        width: 208
        height: 62
        radius: 4
        x: 455
        y: 192
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
            text: "748 g"
            width: 54
            height: 22
            color: "#6D6D6D"
            x: 77
            y: 20
            font.pixelSize: 20
            font.family: "Archivo"
        }
    }

    Rectangle {
        width: 208
        height: 62
        radius: 4
        x: 455
        y: 286
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
            text: "Set weight #2"
            width: 134
            height: 22
            color: "#D9D9D9"
            x: 37
            y: 20
            font.pixelSize: 20
            font.family: "Archivo"
        }
    }

    Rectangle {
        width: 208
        height: 62
        radius: 4
        x: 455
        y: 380
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
            text: "Set weight #3"
            width: 134
            height: 22
            color: "#D9D9D9"
            x: 37
            y: 20
            font.pixelSize: 20
            font.family: "Archivo"
        }
    } 
    
    Rectangle {
        width: 208
        height: 62
        radius: 4
        x: 455
        y: 474
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
            text: "Set weight #4"
            width: 134
            height: 22
            color: "#D9D9D9"
            x: 37
            y: 20
            font.pixelSize: 20
            font.family: "Archivo"
        }
    }

    Rectangle {
        width: 208
        height: 62
        radius: 4
        x: 455
        y: 568
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
            text: "Set weight #3"
            width: 134
            height: 22
            color: "#D9D9D9"
            x: 37
            y: 20
            font.pixelSize: 20
            font.family: "Archivo"
        }
    }

    Rectangle {
        width: 208
        height: 62
        radius: 4
        x: 695
        y: 192
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
            text: "Set weight #6"
            width: 134
            height: 22
            color: "#D9D9D9"
            x: 37
            y: 20
            font.pixelSize: 20
            font.family: "Archivo"
        }
    }

    Rectangle {
        width: 208
        height: 62
        radius: 4
        x: 695
        y: 286
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
            text: "Set weight #7"
            width: 134
            height: 22
            color: "#D9D9D9"
            x: 37
            y: 20
            font.pixelSize: 20
            font.family: "Archivo"
        }
    }

    Rectangle {
        width: 208
        height: 62
        radius: 4
        x: 695
        y: 380
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
            text: "Set weight #8"
            width: 134
            height: 22
            color: "#D9D9D9"
            x: 37
            y: 20
            font.pixelSize: 20
            font.family: "Archivo"
        }
    }

    Rectangle {
        width: 208
        height: 62
        radius: 4
        x: 695
        y: 474
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
            text: "Set weight #9"
            width: 134
            height: 22
            color: "#D9D9D9"
            x: 37
            y: 20
            font.pixelSize: 20
            font.family: "Archivo"
        }
    }

    Rectangle {
        width: 208
        height: 62
        radius: 4
        x: 695
        y: 568
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
            text: "Set weight #10"
            width: 134
            height: 22
            color: "#D9D9D9"
            x: 37
            y: 20
            font.pixelSize: 20
            font.family: "Archivo"
        }
    }

    Rectangle {
        width: 208
        height: 156
        radius: 4
        color: "white"
        x: 935
        y: 192
        layer.enabled: true
            layer.effect: DropShadow {
            horizontalOffset: 1
            verticalOffset: 1
            radius: 10
            samples: 16
            color: "#d3d3d3"
            }

        Text {
            text: "Average weight"
            width: 154
            height: 22
            x: 27
            y: 34
            color: "black"
            font.family: "Archivo"
            font.pixelSize: 20
        }

        Text {
            text: "747 g"
            width: 86
            height: 34
            x: 50
            y: 88
            color: "#4696FA"
            font.family: "Archivo"
            font.pixelSize: 20
        }
    }

    Button {
        background: Item{}

        Rectangle {
            color: "#4696FA"
            width: 208
            height: 62
            radius: 4
            x: 935
            y: 380

            Text {
                text: "Next"
                color: "white"
                width: 54
                height: 26
                x: 77
                y: 18
                font.family: "Archivo"
                font.pixelSize: 24
            }
        }

        Button {
            background: Item{}

            Rectangle {
                width: 120
                height: 41
                color: "#4696FA"
                x: 1127
                y: 25.5
                radius: 4

                Image {
                    source: "/home/mahnaz/akam/ui_aptinet/assets/question.png"
                    width: 16
                    height: 16
                    x: 12
                    y: 12.5
                }

                Text {
                    text: "Manual"
                    color: "white"
                    width: 58
                    height: 17
                    x: 38
                    y: 12
                    font.family:"Archivo"
                    font.pixelSize: 16
                }
            }
        }

        Button {
            background: Item{}

            Rectangle {
                width: 164
                height: 41
                color: "#F08C5A"
                x: 939
                y: 25.5
                radius: 4

                Image {
                    source: "/home/mahnaz/akam/ui_aptinet/assets/plus.png"
                    width: 12
                    height: 12
                    x: 12
                    y: 14.5
                }

                Text {
                    text: "Enter Barcode"
                    color: "white"
                    width: 114
                    height: 17
                    x: 34
                    y: 12
                    font.family: "Archivo"
                    font.pixelSize: 16
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



    

