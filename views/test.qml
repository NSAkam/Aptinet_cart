import QtQuick 2.12
import QtMultimedia 5.12
import QtQuick.Window 2.12

Window {
visible: true
width: 1280
height: 800
title: qsTr("Hello World")
Item{
id: cameraLeft
anchors.left: parent.left
anchors.top: parent.top
anchors.bottom: parent.bottom

        CamCam{
            //theID: QtMultimedia.availableCameras[0].deviceId
            backgroundColor: "red"
        }
    }

// Item{
//         id: cameraRight
//         anchors.right: parent.right
//         anchors.top: parent.top
//         anchors.left: swipeView.right
//         anchors.bottom: parent.bottom

//         CamCam{
//             theID: QtMultimedia.availableCameras[1].deviceId
//             backgroundColor: "blue"
//         }
//     }

}

