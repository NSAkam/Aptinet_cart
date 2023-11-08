import QtQuick 2.15
import QtGraphicalEffects 1.15
import "../Utiles" as Util
import "../Components"

Item {
    id: root
    signal nfcPaymentClicked()

    Rectangle{
        id: toppart
        width: 632
        height: 300
        radius: 8
        color: Qt.rgba(255, 255, 255, 0.6)
        x: 120
        y: 54 + 25

        Text {
            id: cart_subtotal_text
            text: qsTr("Cart Subtotal")
            font.pixelSize: 20
            color: "#6D6D6D"
            x: 48
            y: 42
        }

        Rectangle {
            id: cart_subtotal_line
            width: 272
            height: 0.51
            color: "#D9D9D9"
            border.color: "#D9D9D9"
            border.width: 0.5
            x: 199
            y: 59
        }

        Text {
            id: taxtext
            text: qsTr("Tax")
            font.pixelSize: 20
            color: "#6D6D6D"
            x: 48
            y: 100
        }

        Rectangle {
            id: taxline
            width: 380
            height: 0.51
            color: "#D9D9D9"
            border.color: "#D9D9D9"
            border.width: 0.5
            x: 106
            y: 117
        }

        Text {
            id: savingstext
            text: qsTr("Savings")
            font.pixelSize: 20
            color: "#6D6D6D"
            x: 48
            y: 158
        }

        Rectangle {
            id: savingsline
            width: 322
            height: 0.51
            color: "#D9D9D9"
            border.color: "#D9D9D9"
            border.width: 0.5
            x: 149
            y: 175
        }

        Text {
            id: cartsubtotalvalue
            text: qsTr("$ 90.72")
            font.pixelSize: 24
            color: viewset.primaryColor
            x: 495
            y: 40
            font.bold: true
        }

        Text {
            id: taxvalue
            text: qsTr("$ 0.00")
            font.pixelSize: 24
            color: viewset.primaryColor
            x: 510
            y: 98
            font.bold: true
        }

        Text {
            id: savingsvalue
            text: qsTr("$ 22.00")
            font.pixelSize: 24
            color: viewset.primaryColor
            x: 495
            y: 156
            font.bold: true
        }

        Rectangle {
            id: discountcartrect
            width: 417
            height: 54
            x: 48
            y: 214
            radius: 4

            Text {
                id: discountcarttext
                text: qsTr("Enter Discount Code")
                font.pixelSize: 20
                color: "#9D9D9D"
                x: 16
                y: 16
            }
        }

        KButton {
            text: "Apply"
            x: 465
            y: 214
            borderRadius: 4
            btn_color: viewset.secondaryColor
            btn_bordercolor: viewset.secondaryColor
        }
    }

    Rectangle {
        id: bottompart
        width: 632
        height: 195
        radius: 8
        color: Qt.rgba(255, 255, 255, 0.9)
        x: 120
        y: 362 + 25

        Text {
            id: totaltext
            text: qsTr("Total")
            font.pixelSize: 20
            color: "#6D6D6D"
            x: 48
            y: 38.5
        }

        Rectangle {
            id: totalline
            width: 324
            height: 0.51
            color: "#D9D9D9"
            border.color: "#D9D9D9"
            border.width: 0.5
            x: 118.5
            y: 55.5
        }

        Text {
            id: totalvalue
            text: qsTr("$ 68.72")
            font.pixelSize: 32
            color: viewset.secondaryColor
            x: 466
            y: 32
            font.bold: true
        }

        KButton {
            text: "Back"
            fontsize: 24
            x: 43
            y: 99
            borderRadius: 4
        }

        KButton {
            text: "Payment via NFC"
            fontsize: 24
            x: 274
            y: 99
            borderRadius: 4
            btn_color: viewset.secondaryColor
            btn_bordercolor: viewset.secondaryColor

            Image {
                source: "../../Assets/goRightInItemView.png"
                x: 282
                y: 28

            }

            MouseArea {
                anchors.fill: parent
                onClicked: {
                    root.nfcPaymentClicked()
                }

            }
        }
    }

    Image {
        source: "../../Assets/OrangeWarning.png"
        x: 519 - 390
        y: 589 + 25
    }

    Text {
        text: "<font color='#6D6D6D'>You can’t </font><font color='" + viewset.primaryColor + "'>add</font><font color='#6D6D6D'> or </font><font color='" + viewset.primaryColor + "'>remove</font><font color='#6D6D6D'> items from your cart </font><font color='" + viewset.primaryColor + "'>during</font><font color='#6D6D6D'> the payment process.</font>"
        font.pixelSize: 16
        y: 590.5 + 25 - 3
        x: 553 - 390
    }

    Image {
        source: "../../Assets/OrangeWarning.png"
        x: 519 - 390
        y: 633 + 25
    }

    Text {
        text: "<font color='#6D6D6D'>Please, </font><font color='" + viewset.primaryColor + "'>check</font><font color='#6D6D6D'> all the items of your list in the cart before payment.</font>"
        font.pixelSize: 16
        y: 634.5 + 25 - 2
        x: 553 - 390
    }

    DropShadow {
        anchors.fill: bottompart
        cached: true
        horizontalOffset: 0
        verticalOffset: 8
        radius: 2
        y: 5
        samples: 30
        color: "#0000000A"
        smooth: true
        source: bottompart
        visible: shadow?true:false
    }

}
