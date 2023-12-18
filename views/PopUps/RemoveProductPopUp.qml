import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import QtQuick.Window 2.0
import "../Components"
import "../Containers"
import "../Utiles"
import KAST.Logic 1.0


Popup {
    id: root
    width: 1280
    height: 800
    modal: true
    focus: true

    property Logic obj_logicRemoveProductList

    Component.onCompleted: {
        txt_BarCodeInput.text = ""
    }
    onOpened: {
        txt_BarCodeInput.text = ""
    }


    background:
        Rectangle {
        color: "black"
        opacity: 0.4
        x: 0
        y: 0
        width: parent.width
        height: parent.height
    }

    Rectangle {
        x: 818 + 390
        y: 32
        radius: 4
        color: "white"
        width: 40
        height: 40

        Image {
            source: "../../Assets/alarm.png"
            width: 18
            height: 20
            anchors.centerIn: parent
        }
    }


    Column {
        spacing: 16
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        Rectangle {
            id: notifrect
            width: 1000
            height: 72
            radius: 4

            LinearGradient {
                anchors.fill: parent
                start: Qt.point(0, 10)
                end: Qt.point(72, 60)
                gradient: Gradient {
                    GradientStop { position: 0.5417; color: "#F08C5A" }
                    GradientStop { position: 1.0; color: "#F05A28" }
                }
            }

            Text {
                anchors.fill: notifrect
                text: obj_logicRemoveProductList.lang.txt_Are_you_sure_to_remove_the_products
                font.bold: true
                font.pixelSize: 24
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                color: "white"
            }
        }

        Rectangle{
            width:1000
            height: 400
            color: "transparent"

            Rectangle{
                width: 758
                height: parent.height



                Rectangle{
                    id:rectEnterBarcode
                    y:10
                    anchors.horizontalCenter: parent.horizontalCenter
                    width: 417
                    height: 54
                    color: "#F1F1F1"
                    radius: 4
                    TextInput{
                        id:txt_BarCodeInput
                        anchors.fill: parent
                        font.pixelSize: 18
                        layer.enabled: true
                        horizontalAlignment: TextInput.AlignHCenter
                        verticalAlignment:  TextInput.AlignVCenter
                        font.family: viewset.danaFuNumFont
                        property string placeholderText: "Enter Barcode"

                        onFocusChanged: {
                            numpad.inputtext = txt_BarCodeInput
                            numpad.visible = true
                        }
                        Text {
                            text: txt_BarCodeInput.placeholderText
                            color: "#C6C5CE"
                            visible: !txt_BarCodeInput.text
                            font.pixelSize: 18
                            anchors.verticalCenter: parent.verticalCenter
                            anchors.horizontalCenter: parent.horizontalCenter
                            font.family: viewset.danaFuNumFont
                        }
                    }
                }


                ListView {
                    id:slideshow
                    width: 758
                    height: 210
                    clip: true
                    spacing: 10
                    model: 10
                    y:60
                    orientation: ListView.vertical
                    delegate:Item{
                        width: 758
                        height: 140
                        Rectangle {
                            anchors.fill: parent
                            color: "white"
                            Image {
                                source: model.pic
                                x: 41
                                y: 41
                                width: 90
                                height: 90
                            }
                            Text {
                                text: model.name
                                x: 180
                                y: 40
                                font.pixelSize: 24
                                font.weight: Font.DemiBold
                                color: "black"
                                font.letterSpacing: 0.04 * 24
                                lineHeight: 1.5
                            }

                            Text {
                                text: "Qty:"
                                x: 545
                                y: 48
                                font.pixelSize: 20
                                //              font.weight: Font.DemiBold
                                color: "#6D6D6D"
                            }

                            Text {
                                text: model.countInBasket
                                x: 595
                                y: 45
                                font.pixelSize: 24
                                font.weight: Font.Bold
                                color: "#F08C5A"
                            }
                            KButton{
                                visible: model.productType === "counted" ? true:false
                                width: 35
                                height: 35
                                text: "-"
                                x: 625
                                y: 45
                                onClicked: {
                                    obj_logicRemoveProductList.shopPage.product_removeDecreaseClicked(index)
                                }
                            }
                            KButton{
                                visible: model.productType === "counted" ? true:false
                                text: "+"
                                width: 35
                                height: 35
                                x: 665
                                y: 45
                                onClicked: {
                                    obj_logicRemoveProductList.shopPage.product_removeIncreaseClicked(index)
                                }
                            }

                            //                        Text {
                            //                            text: model.finalPrice
                            //                            x: 615
                            //                            y: 102
                            //                            font.pixelSize: 24
                            //                            font.weight: Font.Bold
                            //                            color: viewset.primaryColor
                            //                        }


                        }
                    }
                }
                KButton{
                    text: obj_logicRemoveProductList.lang.btn_Confirm
                    borderRadius: 4
                    height: 64
                    width: 726
                    anchors.horizontalCenter: parent.horizontalCenter
                    y:290
                    btn_color: viewset.secondaryColor
                    btn_borderWidth: 0
                    onClicked: {
                        obj_logicRemoveProductList.shopPage.product_removeConfirmClicked()
                    }
                }
                Numpad{
                    id:numpad
                    visible: false
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.top: rectEnterBarcode.bottom
                    onEnter: {
                        obj_logicRemoveProductList.shopPage.product_removeManualBarcodeEntered(txt_BarCodeInput.text)
                        numpad.visible = false

                    }
                }
            }

            Rectangle{
                width: 245
                height: parent.height
                anchors.right: parent.right
                color: "transparent"

                GridView {
                    id: productsgridview
                    anchors.horizontalCenter: parent.horizontalCenter
                    width: 190 + 30
                    height: parent.height
                    cellWidth: 190 + 22
                    cellHeight: 249 + 16
                    focus: true

                    flow: GridView.FlowLeftToRight
                    clip: true
                    interactive: true


                    model:obj_logicRemoveProductList.shopPage.removeLookupList
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
                                    obj_logicRemoveProductList.shopPage.product_removeLookupSelected(model.barcode)
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
            }
        }
    }
}
