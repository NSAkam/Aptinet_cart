import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import "Components"
import "Utiles" as Util
import KAST.Logic 1.0





Item {
    
    width: 1280
    height: 800
    property Logic obj_LogicContainerTowStepAuthentication
    
    
    Util.ViewSettings{
        id:viewset
    }
    
    
    
    Image {
        source: "../Assets/AuthenticationBackground.png"
        anchors.fill: parent
    }
    
    Image {
        anchors.top: parent.top
        anchors.left: parent.left
        source: "../Assets/NavBar.png"
    }
    Rectangle{
        id:imgUser
        width: 300
        height: 300
        x:490
        y:135
        color: viewset.primaryColor
        radius: 390/2
        border.width: 20
        border.color: "#D9D9D9"
        Image {
            source: "../Assets/FaceScanning.png"
            anchors.fill: parent
        }
        Behavior on width {
            NumberAnimation{duration: 500}
        }
        Behavior on height {
            NumberAnimation{duration: 500}
        }
        Behavior on x {
            NumberAnimation{duration: 500}
        }
        Behavior on y {
            NumberAnimation{duration: 500}
        }
        Behavior on border.width {
            NumberAnimation{duration: 500}
        }
    }
    
    
    Text {
        id:txt_enterPhone
        text: qsTr(obj_LogicContainerTowStepAuthentication.shopPage.user.loggedInUser.phone)
        anchors.horizontalCenter: parent.horizontalCenter
        y:508
        font.pixelSize: 24
        font.bold: true
        Behavior on width {
            NumberAnimation{duration: 500}
        }
        Behavior on height {
            NumberAnimation{duration: 500}
        }
        Behavior on x {
            NumberAnimation{duration: 500}
        }
        Behavior on y {
            NumberAnimation{duration: 500}
        }
    }
    
    KButton{
        id:btn_Continue
        text: "START SHOPPING"
        fontsize: 24
        anchors.horizontalCenter: parent.horizontalCenter
        width: 351
        y:566
        height: 66
        borderRadius: 5
        onClicked: {
            stackview.push(shoppage)
        }
    }
    
    TopNav{
        id:topnavbar
        backvisible: true
        onBackClicked: {
            stackview.pop()
        }
    }
    
    Component{
        id:shoppage
        Shop{
            
        }
    }
}
