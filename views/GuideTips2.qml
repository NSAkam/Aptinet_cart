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
import KAST.Logic 1.0



Item {
    id: root
    width: 1280
    height: 800

    property Logic obj_LogicContainerGuidTips2


    Util.ViewSettings{
        id:viewset
    }

    property int state: 0

    Image {
        source: "/home/aptinet/files/AuthenticationBackground.png"
        anchors.fill: parent
    }

    Timer{
        repeat: true
        interval: 1000
        onTriggered: {
            if(state == 0)
            {
                rect1.opacity = 0.5
                txt_1.opacity =1

            }
            else if(state == 2)
            {
                rect2.opacity = 0.5
                txt_2.opacity =1
            }
            else if(state == 4)
            {
                rect3.opacity = 0.5
                txt_3.opacity =1

            }
            else if(state == 5){
                nextbutton.opacity = 1
                nextbutton.visible = true
            }

            state = state + 1
        }
        running: true
    }

    Rectangle{
        width: parent.width
        height: 92
        x:0
        y:0
        color: "#F05A28"

        Text {
            text: obj_LogicContainerGuidTips2.lang.txt_Required_Tips
            color: "white"
            font.family: "Archivo"
            font.pixelSize: 32
            font.bold: true
            x: 526
            y: 28
        }
    }

    Rectangle {
        width: 96
        height: 96
        color: "white"
        x: 170
        y: 224

        Text {
            text: qsTr("1")
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            font.pixelSize: 48
            color: viewset.primaryColor
        }

        Rectangle{
            id:rect1
            height: parent.height
            width: txt_1.width + 100
            color: "white"
            opacity: 0
            anchors.left: parent.right

            Behavior on opacity {
                NumberAnimation{duration: 1000}
            }
        }
        Text {
            id: txt_1
            text: obj_LogicContainerGuidTips2.lang.txt_Stop_and_remove_the_product_from_the_cart
            anchors.verticalCenter: rect1.verticalCenter
            anchors.horizontalCenter: rect1.horizontalCenter
            font.pixelSize: 32
            opacity: 0
            Behavior on opacity {
                NumberAnimation{duration: 1000}
            }
        }
    }

    Rectangle {
        width: 96
        height: 96
        color: "white"
        x: 170
        y: 352

        Text {
            text: qsTr("2")
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            font.pixelSize: 48
            color: viewset.primaryColor
        }
        Rectangle{
            id:rect2
            height: parent.height
            width: txt_2.width + 100
            color: "white"
            opacity: 0
            anchors.left: parent.right
            Behavior on opacity {
                NumberAnimation{duration: 1000}
            }
        }
        Text {
            id: txt_2
            text: obj_LogicContainerGuidTips2.lang.txt_After_see_the_window_scan_its_barcode_of_the_selected_product_to_remove
            anchors.verticalCenter: rect2.verticalCenter
            anchors.horizontalCenter: rect2.horizontalCenter
            font.pixelSize: 32
            wrapMode: Text.WordWrap
            width: 700

            opacity: 0
            Behavior on opacity {
                NumberAnimation{duration: 1000}
            }
        }
    }

    Rectangle {
        width: 96
        height: 96
        color: "white"
        x: 170
        y: 480

        Text {
            text: qsTr("3")
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            font.pixelSize: 48
            color: viewset.primaryColor
        }
        Rectangle{
            id:rect3
            height: parent.height
            width: txt_3.width + 100
            color: "white"
            opacity: 0
            anchors.left: parent.right
            Behavior on opacity {
                NumberAnimation{duration: 1000}
            }

        }
        Text {
            id: txt_3
            text: obj_LogicContainerGuidTips2.lang.txt_If_you_are_sure_to_remove_the_product_press_the_confirmation_button
            anchors.verticalCenter: rect3.verticalCenter
            anchors.horizontalCenter: rect3.horizontalCenter
            width: 700
            wrapMode: Text.WordWrap
            font.pixelSize: 32
            opacity: 0
            Behavior on opacity {
                NumberAnimation{duration: 1000}
            }
        }
    }

    KButton {
        id: nextbutton
        text: obj_LogicContainerGuidTips2.lang.btn_I_got_it + " >"
        //color: viewset.secondaryColor
        width: 150
        borderRadius: 5
        fontsize: 20
        opacity: 0
        x:1029
        y:677
        visible: false
        btn_color: viewset.secondaryColor
        btn_borderWidth: 0
        MouseArea{
            anchors.fill: parent
            onClicked: {
                stackview.pop()
                stackview.pop()
                stackview.pop()
            }
        }
    }

}
