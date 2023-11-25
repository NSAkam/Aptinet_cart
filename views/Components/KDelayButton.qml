import QtQuick 2.15
import QtQuick.Window 2.12
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0

Item {
    property alias content: control
    DelayButton {
        id: control
        text: qsTr("Delay\nButton")
        width: parent.width
        height: parent.height
        delay: 1000
        onPressed: {
            rectShadow.visible =false
        }
        onReleased: {
            rectShadow.visible =true
        }
        onActivated: {
            //tanzimat.weightSensorSaveSetting();
        }


        //contentItem: content
        background: Rectangle {
            gradient: Gradient {
                GradientStop { position: 0.50; color: "white"; }
                GradientStop { position: 1.0; color: viewset.primaryColor; }
            }
            implicitWidth: 100
            implicitHeight: 100
            opacity: enabled ? 1 : 0.3
            color: control.down ? "white" : "white"
            radius: size / 2

            readonly property real size: Math.min(control.width, control.height)
            width: size
            height: size
            anchors.centerIn: parent

            Canvas {
                id: canvas
                anchors.fill: parent

                Connections {
                    target: control
                    onProgressChanged:
                    {

                        canvas.requestPaint()
                    }
                }

                onPaint: {
                    var ctx = getContext("2d")
                    ctx.clearRect(0, 0, width, height)
                    ctx.strokeStyle = "#2979ff"
                    ctx.lineWidth = parent.size / 50
                    ctx.beginPath()
                    var startAngle = Math.PI / 5 * 3
                    var endAngle = startAngle + control.progress * Math.PI / 5 * 9
                    ctx.arc(width / 2, height / 2, width / 2 - ctx.lineWidth / 2 - 2, startAngle, endAngle)

                    ctx.stroke()

                }
            }

        }
    }

    DropShadow {
        id: rectShadow
        anchors.fill: source
        cached: false
        horizontalOffset: 0
        verticalOffset: 0
        radius: 50
        samples: 20
        color: "white"
        smooth: true
        source: control
    }
}
