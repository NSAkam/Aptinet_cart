import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.12


Window {
    width: 1280
    height: 800
    visible: false
    title: qsTr("Menu Test - 1")
    id: root

    StackView {
        id: stackview
        anchors.fill: parent
        initialItem: splashdisabledPage
    }

    Component {
        id: splashdisabledPage
        Splash_Disable {
            id: sdPage
            taptostartbtn.onClicked: {
                stackview.push(splashenabledPage)
//                stackview.replace(splashdisabledPage, splashenabledPage)
            }
        }

    }

    Component {
        id: splashenabledPage
        Splash_Enable {
            id: sePage
            settingsbtn.onClicked: {
                stackview.push(menutest)
            }

        }

    }

    Component {
        id: menutest
        Menu_Test {
            id: mt
        }
    }

}


