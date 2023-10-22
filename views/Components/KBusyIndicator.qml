import QtQuick 2.15
import QtQuick.Controls 2.15

BusyIndicator {
    id: control
    anchors.fill: parent
    property string mtext: "در حال پردازش"
    background: Item {
        Rectangle{
            anchors.fill: parent
            color: "black"
            opacity: 0.5

        }
        Rectangle{
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            width: 400
            height: 200
            radius: 15
            Label{
                text: control.mtext
                font.family: viewset.danaFuNumBoldFont
                color: "black"
                font.pixelSize: 24
                anchors.horizontalCenter: parent.horizontalCenter
                //anchors.verticalCenter: parent.verticalCenter
                y:parent.height / 2 + 32
            }
        }
    }


    contentItem: Item {
        implicitWidth: 64
        implicitHeight: 64

        Item {
            id: item
            x: parent.width / 2 - 32
            y: parent.height / 2 - 64
            width: 64
            height: 64
            opacity: control.running ? 1 : 0

            Behavior on opacity {
                OpacityAnimator {
                    duration: 250
                }
            }

            RotationAnimator {
                target: item
                running: control.visible && control.running
                from: 0
                to: 360
                loops: Animation.Infinite
                duration: 1250
            }

            Repeater {
                id: repeater
                model: 6

                Rectangle {
                    id: delegate
                    x: item.width / 2 - width / 2
                    y: item.height / 2 - height / 2
                    implicitWidth: 10
                    implicitHeight: 10
                    radius: 5
                    color: viewset.primaryColor

                    required property int index

                    transform: [
                        Translate {
                            y: -Math.min(item.width, item.height) * 0.5 + 5
                        },
                        Rotation {
                            angle: delegate.index / repeater.count * 360
                            origin.x: 5
                            origin.y: 5
                        }
                    ]
                }
            }
        }
    }
}
