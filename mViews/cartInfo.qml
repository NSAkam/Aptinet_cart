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
                onClicked: {
                    StackView.pop();
                }
            }

        }

        Rectangle {
        width: 672
        height: 86
        color: "white"
        x: 304
        y: 272
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
            width: 160
            height: 22
            x: 24
            y: 32
            color: "#1D1D1D"
            font.pixelSize: 20
            font.family: "Archivo"
        }

        Text {
            text: "2.3"
            width: 30
            height: 22
            x: 502
            y: 32
            color: "#6D6D6D"
            font.pixelSize: 20
            font.family: "Archivo"
        }

        Button {
            width: 92
            height: 38
            x: 556
            y: 24
            background: Rectangle {
                color: "white"
                radius: 2
                border.color: "#4696FA"
                border.width: 1
                

                Text {
                    text: "Update"
                    width: 68
                    height: 22
                    x: 12
                    y: 8
                    color: "#4696FA"
                    font.pixelSize: 20
                }
        }
    }
}

    Rectangle {
        width: 672
        height: 1
        x: 303
        y: 358
        color: "#9D9D9D"
    }

    Rectangle {
        width: 672
        height: 86
        color: "white"
        x: 304
        y: 360
        layer.enabled: true
            layer.effect: DropShadow {
            horizontalOffset: 1
            verticalOffset: 1
            radius: 10
            samples: 16
            color: "#d3d3d3"
        }

        Text {
            text: "Unit"
            width: 39
            height: 22
            x: 24
            y: 32
            color: "#1D1D1D"
            font.pixelSize: 20
        }

        Text {
            text: "Kg"
            width: 25
            height: 22
            x: 502
            y: 32
            color: "#6D6D6D"
            font.pixelSize: 20
        }

        Button {
            width: 92
            height: 38
            x: 556
            y: 24
            onClicked: {
                toggleRectangles();
            }
            background: Rectangle {
                color: "white"
                radius: 2
                border.color: "#4696FA"
                border.width: 1
                

                Text {
                    text: "Change"
                    width: 68
                    height: 22
                    x: 12
                    y: 8
                    color: "#4696FA"
                    font.pixelSize: 20
                }
        }
    }
    }

    Rectangle {
        width: 672
        height: 1
        x: 303
        y: 446
        color: "#9D9D9D"
    }

    Rectangle {
        width: 672
        height: 86
        color: "white"
        x: 304
        y: 448
        layer.enabled: true
            layer.effect: DropShadow {
            horizontalOffset: 1
            verticalOffset: 1
            radius: 10
            samples: 16
            color: "#d3d3d3"
        }

        Text {
            text: "Calibration Date"
            width: 152
            height: 22
            x: 24
            y: 32
            color: "#1D1D1D"
            font.pixelSize: 20
        }

        Text {
            text: "2023/05/08"
            width: 107
            height: 22
            x: 433
            y: 32
            color: "#6D6D6D"
            font.pixelSize: 20
        }

        Text {
                text: "Expired"
                width: 73
                height: 22
                x: 567
                y: 32
                color: "#F08C5A"
                font.pixelSize: 20
            }
    }

    Rectangle {
        id: rectangle1
        radius: 2
        width: 64
        height: 60
        x: 1000
        y: 300
        color: "#4696FA"
        visible: false

        layer.enabled: true
            layer.effect: DropShadow {
            horizontalOffset: 1
            verticalOffset: 1
            radius: 10
            samples: 16
            color: "#d3d3d3"
        }

        Text {
            text: "gr"
            font.pixelSize: 24
            color: "white"
            x: 20
            y: 16
        }
    }

    Rectangle {
        id: separator1
        width: 64
        height: 1
        x: 1000
        y: 360
        color: "#9D9D9D"
        visible: false

    }

    Rectangle {
        id: rectangle2
        radius: 2
        width: 64
        height: 60
        x: 1000
        y: 361
        color: "white"
        visible: false
        layer.enabled: true
            layer.effect: DropShadow {
            horizontalOffset: 1
            verticalOffset: 1
            radius: 10
            samples: 16
            color: "#d3d3d3"
        }

        Text {
            text: "Kg"
            font.pixelSize: 24
            color: "#9D9D9D"
            x: 20
            y: 16
        }
    }

    Rectangle {
        id: separator2
        width: 64
        height: 1
        x: 1000
        y: 420
        color: "#9D9D9D"
        visible: false
    }

    Rectangle {
        id: rectangle3
        radius: 2
        width: 64
        height: 60
        x: 1000
        y: 421
        color: "white"
        visible: false
        layer.enabled: true
            layer.effect: DropShadow {
            horizontalOffset: 1
            verticalOffset: 1
            radius: 10
            samples: 16
            color: "#d3d3d3"
        }

        Text {
            text: "lb"
            font.pixelSize: 24
            color: "#9D9D9D"
            x: 20
            y: 16
        }
    }

    function toggleRectangles() {
            rectangle1.visible = !rectangle1.visible;
            separator1.visible = !separator1.visible;
            rectangle2.visible = !rectangle2.visible;
            separator2.visible = !separator2.visible;
            rectangle3.visible = !rectangle3.visible;
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

    



    

