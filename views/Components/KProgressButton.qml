import QtQuick 2.15
import QtGraphicalEffects 1.0
import QtQuick.Controls 2.15
import "../Utiles"

Item{
    property int level: 7
    ViewSettings{
        id:viewset
    }
    ProgressBar {
        id: targetProgressBar
        value: level
        from:7
        to:0


        background: Rectangle {
            implicitWidth: btn.width
            implicitHeight: btn.height
            color: "transparent"
            radius: 15
        }

        contentItem: Item {
            anchors.fill: btn

            Rectangle {
                id:rect_porgress
                width: targetProgressBar.visualPosition * btn.width
                height: btn.height
                radius: 15
                color: "#6C97E7"
            }
//            LinearGradient {
//                anchors.fill: rect_porgress
//                source: rect_porgress
//                start: Qt.point(0, 0)
//                end: Qt.point(50, 0)
//                gradient: Gradient {
//                    GradientStop { position: 0.0; color:"transparent" }
//                    GradientStop { position: 1.0; color: "#6C97E7" }
//                }
//            }
        }
    }

    Rectangle {
        id:btn
        width: 164
        height: 33
        color: "transparent"
        radius: 12
        border.color: viewset.primaryColor
        border.width: 1

        Text {
            id: buttonText;
            text: "انصراف";
            color: viewset.primaryColor;
            font {
                pixelSize: 12
                family: viewset.danaFuNumFont
                bold: false
            }
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter

            //y:parent.height / 2 - 8
        }
    }
}
