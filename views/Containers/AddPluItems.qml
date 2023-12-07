import QtQuick 2.15
import "../Components"
import KAST.Logic 1.0


Item {
    id:root
    width: 890
    height: 708
    property Logic obj_LogicContainerAddPluItems

    Image {
        source: "../../Assets/StackBackground.png"
        anchors.fill: parent
    }


    signal back()
    signal seeAll()

    Text {
        text: "Search Results"
        x:32
        y:40
        font.pixelSize: 24
        color: "#6D6D6D"
    }
    Rectangle{
        width: 398
        height: 249
        x:32
        y:94
        radius: 4
        color: "white"
        MouseArea{
            anchors.fill: parent
            onClicked: {
                obj_LogicContainerAddPluItems.shopPage.item_PLUClicked(obj_LogicContainerAddPluItems.shopPage.newProduct.barcode)
            }
        }

        Image {
            source: obj_LogicContainerAddPluItems.shopPage.newProduct.pic
            x:32
            y:54
            width: 140
            height: 140
        }
        Text {
            x:204
            y:56
            font.pixelSize: 24
            font.bold: true
            color: "#D9D9D9"
            text: "#" + obj_LogicContainerAddPluItems.shopPage.newProduct.barcode
        }
        Text {
            x:204
            y:106
            font.pixelSize: 24
            font.bold: true
            color: "#D9D9D9"
            text: obj_LogicContainerAddPluItems.shopPage.newProduct.name
        }
        Text {
            x:204
            y:156
            font.pixelSize: 24
            font.bold: true
            color: "#D9D9D9"
            text: obj_LogicContainerAddPluItems.shopPage.newProduct.dataModelShow === 0 ? "$ "+ obj_LogicContainerAddPluItems.shopPage.newProduct.finalPrice+" each" : obj_LogicContainerAddPluItems.shopPage.newProduct.Qprice
        }
    }
    Rectangle{
        width: 398
        height: 249
        x:32
        y:359
        radius: 4
        Text {
            text: "How to add Lookup"
            anchors.horizontalCenter:  parent.horizontalCenter
            y:35
            font.pixelSize: 24
            font.bold: true
        }
        Rectangle{
            width: 90
            height: 88
            x:32
            y:113
            Rectangle{
                width: 32
                height: 32
                x:29
                color: viewset.secondaryColor
                radius: width / 2
                anchors.horizontalCenter: parent.horizontalCenter
                Text{
                    text: "1"
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    color: "white"
                    font.pixelSize: 16
                }
            }
            Text {
                text: "Enter \n product code"
                horizontalAlignment:  TextInput.AlignHCenter
                y:44
                anchors.horizontalCenter: parent.horizontalCenter
                font.pixelSize: 16
            }
        }
        Rectangle{
            width: 53
            height: 88
            x:181
            y:113
            Rectangle{
                width: 32
                height: 32
                x:29
                color: viewset.secondaryColor
                radius: width / 2
                anchors.horizontalCenter: parent.horizontalCenter
                Text{
                    text: "2"
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    color: "white"
                    font.pixelSize: 16
                }
            }
            Text {
                text: "Add \n to Cart"
                horizontalAlignment:  TextInput.AlignHCenter
                y:44
                anchors.horizontalCenter: parent.horizontalCenter
                font.pixelSize: 16
            }
        }
        Rectangle{
            width: 73
            height: 88
            x:293
            y:113
            Rectangle{
                width: 32
                height: 32
                x:29
                color: viewset.secondaryColor
                radius: width / 2
                anchors.horizontalCenter: parent.horizontalCenter
                Text{
                    text: "3"
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                    color: "white"
                    font.pixelSize: 16
                }
            }
            Text {
                text: "Confirm \n Wt or Qty"
                horizontalAlignment:  TextInput.AlignHCenter
                y:44
                anchors.horizontalCenter: parent.horizontalCenter
                font.pixelSize: 16
            }
        }
    }

    Text {
        text: "Recomended"
        x:462
        y:40
        font.pixelSize: 24
        color: "#6D6D6D"

    }
    GridView {
        id: productsgridview
        x:462
        width: 410
        height: 640
        cellWidth: 190 + 22
        cellHeight: 249 + 16
        focus: true
        y: 94
        flow: GridView.FlowTopToBottom
        clip: true
        interactive: false


        model: obj_LogicContainerAddPluItems.shopPage.pluTopFour
        delegate:
            Item {
            Rectangle {
                id: mainrect
                width: 190
                height: 249
                color: "white"
                radius: 4
                MouseArea{
                    anchors.fill: parent
                    onClicked: {
                        obj_LogicContainerAddPluItems.shopPage.item_PLUClicked(model.barcode)
                    }
                }

                Image {
                    id: productimage
                    source: model.pic
                    width: 120
                    height: 120
                    anchors.horizontalCenter: parent.horizontalCenter
                    y: 8
                }

                Text {
                    text: "# "+model.barcode
                    x: 16
                    y: 144
                    font.pixelSize: 16
                    color: "#9D9D9D"
                    lineHeight: Font.Normal
                }
                Text {
                    text: model.name
                    x: 16
                    y: 173
                    font.pixelSize: 24
                    color: "#1D1D1D"
                    lineHeight: Font.Normal
                }

                Text {
                    text: model.Qprice
                    x: 16
                    y: 211
                    font.pixelSize: 20
                    color: "#F08C5A"
                    lineHeight: Font.Normal
                    font.bold: true
                }

            }

        }
    }

    KButton{
        x:700
        y:640
        width: 150
        text: "See All >"
        font.pixelSize: 24
        borderRadius: 5
        onClicked: {
            root.seeAll()
        }
    }

    KButton{
        x:32
        y:640
        width: 120
        text: "< Back"
        borderRadius: 5

        onClicked: {
            obj_LogicContainerAddPluItems.shopPage.back_addPLUItemsClicked()
        }

    }
}
