import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.12
import QtQuick.Window 2.14
import "../Components"
//import KAST.Logic 1.0


Item{
    id: root
    visible: true
    width: 1280
    height: 800

    property QtObject obj_Logic


    Image {
        id: q
        source: "../../Assets/AuthenticationBackground.png"
        anchors.fill: parent
    }

    Rectangle {
        width: 672
        height: 104
        radius: 4
        color: "white"
        x: 304
        y: 312
        layer.enabled: true
        layer.effect: DropShadow {
            horizontalOffset: 1
            verticalOffset: 1
            radius: 10
            samples: 16
            color: "#d3d3d3"
        }
        Behavior on height {
            NumberAnimation{duration: 500}
        }

        Text {
            text: obj_Logic.lang.txt_Software_Version
            font.pixelSize: 20
            color: "black"
            x: 24
            y: 24
        }

        Text {
            id:txt_newversionid
            text: obj_Logic.settingPage.lastSoftwareVersion + obj_Logic.lang.txt_is_available
            font.pixelSize: 20
            color: "#9D9D9D"
            x: 24
            y: 58
        }


        KBorderButton{
            id:btn_download
            width: 244
            height: 50
            x: 404
            y: 27
            pixelSize: 20
            textColor: "#4696FA"
            bordercolor: "#4696FA"
            text: obj_Logic.lang.btn_Download_and_install
            MouseArea{
                anchors.fill: parent
                onClicked: {
                    parent.parent.height =132
                    btn_download.visible = false
                    txt_newversionid.visible = false
                    progressBar.visible = true
                    txt_percentage.visible = true
                    obj_Logic.settingPage.updateSoftware.startDownload()
                }
            }

        }

        ProgressBar {
            id:progressBar
            from: 0
            to: 100
            x:24
            y:89
            width: 524
            height: 5
            visible: false
            background: Rectangle {
                anchors.fill: progressBar
                color: "white"
                radius: 4
                border.width: 0
                border.color: "white"
            }
            contentItem:
                Item {
                implicitWidth: 200
                implicitHeight: 4
                Rectangle {
                    anchors.left: progressBar.left
                    anchors.bottom: progressBar.bottom
                    height: progressBar.height
                    width: progressBar.width * (progressBar.value /100)
                    color: "#4696FA"
                    radius: 4
                }

            }
        }
        Text {
            id:txt_percentage
            visible: false
            x:605
            y:78
            text: qsTr(progressBar.value *100 + "%")

            font.pixelSize: 20
            color:  "#4696FA"
            font.bold: true
        }
    }

    TopNav{
        backvisible: true
        onBackClicked: {
            stackview.pop()
        }

    }
    Connections{
            target: obj_Logic.settingPage.updateSoftware
            onSetTotalProgressSignal:{
                //btn1.enabled = false
                //btn1.opacity = 0.5
                progressBar.to = v
            }
            onSetCurrentProgressSignal:{
                progressBar.value = v
            }
            onSucceededSignal:{
                //btn1.enabled = true
                //btn1.opacity = 1
            }
        }

}





