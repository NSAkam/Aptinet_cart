import QtQuick 2.15
import QtQuick.Window 2.12
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0
import "../Utiles"

Rectangle {
    id:container

    property string text: "value"
    property string imagesource: "../../Assets/server.svg"
    property string buttonBackColor: "#F2C335"

    width: 114
    height: 145
    color: "transparent"

    ViewSettings{
        id:viewset
    }
    Rectangle{
        id:btnContainer
        anchors.top: parent.top
        anchors.horizontalCenter: parent.horizontalCenter
        width: 96
        height: 96
        color: buttonBackColor
        opacity: 0.3
        radius: 15
    }
    Image {
        anchors.horizontalCenter: btnContainer.horizontalCenter
        anchors.verticalCenter: btnContainer.verticalCenter
        source: parent.imagesource
    }


    Label{
        anchors.bottom: parent.bottom
        text:parent.text
        anchors.horizontalCenter: parent.horizontalCenter
        font.family: viewset.danaFuNumFont
        font.pixelSize: 16
    }
}
