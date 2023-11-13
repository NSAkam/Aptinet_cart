import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.12
import QtQuick.Window 2.14






Item{
    id: root
    visible: true
    width: 1280
    height: 800


    Image {     
        id: q
        source: "../../Assets/AuthenticationBackground.png"
        anchors.fill: parent
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



    

