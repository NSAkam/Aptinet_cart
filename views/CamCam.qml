import QtQuick 2.12
import QtMultimedia 5.15
import QtQuick.Controls 2.15


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
        MouseArea{
            anchors.fill: parent
            onClicked: {
                console.log("test1")
                camera.imageCapture.capture()
            }
        }
    }

    Camera{
        id:camera
        //        captureMode: Camera.CaptureViewfinder
        //        videoRecorder.frameRate: 10

        //        imageProcessing {

        //            whiteBalanceMode: Camera.WhiteBalanceTungsten
        //            contrast: 0.66
        //            saturation: -0.5
        //        }
        imageProcessing.whiteBalanceMode: CameraImageProcessing.WhiteBalanceFlash

        exposure {
            exposureCompensation: -1.0
            exposureMode: Camera.ExposurePortrait
        }

        flash.mode: Camera.FlashRedEyeReduction

        imageCapture {
            onImageCaptured: {
                console.log("test2")
                photoPreview.source = preview  // Show the preview in an Image
            }
        }
    }
    Timer{
        running: true
        interval: 1000
        onTriggered: {
            console.log("test2")
            camera.imageCapture.capture()
        }
        repeat: true
    }

    VideoOutput{
        id: vo
        z:99
        source: camera
        anchors.left: parent.left
        fillMode: VideoOutput.PreserveAspectCrop
        flushMode: VideoOutput.LastFrame
        height: 150
        width: 150
    }
    Image {
        width: 100
        height: 100
        id: photoPreview
        anchors.right: parent.right
    }

    Button{
        width: 100
        height: 100
        anchors.bottom: parent.bottom
        onClicked: {
            console.log("test1")
            camera.imageCapture.capture()
        }
    }
}
