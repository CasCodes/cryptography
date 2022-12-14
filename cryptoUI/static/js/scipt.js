$(".alert").hide()
// private, public
keys = [[22499,7081],[22499,5521]]

// displays the encryption/decryption result on screen
function displayResult(text) {
    div = document.getElementById('modal-text');
    div.textContent = text;

    // TODO deal with too long result (rsa)
    // open modal (result popup)
    $(".modal").modal()
}

// copies the result to clipboard
function copyToClipboard() {
    div = document.getElementById('modal-text');
    navigator.clipboard.writeText(div.textContent)
    console.log(div.textContent)
}

function displayKeys(k) {
    // display public keypair
    keyfield = document.getElementById('public-key-field')
    keyfield.textContent = keys[1]
}

function callBackend(data) {
        // call python
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
            // return response
            if (data['method'] == 'KEYS') {
                // save keypair
                keys[0] = rb['result']['private']
                keys[1] = rb['result']['public']
                displayKeys(keys)
            }
            // display on frontend
            else {
                displayResult(rb['result'])
            }
             
        });
}
// call backend for new RSA key pairs & display on frontend
function generateKeys() {
    // send message to backend requesting keys
    data = {
        'method': 'KEYS'
    }
    callBackend(data)
}

// triggers when a new selection is made in the select menu
function changeOptions(selector) {
    selected = (document.getElementById(selector)).value
    rsaSec = document.getElementById('RSAcontainer')
    keyIn = document.getElementById('key-inputs')

    // show RSA section when 3 is selected
    if (selected == 3) {
        // show Keys field
        rsaSec.style.display = 'block'
        // hide key input
        keyIn.style.display = 'none'
    }
    // else hide
    else {
        // hide Keys field
        rsaSec.style.display = 'none'
        // show key input
        keyIn.style.display = 'block'
    }
}

// fetches the selections of each input field
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
    if (method == 'RSA') {
        var key = keys
    }
    else {
        var key = document.getElementById("form-2-key").value
    }
    console.log(key)

    // check if inputs are of valid type
    if (method == 'Caesar') {
        key = parseInt(key)
        // only allow int for cesar
        if (!Number.isInteger(key)) {
            // display error message
            $('.alert').show()
            return
        }
    }
    if (method == 'Vigenere'){
        // only allow alphabetic string for vigenere
        if (/^[a-zA-Z]+$/.test(key) == false) {
            $('.alert').show()
            return
        }
    }
    $(".alert").hide()

    data = {
        'encrypt': encrypt,
        'method': method,
        'message': msg,
        'key': key
    }
    // fetch result from backend
    callBackend(data)
}
// display default key
displayKeys(keys)