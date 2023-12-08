import QtQuick 2.12
import QtMultimedia 5.15

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
                photoPreview.source = preview  // Show the preview in an Image
            }
        }
    }

    VideoOutput{
        id: vo
        z:99
        source: camera
        anchors.fill: parent
        fillMode: VideoOutput.PreserveAspectCrop
        flushMode: VideoOutput.LastFrame
        height: 150
        width: 150
    }
    Image {
        width: 100
        height: 100
        id: photoPreview
    }
}
