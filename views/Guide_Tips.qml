import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import QtQuick.Window 2.0
import QtQuick.Controls.Styles 1.4
import QtGraphicalEffects 1.0
import "Components"
import "Containers"
import "Utiles" as Util
import "PopUps"

Item {
    id: root
    width: 1280
    height: 800

    Util.ViewSettings{
        id:viewset
    }

    Image {
        source: "../Assets/AuthenticationBackground.png"
        anchors.fill: parent
    }


    Rectangle {
        width: root.width
        height: 92
        color: "#F05A28"
        x: 0
        y: 0

        Text {
           text: qsTr("Required Tips")
           font.pixelSize: 32
           font.weight: Font.Bold
           lineHeight: Font.Normal
           y: 28
           x: 526
           font.letterSpacing: 1.28
           color: "white"
        }
    }

    Column {
        x: 170
        y: 224
        spacing: 32

        TipsText {
            imagesource: "../Assets/blankbasket.png"
            textcontent: "<font color='#6D6D6D'>Make sure the cart is</font><font color='" + viewset.primaryColor + "'> empty</font>"
        }

        TipsText {
            imagesource: "../Assets/plusbasket.png"
            textcontent: "<font color='#6D6D6D'>Don’t <font color='" + viewset.primaryColor + "'>move</font> the cart when add or remove products.</font>"
        }

    }

}
