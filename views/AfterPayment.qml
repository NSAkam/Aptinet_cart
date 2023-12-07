import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import QtQuick.Window 2.0
import "Components"
import "Containers"
import "Utiles" as Util
import KAST.Logic 1.0


Window {

    width: 1280
    height: 800

    property Logic obj_LogicContainerAfterPayment

    Util.ViewSettings{
        id:viewset
    }

    Image {
        id: bg
        source: "../Assets/AuthenticationBackground.png"
        anchors.fill: parent
    }

    Rectangle {
        color: "#1745E8"
        anchors.fill: bg
        opacity: 0.4
    }

    Item{
        id:topPanel
        width: parent.width
        height: 92

        Rectangle {
            id: questionmarkrect
            width: 40
            height: 40
            radius: 4
            color: "white"
            x:1156
            y:32

            Image {
                source: "../Assets/questionmark.png"
                anchors.centerIn: parent
                //                width: 57
                //                height: 57
            }
        }


        Rectangle {
            id: alarmrect
            width: 40
            height: 40
            radius: 4
            color: "white"
            x:1208
            y:32

            Image {
                source: "../Assets/alarm.png"
                anchors.centerIn: parent
                //                width: 57
                //                height: 57
            }
        }



    }

    Item{
        id:leftPanel
        width: 390
        height: parent.height

        Image {
            source: "../Assets/AptinetText1.png"
            x:32
            y:32
        }
    }

    Item {
        id: mainPanel
        width: 1280
        height: 800

        Rectangle {
            width: 502
            height: 72
            x: 389
            y: -9
            radius: 12
            color: Qt.hsla(0, 0, 100, 0.2)
        }

        Canvas {
            x: 401
            y: 63
            width: 478
            height: 1

            onPaint: {
                var ctx = getContext("2d");
                ctx.strokeStyle = "#9D9D9D";
                ctx.lineWidth = 2;
                ctx.setLineDash([4, 4]); // Set the dash pattern
                ctx.beginPath();
                ctx.moveTo(0, height / 2);
                ctx.lineTo(width, height / 2);
                ctx.stroke();
            }
        }

        Rectangle {
            width: 502
            height: 379
            x: 389
            y: 63
            radius: 12
            color: Qt.hsla(0, 0, 100, 0.2)

            Rectangle {
                width: 167.9
                height: 167.9
                radius: width / 2
                color: "#36EB00"
                x: 167
                y: 47.2

                AnimatedImage {
                    source: "../Assets/5601968.gif"
                    anchors.fill: parent
                }
            }

            Text {
                text: "You’re good to go!"
                font.pixelSize: 40
                color: "#36EB00"
                anchors.horizontalCenter: parent.horizontalCenter
                y: 246
                font.bold: true
            }

            Text {
                text: "Thanks for shopping with us"
                font.pixelSize: 30
                color: "white"
                x: 51
                y: 314
                font.weight: Font.DemiBold
            }

        }
        EnterEmail {
            width: 393
            height: 280
            x: 444
            y: 451
            visible: false
        }
        Text {
            text: "How would you rate your shopping experience?"
            font.pixelSize: 24
            horizontalAlignment: Text.AlignHCenter
            anchors.horizontalCenter: parent.horizontalCenter
            y: 473
            color: "#1D1D1D"
        }

        Row {
            spacing: 32
            y: 579
            anchors.horizontalCenter: parent.horizontalCenter


            Rectangle {
                width: 70
                height: 70
                radius: 70
                KButton {
                    anchors.fill: parent
                    btn_color: "#92dc7c"
                    btn_bordercolor: "#92dc7c"

                    Image {
                        source: "../Assets/badrate.png"
                        anchors.centerIn: parent
                    }

                }

            }



            Rectangle {
                width: 70
                height: 70
                radius: 70

                KButton {
                    anchors.fill: parent
                    btn_color: "#7ad35f"
                    btn_bordercolor: "#7ad35f"

                    Image {
                        source: "../Assets/goodrate.png"
                        anchors.centerIn: parent
                    }
                }

            }


            Rectangle {
                width: 70
                height: 70
                radius: 70

                KButton {
                    anchors.fill: parent
                    btn_color: "#67db45"
                    btn_bordercolor: "#67db45"

                    Image {
                        source: "../Assets/verygoodrate.png"
                        anchors.centerIn: parent
                    }
                }

            }


            Rectangle {
                width: 70
                height: 70
                radius: 70
                color: "#4ce51f"

                KButton {
                    anchors.fill: parent
                    btn_color: "#4ce51f"
                    btn_bordercolor: "#4ce51f"

                    Image {
                        source: "../Assets/excellentrate.png"
                        anchors.centerIn: parent
                    }



                }
            }

        }

    }
}
