import QtQuick 2.12
import QtMultimedia 5.12

Item{
    id:cameraWindow
    anchors.fill: parent
    signal closed
    property alias theID: camera.deviceId
    property alias backgroundColor: background.color
    property alias orientation: vo.orientation

    Rectangle{
        id: background
        anchors.fill: parent
        color: "blue"
    }

    Camera{
        id:camera

        imageProcessing {
            whiteBalanceMode: Camera.WhiteBalanceTungsten
            contrast: 0.66
            saturation: -0.5
        }    }

    VideoOutput{
        id: vo
        z:99
        source: camera
        anchors.fill: parent
    }
}
