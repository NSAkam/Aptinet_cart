import QtQuick 2.15
import QtQuick.Controls 2.15



Item {

    width: 1280
    height: 462


    id:obj
    property int leftpad:0
    property int toppad: 0
    property TextEdit inputtext
    y:mainwindow.height - loader.height - toppad
    x:(mainwindow.width / 2) - (loader.width / 2) - leftpad
    Rectangle{
        id:obj_keyboard
        color: "red"
        Loader{
            asynchronous: true
            id:loader
            sourceComponent: lowerkeyboard
        }
        Component {
            id: lowerkeyboard
            KkeyboardEnLowerCase{
                id:keyboard
                onShiftClicked:function (state) { parent.parent.keyboardState(state) }
                onInput:function (key){inputtext.text = inputtext.text + key}
                onBackspace: function (){inputtext.text = inputtext.text.slice(0,-1)}
                onClose: function (){
                    obj.visible=false
                    //obj.destroy()
                }
            }
        }
        Component {
            id: upperkeyboard
            KkeyboardEnUpperCase{
                id:keyboard
                onShiftClicked:function (state) { parent.parent.keyboardState(state) }
                onInput:function (key){inputtext.text = inputtext.text + key}
                onBackspace: function (){inputtext.text = inputtext.text.slice(0,-1)}
                onClose: function (){
                    obj.visible=false
                    //obj.destroy()
                }
            }
        }
        Component {
            id: functionkeyboard
            KkeyboardFn{
                id:keyboard
                onShiftClicked:function (state) { parent.parent.keyboardState(state) }
                onInput:function (key){inputtext.text = inputtext.text + key}
                onBackspace: function (){inputtext.text = inputtext.text.slice(0,-1)}
                onClose: function (){
                    obj.visible=false
                    //obj.destroy()
                }
            }
        }

        function keyboardState(v:int)
        {
            if(v === 1)
            {
                loader.sourceComponent = upperkeyboard
            }
            else if(v === 2)
            {
                loader.sourceComponent = lowerkeyboard
            }
            else if(v === 3)
            {
                loader.sourceComponent = functionkeyboard
            }
        }
    }

}
