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
                y:280
                anchors.horizontalCenter: parent.horizontalCenter
                text: "Upload"
                width: 179
                height: 44
                btn_color: "#4696FA"
                borderRadius: 5
                btn_borderWidth: 0
                onClicked: {
                    obj_LogicServer.startUploadToServer()
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
                y:280
                anchors.horizontalCenter: parent.horizontalCenter
                text: "Download"
                width: 179
                height: 44
                btn_color: "#4696FA"
                borderRadius: 5
                btn_borderWidth: 0
                onClicked: {
                    obj_LogicServer.settingPage.apiHandler.startDownloadFromServer()
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
    
    Connections{
        target: obj_LogicServer.settingPage
        onUpdateUploadToServerSignal:{
            progressUploadedToServer.update(value);
        }
    }
    Connections{
        target:obj_LogicServer.settingPage.apiHandler
        onUpdateDownloadedFromServerValue:{
            progressDownloadFromServer.update(value * 25);
        }
    }
}
