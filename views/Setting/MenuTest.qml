import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.12
import QtQuick.Window 2.15
import "../Components"
import "../PopUps"
import KAST.Logic 1.0




Item {
    id: root
    visible: true
    width: 1280
    height: 800

    property Logic obj_LogicMenuTest

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


            }


            Image {
                source: "../../Assets/weightsensor.png"
                width: 64
                height: 64
                anchors.horizontalCenter: parent.horizontalCenter
                y: 30
            }


            Text {
                text: obj_LogicMenuTest.lang.btn_Weight_Sensor
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
            }

            Image {
                source: "../../Assets/scanner.png"
                height: 64
                anchors.horizontalCenter: parent.horizontalCenter
                y: 30
            }

            Text {
                text: obj_LogicMenuTest.lang.btn_Scanner
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
                text: obj_LogicMenuTest.lang.btn_Lights
                anchors.horizontalCenter: parent.horizontalCenter
                y: 124
                color: "#6D6D6D"
                font.pixelSize: 18
            }
            MouseArea{
                anchors.fill: parent
                onClicked: {
                    obj_LogicMenuTest.settingPage.light_testClicked()
                }
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
                text: obj_LogicMenuTest.lang.btn_Sound
                anchors.horizontalCenter: parent.horizontalCenter
                y: 124
                color: "#6D6D6D"
                font.pixelSize: 18

            }
            onClicked: {
                obj_LogicMenuTest.settingPage.sound_testClicked()
            }
        }
    }


    ScannerPopup {
        id: sensorPopup
        obj_LogicScannerPopUp: obj_LogicMenuTest
    }

    WeightsensorPopup {
        id: weightsesnsorPopup
        obj_LogicWeightSensorPopUp: obj_LogicMenuTest
    }

    TopNav{
        backvisible: true
        onBackClicked: {
                stackview.pop()
        }
    }
}








