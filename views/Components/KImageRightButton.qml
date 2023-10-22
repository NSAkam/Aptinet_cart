import QtQuick 2.3
import QtGraphicalEffects 1.0



Rectangle {
    id: root;
    width: 175;
    height: 40;
    radius: 10;

    property alias mouseField: mouseArea;


    MouseArea {
        id: mouseArea;
        anchors.fill: parent;

        onClicked: {
            if(animate == true)
            {
                clickanimation.start()
            }
        }
    }

    property string color: viewset.primaryColor;
    property string pressColor: viewset.focusColor;
    property string highlightColor: "#2979ff";
    property string text: "Button";
    property string textColor: "white";
    property int pixelSize: 20;
    property string imagesource: ""
    property Image imgBtn:img_btn
    property int imagewidth: 15;
    property int imageheight: 18;
    property int imageX:10
    property int imageY: 13
    property int textX:16
    property int textY: 12
    property bool animate: true



    Rectangle {
        id: primaryButton;
        anchors.fill: parent;
        color: root.color;
        radius: root.radius;


        Image {
            id:img_btn
            anchors.verticalCenter: parent.verticalCenter
            anchors.rightMargin: 20
            source: imagesource
            height: imagewidth
            width: imageheight
            fillMode: Image.PreserveAspectFit
            antialiasing: true
            x:imageX
            y:imageY
        }

        Text {
            id: buttonText;
            anchors.right: img_btn.left
            anchors.rightMargin: 10
            text: root.text;
            color: root.textColor;
            font {
                pixelSize: root.pixelSize;
                family: viewset.danaFuNumFont
                bold: false
            }
            x:textX
            y:textY

        }

        Behavior on color {
            PropertyAnimation {}
        }
    }
    SequentialAnimation {
        id: clickanimation
        ParallelAnimation{
            // Expand the button
            PropertyAnimation {
                target: root
                property: "width"
                to: root.width - 5
                duration: 25
                easing.type: Easing.Linear
            }

            PropertyAnimation {
                target: primaryButton
                property: "color"
                from: viewset.primaryColor
                to: viewset.focusColor
                duration: 300
            }
        }
        ParallelAnimation
        {
            PropertyAnimation {
                target: root
                property: "width"
                to: root.width
                duration: 100
                easing.type: Easing.Linear
            }
            PropertyAnimation {
                target: primaryButton
                property: "color"
                from: viewset.focusColor
                to: viewset.primaryColor
                duration: 600
            }
        }
    }
}
