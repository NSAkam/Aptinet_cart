import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.12
import QtGraphicalEffects 1.15
import "../Utiles"
import "../Components"
import KAST.Logic 1.0



Popup {
    id: popupBypass
    property Logic obj_logicByPassPopup

    signal ok()



    property string messageText:"value"

    topMargin: 0
    bottomMargin: 0
    x: 0
    width: parent.width
    height: parent.height
    focus: false

    closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutsideParent
    background:
        Item {
        anchors.fill: parent
        Rectangle {
            id:rectContainer
            anchors.fill: parent
            color: "#191641"
            opacity: 0.5
        }
        Image {
            id: img_setting
            source: "../../Assets/setting.png"
            x:20
            y:24
            MouseArea{
                anchors.fill: parent
                onClicked: {

                }
            }
        }
    }

    contentItem: Item {
        Rectangle{
            id:lstfBypass
            visible: true
            color: viewset.backgroundColor
            width: 640
            height: 500
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            radius: 15

            Component{
                id:factorDelegate

                Item {
                    id: itemFactorItem
                    x:5
                    anchors.horizontalCenter: parent.horizontalCenter
                    width: 600
                    height: 70
                    Rectangle{
                        id:rectFactorItem
                        anchors.fill: parent
                        radius: 4
                        Image {
                            id: factorItemPic
                            source: model.pic
                            anchors.right: parent.right
                            anchors.top: parent.top
                            width: 60
                            height: 60
                            anchors.topMargin: 7
                            anchors.rightMargin: 20
                        }
                        Label {
                            id: factorItemName
                            text: model.name
                            font.family: viewset.danaFuNumFont
                            font.pixelSize: 16
                            anchors.right: factorItemPic.left
                            anchors.top: parent.top
                            width: 277
                            height: 75
                            anchors.topMargin: 22
                            anchors.rightMargin: 20
                            elide: Text.ElideRight
                        }
                        Image {
                            id: btnDownCount
                            source: "../../Assets/up.png"
                            width: 24
                            height: 24
                            x:108
                            anchors.verticalCenter: parent.verticalCenter

                            MouseArea{
                                anchors.fill: parent
                                onClicked: {
                                    obj_logicByPassPopup.shopPage.bypass_increaseClicked(index)
                                }
                            }
                        }
                        Rectangle {
                            id: rectFactorItemPercentage
                            anchors.verticalCenter: parent.verticalCenter
                            x:60
                            anchors.rightMargin: 9
                            color: "#F2C335"
                            width: 36
                            height: 36
                            radius: 50
                            Label {
                                text: model.countInBasket
                                anchors.horizontalCenter: parent.horizontalCenter
                                font.family: viewset.danaFuNumBoldFont
                                y:3
                                font.pixelSize: 20
                                font.bold: true
                                //anchors.right:  factorItemPrice.left
                                elide: Text.ElideRight
                                color: "white"
                            }
                        }

                        Image {
                            id: btnUpCount
                            source: "../../Assets/up.png"
                            width: 24
                            height: 24
                            anchors.verticalCenter: parent.verticalCenter
                            x:24
                            transformOrigin: Item.Center
                            rotation: 180
                            MouseArea{
                                anchors.fill: parent
                                onClicked: {
                                    obj_logicByPassPopup.shopPage.bypass_decreaseClicked(index)
                                }
                            }
                        }


                    }
                    DropShadow {
                        id: rectFactorItemshadow
                        anchors.fill: source
                        cached: true
                        radius: 16.0
                        samples: 30
                        color: "#19000000"
                        smooth: true
                        source: rectFactorItem
                        verticalOffset:  5
                    }
                }
            }

            ListView {
                id:lst_prd
                y:10
                spacing: 5
                width: parent.width
                height:parent.height - 80
                focus: true
                model: obj_logicByPassPopup.shopPage.bypassList
                delegate: factorDelegate
                clip: true
                currentIndex: -1
                cacheBuffer: 10000
                smooth: true
                antialiasing: true
                snapMode: ListView.SnapOneItem
            }
            KButton{
                anchors.top: lst_prd.bottom
                anchors.horizontalCenter: parent.horizontalCenter
                text: "Confirm"
                anchors.topMargin: 10
                width: 300
                height: 51
                borderRadius: 4
                onClicked: {
                    popupBypass.ok()
                }
            }
        }
    }

}
