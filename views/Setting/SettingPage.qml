import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.12
import "../Components"
import "../PopUps"
import KAST.Logic 1.0


Item {
    id: root
    visible: true
    width: 1280
    height: 800

    property Logic obj_LogicSetting


    Image {
        id: q
        source: "../../Assets/AuthenticationBackground.png"
        anchors.fill: parent
    }

    Row {
        spacing: 30
        anchors.horizontalCenter: parent.horizontalCenter

        Button {
            width: 128
            height: 160
            x: 166
            y: 312

            background: Rectangle {

                color: "white"

            }


            Image {
                source: "../../Assets/server.png"
                width: 64
                height: 64
                y: 30
                anchors.horizontalCenter: parent.horizontalCenter

            }

            Text {
                text: "Server"
                anchors.horizontalCenter: parent.horizontalCenter
                y: 124
                font.family: "Archivo"
                color: "gray"
                font.pixelSize: 18
            }

            onClicked: {
                stackview.push(serverDownloadUpload)
            }
        }

        Button {
            width: 128
            height: 160
            x: 330
            y: 312

            background: Rectangle {

                color: "white"

            }

            onClicked: {
                obj_LogicSetting.settingPage.gotoWifiSettings()
                stackview.push(wifi)
            }

            Image {
                source: "../../Assets/wifi.png"
                height: 64
                x: 25
                y: 30
                anchors.horizontalCenter: parent.horizontalCenter

            }

            Text {
                text: "Wi-Fi"
                anchors.horizontalCenter: parent.horizontalCenter
                y: 124
                color: "gray"
                font.pixelSize: 18
            }
        }

        Button {
            width: 128
            height: 160
            x: 494
            y: 312
            onClicked: {
                stackview.push(calibrate)
            }

            background: Rectangle {

                color: "white"

            }

            Image {
                source: "../../Assets/calibrate.png"
                width: 64
                height: 64
                y: 30
                anchors.horizontalCenter: parent.horizontalCenter

            }

            Text {
                text: "Calibrate"
                anchors.horizontalCenter: parent.horizontalCenter
                y: 124
                color: "gray"
                font.pixelSize: 18
            }
        }

        Button {
            width: 128
            height: 160
            x: 665
            y: 312
            onClicked: {
                stackview.push(deviceTest)
            }

            background: Rectangle {

                color: "white"

            }

            Image {
                source: "../../Assets/device.png"
                width: 64
                height: 64
                anchors.horizontalCenter: parent.horizontalCenter
                y: 30
            }

            Text {
                text: "Device Test"
                anchors.horizontalCenter: parent.horizontalCenter
                y: 124
                font.family: "Archivo"
                color: "gray"
                font.pixelSize: 18
            }
        }

        Button {
            width: 128
            height: 160
            x: 835
            y: 312
            background: Rectangle {

                color: "white"

            }
            onClicked: {
                obj_LogicSetting.settingPage.cart_infoClicked()
            }

            Image {
                source: "../../Assets/cartinfo.png"
                height: 64
                anchors.horizontalCenter: parent.horizontalCenter
                y: 30
            }

            Text {
                text: "Cart Info"
                anchors.horizontalCenter: parent.horizontalCenter
                y: 124
                color: "gray"
                font.pixelSize: 18
            }
        }
    }

    Button {
        width: 76
        height: 76
        background: Rectangle {
            color: "white"
        }
        Image {
            source: "../../Assets/turnOff.png"
            width: 76
            height: 76
            x: 684
            y: 607
        }

        Text {
            text: "Turn Off"
            width: 59
            height: 17
            color: "#1D1D1D"
            x: 692.5
            y: 703
            font.pixelSize: 16
        }
        onClicked: {
            obj_LogicSetting.turnoff()
        }
    }

    Button {
        width: 76
        height: 76
        background: Rectangle {
            color: "white"
        }
        Image {
            source: "../../Assets/restart.png"
            width: 76
            height: 76
            x: 520.5
            y: 607
        }

        Text {
            text: "Restart Device"
            width: 109
            height: 17
            color: "#6D6D6D"
            x: 504
            y: 703
            font.pixelSize: 16
        }
        onClicked: {
            obj_LogicSetting.turnoff()
            cameraProvider.stop()
        }
    }

    Component {
        id: wifi
        Wifi{
            setting_objWifi: obj_LogicSetting
        }
    }

    Component {
        id:calibrate
        Calibrate{
            obj_LogicCalibrate: obj_LogicSetting
        }
    }


    Component {
        id: cartinfo
        CartInfo{
            obj_LogicContainer: obj_LogicSetting
        }
    }

    Component {
        id: deviceTest
        MenuTest{}
    }

    Component{
        id:serverDownloadUpload
        Server{
            obj_LogicServer: obj_LogicSetting
        }
    }

    TopNav{
        backvisible: true
        onBackClicked: {
            cameraProvider.stop()
        }

    }
    Connections{
        target:obj_LogicSetting.settingPage
        function onCartInfoClickedSignal(){
            stackview.push(cartinfo)
        }
    }
}





