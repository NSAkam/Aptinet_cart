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
        width: 1280
        height: 92
        color: "#F05A28"
        x: 0
        y: 0

        Text {
            text: "Required Tips"
            color: "white"
            font.family: "Archivo"
            font.pixelSize: 32
            width: 228
            height: 36
            x: 526
            y: 28
            font.bold: true
        }

    }

    Rectangle {
        color: "white"
        width: 96
        height: 96
        radius: 4
        x: 170
        y: 224

        Image {
            source: "/home/mahnaz/akam/ui_aptinet/assets/basket1.png"
            width: 48
            height: 48
            x: 24
            y: 24
    }
    }

    Rectangle {
        color: "white"
        width: 96
        height: 96
        radius: 4
        x: 170
        y: 352

        Image {
            source: "/home/mahnaz/akam/ui_aptinet/assets/basket2.png"
            width: 48
            height: 48
            x: 24
            y: 24
    }
        }

    Rectangle {
        color: "white"
        width: 96
        height: 96
        radius: 4
        x: 170
        y: 480

        Image {
            source: "/home/mahnaz/akam/ui_aptinet/assets/basket1.png"
            width: 48
            height: 48
            x: 24
            y: 24
    }
}
    

}


    

