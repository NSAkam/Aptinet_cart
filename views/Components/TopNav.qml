import QtQuick 2.15

Item {
    id:root
    signal backClicked();

    property bool backvisible: false
    width: parent.width
    height: 92
    x:0
    y:0
    Rectangle{
        anchors.fill: parent
        color: "white"
        Image {
            source: "../Assets/AptinetLogo.png"
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
        }
        Image {
            id: btn_back
            source: "../Assets/back.png"
            anchors.left: parent.left
            anchors.leftMargin: 10
            visible: backvisible
            anchors.verticalCenter: parent.verticalCenter
            MouseArea{
                anchors.fill: parent
                onClicked: {
                    root.backClicked()
                }
            }
        }
    }
}
