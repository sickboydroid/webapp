let formMyForm = document.getElementById("myForm")
let btnSendData = document.getElementById("send-data")
let cbPostRequest = document.getElementById("post-request")
let nameUserName = document.getElementById("user-name")
btnSendData.addEventListener("click", function() {
    let postRequest = cbPostRequest.checked
    console.log("Checked: " + postRequest)
    console.log("Username: " + nameUserName.value)
    if(postRequest)
        formMyForm.setAttribute("method", "post")
    else
        formMyForm.setAttribute("method", "get")
})

