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
            text: obj_LogicContainerAddPluItems.shopPage.newProduct.finalPriceQML
        }
    }
    Rectangle{
        width: 398
        height: 249
        x:32
        y:359
        radius: 4
        Text {
            text: obj_LogicContainerAddPluItems.lang.txt_How_to_add_Lookup
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
                text: obj_LogicContainerAddPluItems.lang.txt_Enter_product_code
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
                text: obj_LogicContainerAddPluItems.lang.txt_Add_to_Cart
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
                text: obj_LogicContainerAddPluItems.lang.txt_Confirm_Wt_or_Qty
                horizontalAlignment:  TextInput.AlignHCenter
                y:44
                anchors.horizontalCenter: parent.horizontalCenter
                font.pixelSize: 16
            }
        }
    }

    Text {
        text: obj_LogicContainerAddPluItems.lang.txt_Recomended
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
                    width: 110
                    height: 110
                    anchors.horizontalCenter: parent.horizontalCenter
                    y: 8
                }

                Text {
                    text: "# "+model.barcode
                    x: 16
                    y: 134
                    font.pixelSize: 16
                    color: "#9D9D9D"
                    lineHeight: Font.Normal
                }
                Text {
                    text: model.name
                    width: parent.width -16
                    elide: Text.ElideRight
                    x: 16
                    y: 163
                    font.pixelSize: 24
                    color: "#1D1D1D"
                    lineHeight: Font.Normal
                }

                Text {
                    text: model.savingQML
                    x: 16
                    y: 198
                    font.pixelSize: 10
                    color: "#36EB00"
                    lineHeight: Font.Normal
                    font.bold: true
                }

                Text {
                    text: model.finalPriceQML
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
        text: obj_LogicContainerAddPluItems.lang.btn_See_All +" >"
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
        text: "< " + obj_LogicContainerAddPluItems.lang.btn_Back
        borderRadius: 5

        onClicked: {
            root.back()
            obj_LogicContainerAddPluItems.shopPage.back_addPLUItemsClicked()

        }

    }
}
