import QtQuick 2.15
import QtQuick.Window 2.12
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0
import "Utiles" as Util


Window {
    id:mainwindow
    width: 1280
    height: 800
    visible: true
    color: "white"

    //contentItem.rotation: 180

    property alias stackview: stackview

    StackView
    {
        id:stackview
        anchors.fill: parent
//        initialItem: "Splash.qml"
        initialItem: "AfterPayment.qml"
//        initialItem: "Checkout.qml"
//        initialItem: "PaymentviaNFC.qml"
//        initialItem: "Shop.qml"
        Util.ViewSettings{
            id:viewset
        }
    }
}
