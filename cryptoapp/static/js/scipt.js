
function getSelections() {
    // flip switch checkbox
    if (document.getElementById("customToggle2").checked){
        console.log("encrypt")
    }
    else {
        console.log("decrypt")
    }

    // select dropdown
    var drop = document.getElementById("modeMenu");
    var value = drop.options[drop.selectedIndex].value;
    var text = drop.options[drop.selectedIndex].text;
    console.log(value, text)

    // message
    var msg = document.getElementById("form-2-message")
    console.log(msg.value)    

    // key
    var key = document.getElementById("form-2-key")
    console.log(key.value)

    // call python
    $.ajax({
        type: "POST",
        url: "connect/",
        data: { param: text}
      }).done(function( o ) {
         // do something
      });
}