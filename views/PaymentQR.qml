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
    property Logic obj_LogicContainerPaymentQr


    Util.ViewSettings{
        id:viewset
    }


    Image {
        source: "../Assets/AuthenticationBackground.png"
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
            stackview.pop()
        }
    }
    //    Rectangle{
    //        width: 50
    //        height: 50
    //        color: viewset.primaryColor
    //        x:530 + 390
    //        y:24
    //        radius: width /2
    //    }
    //    Text {
    //        text: "user Email"
    //        color: "#6D6D6D"
    //        width: 148
    //        height: 15
    //        font.pixelSize: 14
    //        x:586 + 390
    //        y:40.5
    //    }
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
            }

        }
    }



    Image {
        source: "../Assets/QR.png"
        x: 498
        y: 185 + topPanel.height
        MouseArea{
            anchors.fill: parent
            onClicked: {
                console.log("asdasd")
               obj_LogicContainerPaymentQr.shopPage.payment_QRClicked()
            }
        }
    }

    Component{
        id:afterpaymentPage
        AfterPayment{
            obj_LogicContainerAfterPayment: obj_LogicContainerPaymentQr
        }
    }

    Connections{
        target:obj_LogicContainerPaymentQr.shopPage
        function onShowAfterPaymentSignal(){
            stackview.push(afterpaymentPage)
        }
    }

}
