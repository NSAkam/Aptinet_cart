import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import QtQuick.Window 2.0
import "../Components"
import "../Containers"
import "../Utiles"

Popup {
    property alias messageText: notiftext.text
    property bool showManualBarcode: false

    id: root
    width: 1280
    height: 800
    modal: true
    focus: false
    onOpened: {
        closetimer.start();

    }
    background:
        Rectangle {
        id:rectContainer
        anchors.fill: parent
        color: "#191641"
        opacity: 0.5
    }
    Timer {
        id: closetimer
        interval: 5000
        onTriggered:{
            root.close()
            console.log("asdasd")
        }
        repeat: false
        running: true
    }

    Rectangle {
        x: 818 + 390
        y: 32
        radius: 4
        color: "white"
        width: 40
        height: 40

        Image {
            source: "../../Assets/Bell.png"
            width: 18
            height: 20
            anchors.centerIn: parent
        }
    }


    KButton {
        visible:showManualBarcode
        x: 630 + 390
        y: 32
        borderRadius: 4
        width: 164
        height: 40

        Text {
            text: "+  Enter Barcode"
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            font.pixelSize: 16
            font.weight: Font.DemiBold
            color: "white"
        }
    }

    Rectangle {
        id: notifrect
        width: 678 + notiftext.width/6
        height: 252
        radius: 4
        y: 274
        //        x: 106 + 390/2
        anchors.horizontalCenter: parent.horizontalCenter

        Image {
            source: "../../Assets/popupwarning.png"
            width: 99
            height: 88
            y: 48
            anchors.horizontalCenter: parent.horizontalCenter
        }

        Text {
            id: notiftext
            text: "Please put the product you scanned into the cart!"
            anchors.horizontalCenter: parent.horizontalCenter
            horizontalAlignment: Text.AlignHCenter
            y: 168
            color: "black"
            font.pixelSize: 24
            font.weight: Font.DemiBold
            //            font.letterSpacing: 0.8
        }
    }

}
