import QtQuick 2.3
import QtGraphicalEffects 1.0
import "../Utiles"



Rectangle {
    id: root;
    width: 175;
    height: 40;
    radius: 5;


    ViewSettings{
        id:viewset
    }

    property alias mouseField: mouseArea;


    MouseArea {
        id: mouseArea;
        anchors.fill: parent;

        onClicked: {

        }
    }
    property int borderwidth: 1
    property string color: "white";
    property string text: "Primary";
    property string textColor: viewset.primaryColor;
    property int pixelSize: 24;
    property string imagesource: ""
    property int imagewidth: 15;
    property int imageheight: 18;
    property alias btn_color: primaryButton.color


    Rectangle {
        id: primaryButton;
        anchors.fill: parent;
        color: root.color;
        radius: root.radius;
        border.color: viewset.primaryColor
        border.width: borderwidth

        Text {
            id: buttonText;
            text: root.text;
            color: root.textColor;
            font {
                pixelSize: root.pixelSize;
            }
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter

            //y:parent.height / 2 - 8
        }
    }
}
