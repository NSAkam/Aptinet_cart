import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.12
import QtQuick.Window 2.14
import "../Components"
import "../PopUps"
//import KAST.Logic 1.0





Item {
    id: root
    visible: true
    width: 1280
    height: 800

    property QtObject setting_objWifi


    Image {
        source: "../../Assets/AuthenticationBackground.png"
        anchors.fill: parent
    }

    Rectangle{
        width: 725
        height: 74
        color: "white"
        y:182
        anchors.horizontalCenter: parent.horizontalCenter
        radius: 12
        Image {
            source: "../../Assets/tik.png"
            x:24
            anchors.verticalCenter: parent.verticalCenter
        }
        Text {
            text: qsTr(setting_objWifi.settingPage.wifimodel.SSID)
            x:71
            anchors.verticalCenter: parent.verticalCenter
            font.pixelSize: 24
        }
        Text {
            id: name
            text: qsTr("IP: " + setting_objWifi.settingPage.wifimodel.IP)
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            font.pixelSize: 18
            color: "gray"
        }
//        Text {
//            text: qsTr("Signal Level: " + "24")
//            x:503
//            anchors.verticalCenter: parent.verticalCenter
//            font.pixelSize: 20
//            color: "gray"
//        }
        Image {
            source: "../../Assets/wifi1.png"
            x:662
            anchors.verticalCenter: parent.verticalCenter
        }
    }

    Rectangle{
        width: 725
        height: 296
        y:304
        radius: 4
        anchors.horizontalCenter: parent.horizontalCenter

        Component {
            id: appDelegate
            Item {
                height:74
                width:725
                Rectangle{
                    anchors.fill: parent
                    color: "transparent"
                    MouseArea{
                        anchors.fill: parent
                        onClicked: {
                            setting_objWifi.settingPage.wifimodel.selectedWifi(index);
                            popup_SetPasssword.open();
                        }
                    }

                    Label{
                        id:txt_data
                        anchors.verticalCenter: parent.verticalCenter
                        text: model.ESSID
                        font.pixelSize: 24
                        x:36
                    }

                    Rectangle{
                        width: parent.width
                        height: 1
                        color: "gray"
                        anchors.bottom: parent.bottom
                    }
                    Image {
                        source: "../../Assets/wifi1.png"
                        x:662
                        anchors.verticalCenter: parent.verticalCenter
                    }
                }
            }
        }

        ListView{
            id:lst_wifis
            anchors.fill: parent
            focus: true
            model: setting_objWifi.settingPage.wifimodel
            delegate: appDelegate
            clip: true
            currentIndex: -1
            //onCurrentIndexChanged: console.log( "Current Index: "+currentIndex )
        }
    }


    TopNav{
        backvisible: true
        onBackClicked: {
            setting_objWifi.settingPage.backFromWifiSettigs()
            stackview.pop();
        }

    }
    InsertWifiPassword{
        id:popup_SetPasssword
        setting_obj:setting_objWifi
    }
}







