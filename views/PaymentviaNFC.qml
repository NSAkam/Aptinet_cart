import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import QtQuick.Window 2.0
import QtQuick.Controls.Styles 1.4
import "Components"
import "Containers"
import "Utiles" as Util
import KAST.Logic 1.0


Item {

    width: 1280
    height: 800

    property Logic obj_LogicContainerPaymentNFC


    Util.ViewSettings{
        id:viewset
    }


    Image {
        source: "/home/aptinet/files/AuthenticationBackground.png"
        anchors.fill: parent
    }

    Rectangle {
        color: "#A37A544D"
        anchors.fill: parent
        opacity: 0.3
    }

    Rectangle{
        width: parent.width
        height: 92
        x:0
        y:0
    }
    TopNav{
        backvisible: true
        onBackClicked: {
            obj_LogicContainerPaymentNFC.shopPage.payment_backClicked()
            stackview.pop()
        }
    }

    Image {
        source: "../Assets/Help.png"
        width: 57
        height: 57
        x:1156
        y:25
        visible: false
    }
    Image {
        source: "../Assets/Notification.png"
        width: 57
        height: 57
        x:1208
        y:25
    }
    Item{
        id:topPanel
        width: 0
        height: 92
        Rectangle{
            width: parent.width
            height: parent.height
            x:0
            y:0
//            Rectangle{
//                width: 50
//                height: 50
//                color: viewset.primaryColor
//                x:530 + 390
//                y:24
//                radius: width /2
//            }
//            Text {
//                text: "user Email"
//                color: "#6D6D6D"
//                width: 148
//                height: 15
//                font.pixelSize: 14
//                x:586 + 390
//                y:40.5
//            }
            Image {
                source: "../Assets/Help.png"
                width: 57
                height: 57
                x:1156
                y:25
            }
            Image {
                source: "../Assets/Notification.png"
                width: 57
                height: 57
                x:1208
                y:25
                MouseArea{
                    anchors.fill: parent
                    onClicked: {
                        obj_LogicContainerPaymentNFC.shopPage.call_forHelpClicked()
                    }
                }
            }

        }
    }



    Image {
        source: "../Assets/payment_animation.png"
        x: 498
        y: 185 + topPanel.height
    }

    Text {
        text: "<font color='#1D1D1D'>"+obj_LogicContainerPaymentNFC.lang.txt_Please_hold_your_phone+"</font><font color='" + viewset.primaryColor + "'> "+obj_LogicContainerPaymentNFC.lang.txt_near_the_display+"<br></font><font color='#1D1D1D'> "+obj_LogicContainerPaymentNFC.lang.txt_until_you_see_a_check_mark+"</font>"
        font.pixelSize: 32
        y: 348 + topPanel.height
        x: 314
        font.bold: true
        horizontalAlignment: Text.AlignHCenter
    }

    Image {
        source: "../Assets/ApplePay.png"
        x: 522
        y: 550 + topPanel.height
    }

    Image {
        source: "../Assets/GooglePay.png"
        x: 672
        y: 550 + topPanel.height
        MouseArea{
            anchors.fill: parent
            onClicked: {

            }
        }
    }

    Text {
        text: obj_LogicContainerPaymentNFC.lang.txt_What_are_NFC_payments_NFC_technology_powers_contactless_payments_via_mobile_wallets_like_Apple_Pay_and_Google_Pay_as_well_as_contactless_cards
        x: 292
        y: 612 + topPanel.height
        font.pixelSize: 16
        color: "#6D6D6D"
        horizontalAlignment: Text.AlignHCenter
    }

    Component{
        id:afterpaymentPage
        AfterPayment{
            obj_LogicContainerAfterPayment: obj_LogicContainerPaymentNFC
        }
    }

    Connections{
        target:obj_LogicContainerPaymentNFC.shopPage
        function onShowAfterPaymentSignal(){
            stackview.push(afterpaymentPage)
        }
    }


}
