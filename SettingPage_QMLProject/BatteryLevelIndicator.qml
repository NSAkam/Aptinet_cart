import QtQuick 2.12
import QtQuick.Controls 2.15



Item {

    property real batterylevel: 0
    property real margin: 2

    x: 32
    y: 32

    Component.onCompleted: console.log(progressrect.width)


    ProgressBar {
        implicitWidth: 48
        implicitHeight: 26.67
        from: 0.2
        to: 1
        indeterminate: false
        //            anchors.fill: batteryimage
        value: 0.5
        contentItem:
            Image {
            id: batteryimage
            source: "Resources/battery.png"
            width: 48
            height: 26.67
            opacity: 1

            Rectangle {
                id: progressrect
                width: (batteryimage.width - 0.15*batteryimage.width) * (1-batterylevel) /*- 2 * margin*/
                height: batteryimage.height - 2 * margin
                color: "white"
                x: margin
                y: margin
                radius: 2
            }

        }

    }

    onBatterylevelChanged: {
        ProgressBar.value = batterylevel

    }


}


//Item {

//    property real batterylevel: 0.8
//    property real margin: 2

//    x: 32
//    y: 32


//    ProgressBar {
//        implicitWidth: 48
//        implicitHeight: 26.67
//        from: 0.2
//        to: 1
//        indeterminate: false
//        //            anchors.fill: batteryimage
//        value: 0.5
//        contentItem:
//            Image {
//            id: batteryimage
//            source: "Resources/battery.png"
//            width: 48
//            height: 26.67
//            opacity: 60

//            Rectangle {
//                id: progressrect
////                width: (batteryimage.width-2) * value
////                height: (batteryimage.height-2)
//                width: 21
//                height: 23
//                color: "white"
//                x: margin
//                y: margin
//                radius: 2
//            }

//        }

//    }

//    onBatterylevelChanged: {
//        ProgressBar.value = batterylevel
//    }

//}

//Item {
//    x: 32
//    y: 32

//    ProgressBar {
//        implicitWidth: 48
//        implicitHeight: 26.67
//        from: 0.2
//        to: 1
//        indeterminate: false
//        //            anchors.fill: batteryimage
//        value: 0.01
//        contentItem:
//            Image {
//            id: batteryimage
//            source: "Resources/battery.png"
//            width: 48
//            height: 26.67
//            opacity: 60

//        }

//    }

//}

//Item {

//    Image {
//        id: batteryimage
//        source: "Resources/battery.png"
//        x: 32
//        y: 32
//        width: 48
//        height: 26.67
//        opacity: 60

//        ProgressBar {
//            implicitWidth: batteryimage.width
//            implicitHeight: batteryimage.height
//            from: 0.2
//            to: 1
//            indeterminate: false
////            anchors.fill: batteryimage
//            value: 0.01
//            contentItem: batteryimage

//        }

//    }

//}
