import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.12
import "../Components"
import "../PopUps"
import KAST.Logic 1.0


Item {
    id: root
    visible: true
    width: 1280
    height: 800

    property Logic obj_LogicServer


    Image {
        id: q
        source: "../../Assets/AuthenticationBackground.png"
        anchors.fill: parent
    }
    Row{
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        spacing: 30

        Rectangle{
            width: 259
            height: 364
            color: "white"
            KProgress{
                id:progressUploadedToServer
                width: 176
                height: 176
                from: 0
                to: 100
                value: 0
                anchors.horizontalCenter: parent.horizontalCenter
                y:40
            }

            KButton{
                id:btn_upload
                y:280
                anchors.horizontalCenter: parent.horizontalCenter
                text: obj_LogicServer.lang.btn_Upload
                width: 179
                height: 44
                btn_color: "#4696FA"
                ishover: false
                borderRadius: 5
                btn_borderWidth: 0
                onClicked: {
                    btn_color = viewset.primaryColor
                    progressUploadedToServer.value = 0
                    progressUploadedToServer.update(0);
                    obj_LogicServer.settingPage.startUploadToServer()
                    btn_download.enabled = false
                    btn_downloadpic.enabled = false
                }
            }
        }
        Rectangle{
            width: 259
            height: 364
            color: "white"
            KProgress{
                id:progressDownloadFromServer
                width: 176
                height: 176
                from: 0
                to: 100
                value: 0
                anchors.horizontalCenter: parent.horizontalCenter
                y:40
            }

            KButton{
                id:btn_download
                y:280
                anchors.horizontalCenter: parent.horizontalCenter
                text: obj_LogicServer.lang.btn_Download
                width: 179
                height: 44
                btn_color: "#4696FA"
                ishover: false
                borderRadius: 5
                btn_borderWidth: 0
                onClicked: {
                    btn_upload.enabled = false
                    btn_color = viewset.primaryColor
                    progressDownloadFromServer.value = 0
                    progressDownloadFromServer.update(0);
                    obj_LogicServer.settingPage.apiHandler.startDownloadFromServer()
                }
            }
        }
        Rectangle{
            width: 259
            height: 364
            color: "white"
            KProgress{
                id:progressDownloadpicFromServer
                width: 176
                height: 176
                from: 0
                to: 100
                value: 0
                anchors.horizontalCenter: parent.horizontalCenter
                y:40
            }

            KButton{
                id:btn_downloadpic
                y:280
                anchors.horizontalCenter: parent.horizontalCenter
                text: obj_LogicServer.lang.btn_Download_Pictures
                width: 200
                height: 44
                ishover: false
                btn_color: "#4696FA"
                borderRadius: 5
                btn_borderWidth: 0
                onClicked: {
                    btn_color = viewset.primaryColor
                    progressDownloadpicFromServer.value = 0
                    progressDownloadpicFromServer.update(0);
                    obj_LogicServer.settingPage.updateFiles.startDownload()
                }
            }
        }
    }

    TopNav{
        backvisible: true
        onBackClicked: {
            stackview.pop()
        }
    }
    FullMessageTimer{
        id:fmessagetimer
    }

    Connections{
        target: obj_LogicServer.settingPage
        function onUpdateUploadToServerSignal(v){
            progressUploadedToServer.update(v);
            if(v>95){

                btn_download.enabled = true
                btn_downloadpic.enabled = true
                btn_upload.btn_color = "#4696FA"
                fmessagetimer.messageText = "upload Completed"
                fmessagetimer.open()
            }
        }
    }
    Connections{
        target:obj_LogicServer.settingPage.apiHandler
        function onUpdateDownloadedFromServerValue(v){
            progressDownloadFromServer.update((v-1) * 25);
            if(v === 5 ){
                btn_upload.enabled = true
                btn_download.btn_color = "#4696FA"
                //cameraProvider.stop()
            }
        }

        function onShowMessageTimer(str){
            fmessagetimer.messageText = str
            fmessagetimer.open()
            btn_download.btn_color = "#4696FA"
            btn_upload.btn_color = "#4696FA"
            btn_downloadpic.btn_color = "#4696FA"
        }

    }
    Connections{
        target:obj_LogicServer.settingPage.updateFiles
        function onSetTotalProgressSignal(v){
            progressDownloadpicFromServer.to = v
        }
        function onSetCurrentProgressSignal(v){
            progressDownloadpicFromServer.update(v)
            if(v>95){
                btn_downloadpic.btn_color = "#4696FA"
            }
        }
        function onShowMessageTimer(str){
            fmessagetimer.messageText = str
            fmessagetimer.open()
            btn_download.btn_color = "#4696FA"
            btn_upload.btn_color = "#4696FA"
            btn_downloadpic.btn_color = "#4696FA"
        }
    }
}
