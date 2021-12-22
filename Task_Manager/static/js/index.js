// when the page loads
document.addEventListener("DOMContentLoaded", () => {
    document.querySelector('form').onsubmit = () => {
        // create a li and set the inner html to the value of the text input
        const li = document.createElement('li');
        li.innerHTML = document.querySelector("#taskInput").value;
        // create a button and give it some css
        const button = document.createElement('button');
        button.className = 'bi bi-x-circle-fill change';
        button.style.color = "#FF0000";
        button.style.background = "unset";
        button.style.cursor = 'pointer';
        button.style.border = 'unset';
        button.style.margin = 'unset';
        button.style.padding = 'unset';
        button.style.textAlign = 'center'

        // create an ajax POST request to the server, where the server will add it to the model
        $.ajax({
            type:'POST',
            url: sURL,
            data: {
                username: username,
                text:document.querySelector("#taskInput").value,
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function(data){
                // append the button to the li and li to the list
                button.id = data.id;
                li.appendChild(button);
                const div = document.createElement('div')
                div.innerHTML = `<div class="todo-item"> <button style="color:red"class="bi bi-x-circle-fill change" id="${data.id}"></button> <span>${document.querySelector("#taskInput").value}</span> </div>`
                document.querySelector("#todo-list").append(div);
                // clear the input field
                document.querySelector("#taskInput").value = "";
            }
        })

        // don't allow the form to submit
        return false;
    }
    document.addEventListener('click', event => {
        const elem = event.target;
        if (elem.className.includes("change")) {
            $.ajax({
                type:"POST",
                url: URLc,
                data:{
                    id: elem.id,
                    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
                }, success: function(data){
                    if (data.done == true) {
                        elem.className = 'bi bi-check-circle-fill change';
                        elem.style.color = "#007500";
                    } else {
                        elem.className = 'bi bi-x-circle-fill change';
                        elem.style.color = "#FF0000";
                    }
                }
            })
        }
    })
})