import QtQuick 2.15
import QtQuick.Window 2.12
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0
import "../Utiles"

Button {
    width: 60
    height: 60
    font.pixelSize: 40

    property int textY:36
    contentItem: Label {
        text: parent.text
        font.bold: false
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        elide: Text.ElideRight
        color: "#9D9D9D"
        font.pixelSize: parent.font.pixelSize
    }

    background: Rectangle {
        id:primaryButton
        color:parent.pressed ? "#F2C335" : "White"
        radius: 0
    }

}
