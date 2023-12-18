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

    Util.ViewSettings{
        id:viewset
    }

    property Logic obj_LogicContainerGuidTips1


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
        color: viewset.secondaryColor

        Text {
            text: obj_LogicContainerGuidTips1.lang.txt_Guide_to_add_product_to_cart
            color: "white"
            font.family: "Archivo"
            anchors.horizontalCenter: parent.horizontalCenter
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
            color: viewset.secondaryColor
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
            text: obj_LogicContainerGuidTips1.lang.txt_scan_its_barcode_of_the_selected_product
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
            color: viewset.secondaryColor
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
            text: obj_LogicContainerGuidTips1.lang.txt_You_have_sec_to_view_product_information_and_put_in_the_cart
            anchors.verticalCenter: rect2.verticalCenter
            anchors.horizontalCenter: rect2.horizontalCenter
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
        y: 480

        Text {
            text: qsTr("3")
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            font.pixelSize: 48
            color: viewset.secondaryColor
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
            text: obj_LogicContainerGuidTips1.lang.txt_Continue_after_you_hear_the_notification_sound
            anchors.verticalCenter: rect3.verticalCenter
            anchors.horizontalCenter: rect3.horizontalCenter
            font.pixelSize: 32
            opacity: 0
            Behavior on opacity {
                NumberAnimation{duration: 1000}
            }
        }
    }

    KButton {
        id: nextbutton
        text: obj_LogicContainerGuidTips1.lang.btn_I_got_it +" >"
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
                stackview.push(g2)
            }
        }
    }
    Component{
        id:g2
        GuideTips2{
            obj_LogicContainerGuidTips2: obj_LogicContainerGuidTips1
        }
    }

}
