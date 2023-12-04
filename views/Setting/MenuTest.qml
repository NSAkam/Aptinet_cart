import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.12
import "../Components"
import "../PopUps"




Item {
    id: root
    visible: true
    width: 1280
    height: 800

    property bool havePopUp : false
    property bool scannerPopUp : false
    property bool weightsensorPopup : false

    Image {
        id: q
        source: "../../Assets/AuthenticationBackground.png"
        anchors.fill: parent
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
                weightsensorPopup = true

            }


            Image {
                source: "../../Assets/weightsensor.png"
                width: 64
                height: 64
                anchors.horizontalCenter: parent.horizontalCenter
                y: 30
            }


            Text {
                text: "Weight\nSensor"
                anchors.horizontalCenter: parent.horizontalCenter
                y: 110
                font.family: "Archivo"
                color: "#6D6D6D"
                font.pixelSize: 16
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
                scannerPopUp = true
            }

            Image {
                source: "../../Assets/scanner.png"
                height: 64
                anchors.horizontalCenter: parent.horizontalCenter
                y: 30
            }

            Text {
                text: "Scanner"
                anchors.horizontalCenter: parent.horizontalCenter
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
                havePopUp = true
            }

            background: Rectangle {

                color: "white"

            }

            Image {
                source: "../../Assets/lights.png"
                width: 64
                height: 64
                anchors.horizontalCenter: parent.horizontalCenter
                y: 30
            }

            Text {
                text: "Lights"
                anchors.horizontalCenter: parent.horizontalCenter
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
                source: "../../Assets/sound.png"
                width: 72
                height: 60
                anchors.horizontalCenter: parent.horizontalCenter
                y: 30
            }

            Text {
                text: "Sound"
                anchors.horizontalCenter: parent.horizontalCenter
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

    TopNav{
        backvisible: true
        onBackClicked: {
            if(parent.havePopUp ===  true)
            {
                serverPopup.close()
                b.visible = false
            }
            else{
                stackview.pop()
            }
            if(parent.scannerPopUp === true)
            {
                sensorPopup.close()
                w.visible = false
            }
            else{
                stackview.pop()
            }
            if(parent.weightsensorPopup === true)
            {
                weightsensorPopup.close()
                s.visible = false
            }
            else{
                stackview.pop()
            }
        }
    }
}

// }







