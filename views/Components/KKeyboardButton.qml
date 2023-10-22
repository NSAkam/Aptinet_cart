import QtQuick 2.15
import QtQuick.Controls 2.15



RoundButton {
    id: control
    radius: width
    width: 70
    height: 70
    font.pixelSize: 24

    property string color: "#7D7D7D"

    contentItem: Text {
            text: control.text
            font: control.font
            opacity: enabled ? 1.0 : 0.3
            color: control.down ? "white" : "white"
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            elide: Text.ElideRight
        }
    background: Rectangle {
            implicitWidth: 50
            implicitHeight: 50
            radius: width
            color: parent.color
        }
}
