import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.12
import "../Components"




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
                scannerPopUp = true
            }

            Image {
                source: "../../Assets/scanner.png"
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
                havePopUp = true
            }

            background: Rectangle {

                color: "white"

            }

            Image {
                source: "../../Assets/lights.png"
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
                source: "../../Assets/sound.png"
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
        color: "black"
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
        color: "black"
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
        color: "black"
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







