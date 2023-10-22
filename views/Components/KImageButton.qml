import QtQuick 2.3
import QtGraphicalEffects 1.0
import "../Utiles"



Rectangle {
    id: root;
    width: 175;
    height: 40;
    radius: 10;
    ViewSettings{
        id:viewset
    }


    property string color: viewset.primaryColor;
    property string pressColor: viewset.focusColor;
    property string highlightColor: "#2979ff";
    property string text: "Primary Button";
    property string textColor: "white";
    property int pixelSize: 20;
    property string imagesource: ""
    property Image imgBtn:img_btn
    property int imagewidth: 15;
    property int imageheight: 18;


    Rectangle {
        id: primaryButton;
        anchors.fill: parent;
        color: root.color;
        radius: root.radius;

        Text {
            id: buttonText;
            text: root.text;
            color: root.textColor;
            font {
                pixelSize: root.pixelSize;
                family: viewset.danaFuNumFont
                bold: true
            }
            x:imagesource=="" ? (parent.width / 2) - (width / 2) : 66
            y:9

        }
        Image {
            id:img_btn
            anchors.verticalCenter: parent.verticalCenter
            anchors.rightMargin: 20
            source: imagesource
            height: imagewidth
            width: imageheight
            fillMode: Image.PreserveAspectFit
            antialiasing: true
            x:30
            y:16
        }

        Behavior on color {
            PropertyAnimation {}
        }
    }
}
