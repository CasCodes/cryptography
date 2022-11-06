$(".alert").hide()

function getSelections() {
    // flip switch checkbox
    if (document.getElementById("customToggle2").checked){
        console.log("encrypt")
    }
    else {
        console.log("decrypt")
    }
    var encrypt = document.getElementById("customToggle2").checked

    // select dropdown
    var drop = document.getElementById("modeMenu");
    var method = drop.options[drop.selectedIndex].text;
    console.log(method)

    // message
    var msg = document.getElementById("form-2-message").value;
    console.log(msg)    

    // key
    var key = document.getElementById("form-2-key").value;
    console.log(key)

    // check if inputs are of valid type
    if (method == 'Cesar') {
        key = parseInt(key)
        // only allow int for cesar
        if (!Number.isInteger(key)) {
            // display error message
            $('.alert').show()
            return
        }
    }
    if (method == 'Vigenere'){
        // TODO only allow string for vigenere
        // why doesnt this regrex work??
        console.log("is msg alpha?", /[^a-zA-Z]/.test(msg))

        if (!/[^a-zA-Z]/.test(msg)) {
            $('.alert').show()
            console.log('hit me daddy make me beg')
            return
        }
    }
    $(".alert").hide()

    // call python
    data = {
        'encrypt': encrypt,
        'method': method,
        'message': msg,
        'key': key
    }
    console.log(JSON.stringify(data))
    fetch("/data", {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(rb => {
        // send text to widget
        console.log(rb);
    });

    // open modal (result popup)
    $(".modal").modal()
}