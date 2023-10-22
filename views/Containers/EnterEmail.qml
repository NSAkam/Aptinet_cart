import QtQuick 2.15
import QtGraphicalEffects 1.15
import "../Utiles" as Util
import "../Components"

Item {

    Text {
        text: qsTr("Please enter your Email or\n Phone Number to get a receipt")
        font.pixelSize: 24
        font.bold: true
        horizontalAlignment: Text.AlignHCenter
        x: 18
        y: 90
    }

    Rectangle {
        id: emailrect
        width: 392
        height: 56
        y: 110 + 90
        x: 10
        color: "white"

        Text {
            text: qsTr("Email / Phone Number")
            color: "#BDBDBD"
            font.pixelSize: 20
            x: 24
            y: 17
        }
    }

    DropShadow {
        anchors.fill: emailrect
        cached: true
        horizontalOffset: 0
        verticalOffset: 5
        radius: 16.0
        y: 5
        samples: 30
        color: "#50000000"
        smooth: true
        source: emailrect
        visible: shadow?true:false

    }

}
