import QtQuick 2.15
import QtQuick.Window 2.2
import QtQuick.Controls 2.2
import QtQuick.Layouts 1.4
import QtGraphicalEffects 1.15


Rectangle{
    radius: 50
    width: 184
    height: 40

    property real pvalue:0.5

    Text{
        id:lbl1
        text: "سقف خرید:"
        anchors.verticalCenter: parent.verticalCenter
        anchors.right: parent.right
        rightPadding: 16
        font.family: viewset.danaFuNumFont
        font.bold: true
        font.pixelSize: 16
    }
    Text {
        id: lbl2
        text: pvalue + "%"
        color: "#F2C335"
        font.pixelSize: 16
        anchors.right: lbl1.left
        anchors.top : lbl1.top
        rightPadding: 6
        font.family: viewset.danaFuNumFont

    }

    Image {
        id: imgContainer
        source: "../../Assets/BasketVector.png"
        anchors.verticalCenter: parent.verticalCenter
        x:12
        z: 100
        width: 14
        height: 14
    }




    Item {
        id: root

        property int size: 40
        property int lineWidth: 6
        property real value: pvalue / 100

        property color primaryColor: "#191641"
        property color secondaryColor: "#FFFFFF"

        property int animationDuration: 1000

        width: 40
        height: parent.height

        onValueChanged: {
            canvas.degree = value * 360;
        }
        Component.onCompleted: {
            canvas.degree = value * 360
        }

        Canvas {
            id: canvas

            property real degree: 0

            anchors.fill: parent
            antialiasing: true

            onDegreeChanged: {
                requestPaint();
            }

            onPaint: {
                var ctx = getContext("2d");

                var x = root.width/2 -0;
                var y = root.height/2;

                var radius = root.size/2 - root.lineWidth+ 3
                var startAngle = (Math.PI/180) * 270;
                var fullAngle = (Math.PI/180) * (270 + 360);
                var progressAngle = (Math.PI/180) * (270 + degree);

                ctx.reset()

                ctx.lineCap = 'solid';
                ctx.lineWidth = root.lineWidth;

                ctx.beginPath();
                ctx.arc(x, y, radius, startAngle, fullAngle);
                ctx.strokeStyle = root.secondaryColor;
                ctx.stroke();

                ctx.beginPath();
                ctx.arc(x, y, radius, startAngle, progressAngle);
                ctx.strokeStyle = root.primaryColor;
                ctx.stroke();
            }

            Behavior on degree {
                NumberAnimation {
                    duration: root.animationDuration
                }
            }
        }
    }

    DropShadow {
        id: sShadow
        anchors.fill: source
        cached: true
        radius: 10.0
        samples: 20
        color: "#80000000"
        smooth: true
        source: root

    }
}
