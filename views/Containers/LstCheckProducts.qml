import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import "../Components"
import KAST.Logic 1.0



Item {
    id:lstFactor
    property Logic obj_LogicContainerLstCheckProducts
    signal gocheckout()


    anchors.fill: parent
    Rectangle{
        anchors.fill: parent
        color: "White"

    }
    Rectangle{
        x:0
        y:0
        width: 890
        height: 103
        Text {
            text: "My Cart"
            font.pixelSize: 36
            anchors.verticalCenter: parent.verticalCenter
            color: "#6D6D6D"
            x:40
            font.bold: true
        }
    }

    Component{
        id:factorDelegate


        Item {
            id: itemFactorItem
            x:5
            width: 826
            height: 140
            anchors.horizontalCenter: parent.horizontalCenter

            Rectangle{
                id:rectFactorItem
                anchors.fill: parent

                Image {
                    id: factorItemPic
                    source:  modelData.pic
                    anchors.left: parent.left
                    width: 90
                    height: 90
                    x:25
                    anchors.verticalCenter: parent.verticalCenter
                }

                Text {
                    id: factorItemName
                    text: modelData.name
                    font.pixelSize: 16
                    anchors.left: factorItemPic.right
                    width: 562
                    height: 22
                    elide: Text.ElideLeft
                    anchors.leftMargin: 57
                    font.bold: true
                    y:32
                }
                Text {
                    id: factorItemprice
                    text: "$ " + modelData.finalPrice + " each"
                    font.pixelSize: 18
                    anchors.left: factorItemPic.right
                    anchors.leftMargin: 57
                    y:91
                }
                Text {
                    id: factorItemQty
                    text: "Qty:" + modelData.countInBasket
                    font.pixelSize: 18
                    anchors.left: factorItemPic.right
                    anchors.leftMargin: 193
                    y:91
                }
                Rectangle{
                    id: splitterQuantityPrice
                    anchors.left: factorItemPic.right
                    color: "#C9C9C9"
                    anchors.leftMargin: 172
                    width: 1
                    height: 20
                    y:91
                }
                Text {
                    id: factorItemTotalPrice
                    text: "$ " + modelData.countInBasket * modelData.finalPrice
                    x:679
                    y:86
                    color: viewset.primaryColor
                    font.pixelSize: 32
                }
                Rectangle{
                    anchors.bottom: parent.bottom
                    width: parent.width
                    height: 1
                    color: "#C9C9C9"
                }
            }

        }
    }
    Component{
        id:factorWeightDelegate


        Item {
            id: itemFactorItem
            x:5
            width: 826
            height: 140
            anchors.horizontalCenter: parent.horizontalCenter

            Rectangle{
                id:rectFactorItem
                anchors.fill: parent

                Image {
                    id: factorItemPic
                    source: modelData.pic
                    anchors.left: parent.left
                    width: 90
                    height: 90
                    x:25
                    anchors.verticalCenter: parent.verticalCenter
                }

                Text {
                    id: factorItemName
                    text: modelData.name
                    font.pixelSize: 16
                    anchors.left: factorItemPic.right
                    width: 562
                    height: 22
                    elide: Text.ElideLeft
                    anchors.leftMargin: 57
                    font.bold: true
                    y:32
                }
                Text {
                    id: factorItemprice
                    text: "$ "+modelData.finalPrice + " /kg"
                    font.pixelSize: 18
                    anchors.left: factorItemPic.right
                    anchors.leftMargin: 57
                    y:91
                }
                Text {
                    id: factorItemQty
                    text: "Wt:" +modelData.productWeightInBasket  + " kg"
                    font.pixelSize: 18
                    anchors.left: factorItemPic.right
                    anchors.leftMargin: 193
                    y:91
                }
                Rectangle{
                    id: splitterQuantityPrice
                    anchors.left: factorItemPic.right
                    color: "#C9C9C9"
                    anchors.leftMargin: 172
                    width: 1
                    height: 20
                    y:91
                }
                Text {
                    id: factorItemTotalPrice
                    text: "$ " + modelData.finalPrice
                    x:679
                    y:86
                    color: viewset.primaryColor
                    font.pixelSize: 32
                }
                Rectangle{
                    anchors.bottom: parent.bottom
                    width: parent.width
                    height: 1
                    color: "#C9C9C9"
                }
            }

        }
    }

    ListView {
        id:lst_prd
        focus: true
        model: obj_LogicContainerLstCheckProducts.shopPage.factorList
        delegate: Loader {
            property variant modelData: model

            sourceComponent:  switch(dataModelShow) {
                              case 0: return factorDelegate
                              case 1: return factorWeightDelegate

                              }
        }
        x:0
        y:103
        width: parent.width
        height: 473
        clip: true
        currentIndex: -1
        cacheBuffer: 10000
        smooth: true
        antialiasing: true
        snapMode: ListView.SnapOneItem
    }

    Rectangle{
        color: "White"
        opacity: 1
        width: 890
        height: 132
        x:0
        y:576


        Text {
            id:check_TotalItems
            text: obj_LogicContainerLstCheckProducts.shopPage.factorList.totalcount
            font.pixelSize: 24
            x:259
            y:39
            color: viewset.primaryColor
            font.bold: true

        }
        Text {
            text: "Items"
            color: "#6D6D6D"
            font.pixelSize: 16
            x:253
            y:83
        }
        Text {
            id:check_TotalSaved
            text: "$  " + obj_LogicContainerLstCheckProducts.shopPage.factorList.profit
            font.pixelSize: 20
            x:344
            y:42
            color: viewset.primaryColor
            font.bold: false
        }
        Text {
            text: "Saving"
            color: "#6D6D6D"
            font.pixelSize: 16
            x:353
            y:83
        }
        Text {
            id:check_TotalPrice
            text: "$  " + obj_LogicContainerLstCheckProducts.shopPage.factorList.priceToPay
            font.pixelSize: 32
            x:463
            y:32
            color: viewset.secondaryColor
            font.bold: true
        }
        Text {
            text: "Subtotal"
            color: "#6D6D6D"
            font.pixelSize: 16
            x:489
            y:83
        }
        Image {
            source: "../../Assets/fullBasket.png"
            width: 84
            height: 84
            x:32
            y:28
        }
        KButton{
            id:btn_Checkout
            text: "Checkout"
            btn_color: viewset.secondaryColor
            borderRadius: 4
            ishover: false
            x:629
            y:30
            width: 229
            height: 72
            btn_borderWidth: 0
            onClicked: {
                obj_LogicContainerLstCheckProducts.shopPage.checkout_Clicked()
            }
        }
    }

}


