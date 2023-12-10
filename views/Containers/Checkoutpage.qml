import QtQuick 2.15
import QtGraphicalEffects 1.15
import "../Utiles" as Util
import "../Components"
import "../"
import KAST.Logic 1.0


Item {
    id: root
    signal nfcPaymentClicked()
    signal back()
    width: 1280
    height: 800

    property Logic obj_LogicContainerCheckoutPage

    Image {
        source: "../../Assets/StackBackground.png"
        anchors.fill: parent
    }

    Rectangle{
        id: toppart
        width: 632
        height: 300
        radius: 8
        color: Qt.rgba(255, 255, 255, 0.6)
        x: 120
        y: 14 + 25

        Text {
            id: cart_subtotal_text
            text: "Cart Subtotal"
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
            text: "Tax"
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
            text: "Savings"
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
            text: "$  " + (obj_LogicContainerCheckoutPage.shopPage.factorList.finalprice *1).toFixed(2)
            font.pixelSize: 24
            color: viewset.primaryColor
            x: 495
            y: 40
            font.bold: true
        }

        Text {
            id: taxvalue
            text: "$  " + (obj_LogicContainerCheckoutPage.shopPage.factorList.tax * 1).toFixed(2)
            font.pixelSize: 24
            color: viewset.primaryColor
            x: 510
            y: 98
            font.bold: true
        }

        Text {
            id: savingsvalue
            text: "$  " + (obj_LogicContainerCheckoutPage.shopPage.factorList.profit * 1).toFixed(2)
            font.pixelSize: 24
            color: viewset.primaryColor
            x: 495
            y: 156
            font.bold: true
        }

        Rectangle{
            id:rectEnterPLU
            x: 48
            y: 214
            width: 417
            height: 54
            color: "#F1F1F1"
            radius: 4
            TextInput{
                id:txt_OfferCodeInput
                anchors.fill: parent
                font.pixelSize: 18
                layer.enabled: true
                horizontalAlignment: TextInput.AlignHCenter
                verticalAlignment:  TextInput.AlignVCenter
                font.family: viewset.danaFuNumFont
                property string placeholderText: "Enter Discount Code"

                onFocusChanged: {
                    numpad.inputtext = txt_OfferCodeInput
                    numpad.visible = true
                }
                Text {
                    text: txt_OfferCodeInput.placeholderText
                    color: "#C6C5CE"
                    visible: !txt_OfferCodeInput.text
                    font.pixelSize: 18
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    font.family: viewset.danaFuNumFont
                }
            }
        }




        KButton {
            text: "Apply"
            x: 465
            y: 214
            width: 119
            height: 54
            borderRadius: 4
            btn_color: viewset.secondaryColor
            btn_bordercolor: viewset.secondaryColor
            onClicked: {
                obj_LogicContainerCheckoutPage.shopPage.apply_couponCode(txt_OfferCodeInput.text)
            }
        }
    }

    Rectangle {
        id: bottompart
        width: 632
        height: 235
        radius: 8
        color: Qt.rgba(255, 255, 255, 0.9)
        x: 120
        y: 322 + 25

        Text {
            id: totaltext
            text: "Total"
            font.pixelSize: 20
            color: "#6D6D6D"
            x: 48
            y: 30.5
        }

        Rectangle {
            id: totalline
            width: 324
            height: 0.51
            color: "#D9D9D9"
            border.color: "#D9D9D9"
            border.width: 0.5
            x: 118.5
            y: 48
        }

        Text {
            id: totalvalue
            text: "$  " + (obj_LogicContainerCheckoutPage.shopPage.factorList.priceToPay * 1).toFixed(2)
            font.pixelSize: 32
            color: viewset.secondaryColor
            x: 466
            y: 24
            font.bold: true
        }

        KButton {
            text: "Back"
            fontsize: 24
            x: 43
            y: 91
            borderRadius: 4
            width: 205
            height: 60
            onClicked: {
                obj_LogicContainerCheckoutPage.shopPage.checkout_backClicked()
            }
        }

        KButton {
            text: "Payment"
            fontsize: 24
            x: 274
            y: 91
            width: 304
            height: 60
            borderRadius: 4
            btn_color: viewset.secondaryColor
            btn_bordercolor: viewset.secondaryColor

            Text {
                font.pixelSize: 24
                anchors.verticalCenter: parent.verticalCenter
                text: ">"
                x:271
                color: "white"
                font.bold: true
            }

            onClicked: {
                obj_LogicContainerCheckoutPage.shopPage.payment_clicked()
            }


        }

        KButton {
            text: "Payment Via QR"
            fontsize: 24
            x: 43
            y: 160
            width: 535
            height: 60
            borderRadius: 4
            btn_color: viewset.secondaryColor
            btn_bordercolor: viewset.secondaryColor

            onClicked: {
                stackview.push(paymentQRCode)
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


    Numpad{
        id:numpad
        visible: false
        x:400
        y:290
        onEnter: {
            numpad.visible = false

        }
    }

    Component{
        id:paymentQRCode
        PaymentQR{
            obj_LogicContainerPaymentQr: obj_LogicContainerCheckoutPage
        }

    }

}
