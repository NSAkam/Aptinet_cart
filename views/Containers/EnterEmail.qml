import QtQuick 2.15
import QtGraphicalEffects 1.15
import "../Utiles" as Util
import "../Components"

Item {
    id: root
    signal continueClicked()


    Text {
        text: qsTr("Please enter your Email or\n Phone Number to get a receipt")
        font.pixelSize: 24
        font.bold: true
        horizontalAlignment: Text.AlignHCenter
        x: 15
        y: 24
    }

    Rectangle {
        id: emailrect
        width: 392
        height: 56
        y: 128
        x: 0.5
        color: "white"

        Text {
            text: qsTr("Email / Phone Number")
            color: "#BDBDBD"
            font.pixelSize: 20
            x: 24
            y: 17
        }
    }

    KButton {
        text: "Continue with Aptinet Card"
        x: 0.5
        y: 200
        btn_width: 392
        btn_height: 56
        borderRadius: 4
        btn_color: viewset.primaryColor

        MouseArea {
            anchors.fill: parent
            onClicked: {
                console.log("Akbar")
                root.continueClicked()
            }
        }
    }

    DropShadow {
        anchors.fill: emailrect
        cached: true
        horizontalOffset: 0
        verticalOffset: 5
        radius: 5.0
        y: 5
        samples: 10
        color: "#0000000A"
        smooth: true
        source: emailrect
        visible: shadow?true:false

    }

}
