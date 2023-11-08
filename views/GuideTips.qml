import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import QtQuick.Window 2.0
import QtQuick.Controls.Styles 1.4
import QtGraphicalEffects 1.0
import "Components"
import "Containers"
import "Utiles" as Util
import "PopUps"


Item {
    id: root
    width: 1280
    height: 800

    Image {
        source: "../Assets/AuthenticationBackground.png"
        anchors.fill: parent
    }

    Rectangle{
        width: parent.width
        height: 92
        x:0
        y:0
        color: "#F05A28"

        Text {
            text: "Required Tips"
            color: "white"
            font.family: "Archivo"
            font.pixelSize: 32
            font.bold: true
            x: 526
            y: 28
        }
    }

    Rectangle {
        width: 96
        height: 96
        color: "white"
        x: 170
        y: 224

        Image {
            source: "../Assets/blankbasket.png"
            width: 48
            height: 48
            x: 24
            y: 24
        }
    }

    Rectangle {
        width: 96
        height: 96
        color: "white"
        x: 170
        y: 352

        Image {
            source: "../Assets/basket2.png"
            width: 48
            height: 48
            x: 24
            y: 24
        }
    }

    Rectangle {
        width: 96
        height: 96
        color: "white"
        x: 170
        y: 480

        Image {
            source: "../Assets/basket3.png"
            width: 48
            height: 48
            x: 24
            y: 24
        }
    }

}
