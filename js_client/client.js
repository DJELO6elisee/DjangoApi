const loginForm = document.getElementById('login-form');
const baseEndpoint = "http://localost:8001/api"


if (loginForm){
    loginForm.addEventListener('submit', handlelogin);
}

function handlelogin(event){
    event.preventDefault();
    const loginEndpoint = `${baseEndpoint}/token/`;
    let loginFormData = new FormData(loginForm);

    let loginObjectData = Object.fromEntries(loginFormData);
    let bodyJsonData = JSON.stringify(loginObjectData);

    const options = {
        method:"POST",
        headers:{
            "content-type":"application/json"
        },
        body:bodyJsonData
    }
    fetch(loginEndpoint, options)
    .then(response => {
        console.log(response);
        return response.json();
    
    })
    .then(x => {
        console.log(x)
    })
    .catch(err => {
        console.log('error', err);
    })
}