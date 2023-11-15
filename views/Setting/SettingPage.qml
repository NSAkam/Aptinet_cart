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


    Image {
        id: q
        source: "../../Assets/AuthenticationBackground.png"
        anchors.fill: parent
    }





    Row {
        spacing: 30
        x: 166
        y: 400
        anchors {
            top: parent.top
            horizontalCenter: parent.horizontalCenter
            topMargin:300
        }
    }

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
            x: 34
            y: 30
        }

        Text {
            text: "Server"
            width: 70
            height: 20
            x: 42
            y: 124
            font.family: "Archivo"
            color: "gray"
            font.pixelSize: 18
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
            stackview.push(wifi)
        }

        Image {
            source: "../../Assets/wifi.png"
            height: 64
            x: 25
            y: 30
        }

        Text {
            text: "Wi-Fi"
            width: 56
            height: 20
            x: 45
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
            x: 34
            y: 30
        }

        Text {
            text: "Calibrate"
            width: 56
            height: 20
            x: 33
            y: 124
            color: "gray"
            font.pixelSize: 18
        }
    }

    Button {
        width: 128
        height: 160
        x: 658
        y: 312
        onClicked: {
            stackview.push(dataEntry)
        }

        background: Rectangle {

            color: "white"

        }

        Image {
            source: "../../Assets/data.png"
            width: 64
            height: 64
            y: 30
            anchors.horizontalCenter: parent.horizontalCenter
        }

        Text {
            text: "Data Entry"
            y: 124
            color: "gray"
            font.pixelSize: 18
            anchors.horizontalCenter: parent.horizontalCenter
        }
    }

    Button {
        width: 128
        height: 160
        x: 822
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
            x: 34
            y: 30
        }

        Text {
            text: "Device Test"
            width: 70
            height: 20
            x: 30
            y: 124
            font.family: "Archivo"
            color: "gray"
            font.pixelSize: 18
        }
    }

    Button {
        width: 128
        height: 160
        x: 986
        y: 312
        background: Rectangle {

            color: "white"

        }
        onClicked: {
            stackview.push(cartinfo)
        }

        Image {
            source: "../../Assets/cartinfo.png"
            height: 64
            x: 32
            y: 30
        }

        Text {
            text: "Cart Info"
            width: 56
            height: 20
            x: 38
            y: 124
            color: "gray"
            font.pixelSize: 18
        }
    }
    // }

    Button {
        width: 76
        height: 76
        background: Rectangle {
            color: "white"
        }
        Image {
            source: "../../Assets/turnoff.png"
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
    }

    Component {
        id: wifi
        Wifi{}
    }

    Component {
        id:calibrate
        Calibrate{}
    }

    Component {
        id: dataEntry
        DataEntry1{}
    }

    Component {
        id: cartinfo
        CartInfo{}
    }

    Component {
        id: deviceTest
        MenuTest{}
    }

    TopNav{
        backvisible: true
        onBackClicked: {
            stackview.pop()
        }

    }
}





