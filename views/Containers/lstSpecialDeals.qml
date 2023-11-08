import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import "../Components"
//import KAST.Logic 1.0



Item {
    id:lstFactor
    property QtObject tanzimat

    anchors.fill: parent

    Component{
        id:factorDelegate


        Item {
            id: itemFactorItem
            x:5
            width: 640
            height: 90
            Component.onCompleted:{
                if(1==1){
                    visible = true
                }
            }

            Rectangle{
                id:rectFactorItem
                anchors.fill: parent
                radius: 20

                Image {
                    id: factorItemPic
                    source: "/home/kast/pics/" + model.QRCode + ".png"
                    anchors.right: parent.right
                    anchors.top: parent.top
                    width: 75
                    height: 75
                    anchors.topMargin: 7
                    anchors.rightMargin: 20
                }
                Label {
                    id: factorItemName
                    text: md.name
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
                Label {
                    id: factorItemPrice
                    text: model.price + "هرعدد"
                    font.family: viewset.danaFuNumFont
                    font.pixelSize: 16
                    anchors.right: factorItemPic.left
                    y:54
                    anchors.rightMargin: 20
                    elide: Text.ElideRight
                    color: "#A3A2B3"
                }
                Rectangle{
                    width: 1
                    height: 12
                    color: "#A3A2B3"
                    anchors.right: factorItemPrice.left
                    y:58
                    anchors.rightMargin: 6
                }
                Label {
                    id: lblFactorItemCount
                    text: "تعداد"
                    font.family: viewset.danaFuNumFont
                    font.pixelSize: 16
                    anchors.right:  factorItemPrice.left
                    y:54
                    anchors.rightMargin: 17
                    elide: Text.ElideRight
                    color: "#A3A2B3"
                }
                Rectangle {
                    id: rectFactorItemPercentage
                    anchors.right:  lblFactorItemCount.left
                    y:54
                    anchors.rightMargin: 9
                    color: "#F2C335"
                    width: 25
                    height: 25
                    radius: 50
                    Label {
                        text: model.tedad
                        anchors.horizontalCenter: parent.horizontalCenter
                        font.family: viewset.danaFuNumBoldFont
                        y:3
                        font.pixelSize: 14
                        font.bold: true
                        //anchors.right:  factorItemPrice.left
                        elide: Text.ElideRight
                        color: "white"
                    }
                }
                Rectangle{
                    width: 54
                    height: 26
                    color: "#E45F2B"
                    radius: 50
                    x:150
                    y:31
                    Label {
                        text: (100-((model.finalprice*100)/model.price)).toFixed(0) + "%"
                        anchors.horizontalCenter: parent.horizontalCenter
                        font.family: viewset.danaFuNumBoldFont
                        y:3
                        font.pixelSize: 14
                        font.bold: true
                        //anchors.right: factorItemPrice.left
                        elide: Text.ElideRight
                        color: "white"
                    }
                }
                Label {
                    id: factorItemTotalPrice
                    text:  "99999999 ریال"
                    font.family: viewset.danaFuNumFont
                    font.pixelSize: 18
                    x:20
                    y:30
                    elide: Text.ElideRight
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
    Component{
        id:factorChangedDelegate


        Item {
            id: itemfactorInfoDelegate
            x:5
            width: 640
            height: 94
            Rectangle{
                color: "#E45F2B"
                anchors.fill: parent
                radius: 20
                Rectangle{
                    color: "white"
                    width: 570
                    height: parent.height - 4
                    anchors.right: parent.right
                    radius: 20
                    anchors.rightMargin: 2
                    anchors.verticalCenter: parent.verticalCenter
                    Image {
                        id: factorItemChangePic
                        source: "../../Assets/adbanner.png"
                        anchors.verticalCenter: parent.verticalCenter
                        width: 75
                        height: 75
                        anchors.right: parent.right
                        anchors.topMargin: 7
                        anchors.rightMargin: 18
                        Rectangle{
                            color: "#E45F2B"
                            height: 27
                            width: parent.width + 20
                            radius: 20
                            anchors.verticalCenter: parent.verticalCenter
                            anchors.horizontalCenter: parent.horizontalCenter
                            Text {
                                text: qsTr("تغییر موجودی")
                                font.family: viewset.danaFuNumBoldFont
                                anchors.verticalCenter: parent.verticalCenter
                                anchors.horizontalCenter: parent.horizontalCenter
                                color: "white"
                            }
                        }
                    }
                    Label {
                        id: factorItemChangeName
                        text: "صابونننننننننننننننننننننننسیشسیشبسیبسییشبسیببطببیطبلبسیب"
                        font.family: viewset.danaFuNumFont
                        font.pixelSize: 16
                        anchors.right: factorItemChangePic.left
                        anchors.top: parent.top
                        width: 222
                        height: 75
                        anchors.topMargin: 15
                        anchors.rightMargin: 20
                        elide: Text.ElideRight
                    }
                    Rectangle{
                        id: rectfactorItemChangeTedad
                        radius: 50
                        color: "#F2C335"
                        width: 25
                        height: width
                        anchors.right: factorItemChangeName.left
                        anchors.top: factorItemChangeName.top
                        Text {
                            id: factorItemChangeTedad
                            text: qsTr("5")
                            font.family: viewset.danaFuNumFont
                            anchors.verticalCenter: parent.verticalCenter
                            anchors.horizontalCenter: parent.horizontalCenter
                            font.pixelSize: 14
                            color: "white"

                        }
                    }
                    Label {
                        id: factorItemChangePrice
                        text: "هرعدد 2000"
                        font.family: viewset.danaFuNumFont
                        font.pixelSize: 16
                        anchors.right: factorItemChangePic.left
                        y:54
                        anchors.rightMargin: 20
                        elide: Text.ElideRight
                        color: "#A3A2B3"
                    }
                    Label {
                        text: "تعداد قابل خرید"
                        font.family: viewset.danaFuNumFont
                        font.pixelSize: 16
                        anchors.right: factorItemChangePrice.left
                        y:54
                        anchors.rightMargin: 20
                        elide: Text.ElideRight
                        color: "#A3A2B3"
                    }
                    Rectangle{
                        radius: 50
                        color: "#E45F2B"
                        width: 25
                        height: width
                        anchors.left: rectfactorItemChangeTedad.left
                        anchors.top: factorItemChangePrice.top
                        Text {
                            id: factoreItemChangeCanSell
                            text: qsTr("5")
                            font.family: viewset.danaFuNumFont
                            anchors.verticalCenter: parent.verticalCenter
                            anchors.horizontalCenter: parent.horizontalCenter
                            font.pixelSize: 14
                            color: "white"

                        }
                    }
                    Label{
                        anchors.top: factorItemChangeName.top
                        x:26
                        text: "مبلغ قابل پرداخت"
                        font.family: viewset.danaFuNumFont
                        elide: Text.ElideRight
                            font.pixelSize: 16
                            Label{
                                text: "0" + "تومان"
                                anchors.horizontalCenter: parent.horizontalCenter
                                y:35
                            }
                    }
                }
                Text {
                   text: "×4"
                   font.pixelSize: 32
                   font.family: viewset.danaFuNumFont
                    x:18
                    color: "white"
                    Text{
                        text: "از سبد\nکسر شود"
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        font.pixelSize: 15
                        font.family: viewset.danaFuNumFont

                        color: "white"
                        x:-9
                        y:parent.height -10

                    }
                }
            }

        }
    }

    ListView {
        id:lst_prd
        spacing: 5
        anchors.fill: parent
        focus: true
        model: contactsModel
        delegate:  Loader {
            id:loaderChooser
            property variant modelData: model

            sourceComponent:  switch(name) {
                              case 1: return factorDelegate
                              case 2: return factorChangedDelegate
                              }
        }

        clip: true
        currentIndex: -1
        cacheBuffer: 10000
        smooth: true
        antialiasing: true
        snapMode: ListView.SnapOneItem


        ListModel {
            id: contactsModel
            ListElement {
                name: 1
                position: "Engineer"
            }
            ListElement {
                name: 2
                position: "Engineer"
            }
            ListElement {
                name: 3
                position: "Manager"
            }
        }

    }
}


