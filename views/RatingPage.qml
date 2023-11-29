import QtQuick 2.15
import QtGraphicalEffects 1.15
import "Utiles" as Util
import "Components"
import KAST.Logic 1.0


Item {

    property int sizeVal: 70
    property int radiusVal: 40

    property Logic obj_LogicContainerRatingPage


    Text {
        text: "How would you rate your shopping experience?"
        font.pixelSize: 24
        horizontalAlignment: Text.AlignHCenter
        x: -55
        y: 48
        color: "#1D1D1D"
    }

    Row {
        spacing: 32
        y: 122
        x: -10

        Rectangle {
            width: sizeVal
            height: sizeVal
            radius: radiusVal

            KButton {
                anchors.fill: parent
                btn_color: "#92dc7c"
                btn_bordercolor: "#92dc7c"

                Image {
                    source: "../Assets/badrate.png"
                    anchors.centerIn: parent
                }

                DropShadow {
                    anchors.fill: parent
                    cached: true
                    horizontalOffset: 0
                    verticalOffset: 4
                    radius: 4.0
                    y: 0
                    samples: 30
                    color: "#6c9bd7"
                    smooth: true
                    source: parent
                    visible: shadow?true:false
                }
            }

        }



        Rectangle {
            width: sizeVal
            height: sizeVal
            radius: radiusVal

            KButton {
                anchors.fill: parent
                btn_color: "#7ad35f"
                btn_bordercolor: "#7ad35f"

                Image {
                    source: "../Assets/goodrate.png"
                    anchors.centerIn: parent
                }

                DropShadow {
                    anchors.fill: parent
                    cached: true
                    horizontalOffset: 0
                    verticalOffset: 4
                    radius: 4.0
                    y: 0
                    samples: 30
                    color: "#6c9bd7"
                    smooth: true
                    source: parent
                    visible: shadow?true:false
                }
            }

        }


        Rectangle {
            width: sizeVal
            height: sizeVal
            radius: radiusVal
            color: "#67db45"

            KButton {
                anchors.fill: parent
                btn_color: "#67db45"
                btn_bordercolor: "#67db45"

                Image {
                    source: "../Assets/verygoodrate.png"
                    anchors.centerIn: parent
                }

                DropShadow {
                    anchors.fill: parent
                    cached: true
                    horizontalOffset: 0
                    verticalOffset: 4
                    radius: 4.0
                    y: 0
                    samples: 30
                    color: "#6c9bd7"
                    smooth: true
                    source: parent
                    visible: shadow?true:false
                }
            }

        }


        Rectangle {
            width: sizeVal
            height: sizeVal
            radius: radiusVal
            color: "#4ce51f"

            KButton {
                anchors.fill: parent
                btn_color: "#4ce51f"
                btn_bordercolor: "#4ce51f"

                Image {
                    source: "../Assets/excellentrate.png"
                    anchors.centerIn: parent
                }

                DropShadow {
                    anchors.fill: parent
                    cached: true
                    horizontalOffset: 0
                    verticalOffset: 4
                    radius: 4.0
                    y: 0
                    samples: 30
                    color: "#6c9bd7"
                    smooth: true
                    source: parent
                    visible: shadow?true:false
                }

            }
        }
    }
}
