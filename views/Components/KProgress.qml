import QtQuick 2.12
import QtGraphicalEffects 1.0

import "."

Item {
    id: kprogress
    transformOrigin: Item.Center

    property var metaData : ["from", "to", "value",
        "reverse",
        "fromAngle", "toAngle",
        "lineWidth", "fontSize",
        "kprogressBackgroundColor", "kprogressColor",
        "title", "titleFont", "titleFontSize", "titleFontColor"]

    //value parameters
    property double from:0
    property double value: 50
    property double to: 100

    //progress from right to left
    property bool reverse: false

    //progress circle angle
    property double fromAngle: Math.PI * 0.5
    property double toAngle: Math.PI * 3

    property int lineWidth: height / 10
    property int fontSize: height / 7

    property color kprogressBackgroundColor: "#F8C6AD"
    property color kprogressColor: "#ff6a00"

    property string title: "0"
    property alias titleFont: labelTitle.font.family
    property alias titleFontSize: labelTitle.font.pointSize
    property alias titleFontColor: labelTitle.color

    function update(value) {
        //        shadow.radius =14- value/7
        //        shadow1.radius =18- value/7
        kprogress.value = value
        canvas.requestPaint()
        background.requestPaint()
        labelTitle.text = value.toFixed(0);

    }

    Text {
        id: labelTitle
        y:15
        text: kprogress.title
        visible: true
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        font.pixelSize: 32
        font.family: viewset.danaFuNumBoldFont
        font.bold: true
        color: viewset.primaryColor
    }


    Canvas {
        id: background
        width: parent.height
        height: parent.height
        antialiasing: true

        property int radius: background.width/2

        onPaint: {



            var centreX = background.width / 2.0;
            var centreY = background.height / 2.0;

            var ctx = background.getContext('2d');
            ctx.strokeStyle = kprogress.kprogressBackgroundColor;
            ctx.lineWidth = 15;
            ctx.lineCap = "round"
            ctx.beginPath();
            ctx.clearRect(0, 0, background.width, background.height);
            ctx.arc(centreX, centreY, radius - kprogress.lineWidth, kprogress.fromAngle, kprogress.toAngle, false);
            ctx.stroke();
        }
    }

    Canvas {
        id:canvas
        width: parent.height
        height: parent.height
        antialiasing: true

        property double step: kprogress.value / (kprogress.to - kprogress.from) * (kprogress.toAngle - kprogress.fromAngle)
        property int radius: height/2



        onPaint: {
            var centreX = canvas.width / 2.0;
            var centreY = canvas.height / 2.0;

            var ctx = canvas.getContext('2d');
            ctx.strokeStyle = kprogress.kprogressColor;
            ctx.lineWidth = 15;
            ctx.beginPath();
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            if (kprogress.reverse) {
                ctx.arc(centreX, centreY, radius - kprogress.lineWidth, kprogress.toAngle, kprogress.toAngle - step, true);
            } else {
                ctx.arc(centreX, centreY, radius - kprogress.lineWidth, kprogress.fromAngle, kprogress.fromAngle + step, false);
            }
            ctx.stroke();
        }
    }
}
