// function for checking if the passwords match and if the fields are not empty
function match(password, password2, login){
    if(password.value == password2.value) {
        if (password.value != "" && password2.value != "" && login.value != ""){
            // hide the match and noPas text and make the button available
            document.querySelector("#match").style.display = "none";
            document.querySelector("#noPas").style.display = "none";
            document.querySelector("#sign").disabled = "";
        } else {
            // hide the match text, show the noPas text and disable the button
            document.querySelector("#match").style.display = "none";
            document.querySelector("#noPas").style.display = "block";
            document.querySelector("#sign").disabled = "disabled";
        }
    } else {
        if (password.value != "" && password2.value != "" && login.value != ""){
            // hide the noPas text
            document.querySelector("#noPas").style.display = "none";
        } else {
            // show the noPas text
            document.querySelector("#noPas").style.display = "block";
        };
        // show the match text and disable the button
        document.querySelector("#match").style.display = "block";
        document.querySelector("#sign").disabled = "disabled";
    };
};

// when the page is loaded, get the passwords
window.addEventListener('DOMContentLoaded', (event) => {
    const log = document.querySelector("#login");
    const pas = document.querySelector("#password");
    const pas2 = document.querySelector("#password2");
    // check if the passwords match
    setInterval( () => {
        match(pas, pas2, log);
    },300);
});
