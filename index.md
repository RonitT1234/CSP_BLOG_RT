---
layout: default
title: Ronit Thomas Blog
---

<style>
 #login {
    margin-top: 10px;
    padding-top: 1.5rem;
    padding-bottom: 1.5rem;
    padding-left: 2rem;
    padding-right: 2rem;
    text-align: center;
    width: 100%;
}
.login-container {
  border: 3px solid #4CAF50;
  background: linear-gradient(to right, #3aded8, #fa0c0c);
}

input[type=text], input[type=password] {
  width: 100%;
  padding: 14px 20px;
  margin: 10px 0;
  display: inline-block;
  border: 2px solid #2E7D32;
  box-sizing: border-box;
  background-color: #ff91fd;
  color: white;
}

button {
  background-color: #ff91fd;
  color: white;
  padding: 16px 20px;
  margin: 10px 0;
  border: none;
  cursor: pointer;
  width: 50%;
  margin-left: 170px;
  border-radius: 5px;
}
button:hover {
  opacity: 0.8;
}

.imgcontainer {
  text-align: center;
  margin: 24px 0 12px 0;
}

img.avatar {
  width: 60%;
  border-radius: 50%;
}

.container {
  padding: 16px;
  color: #fff;
}

span.psw {
  display: flex;
  justify-content: center;
  text-align: center;
  margin-left: 225px;
  padding-top: 16px;
  color: #3498db;
}
span.psw2 {
  display: flex;
  justify-content: center;
  text-align: center;
  margin-left: 220px;
  color: #3498db;
}

@media screen and (max-width: 600px) {
  span.psw, span.psw2 {
    display: block;
    float: none;
    margin-left: 0;
  }
  button {
    width: 100%;
  }
}

</style>
<div class="login-container">
  <div class="imgcontainer">
    <img src="{{site.baseurl}}/images/logo.webp" alt="Avatar" class="avatar">
  </div>

<form action="javascript:login_user()">
    <label for="uid"><b>Username</b></label>
    <input type="text" id="uid" placeholder="Enter Username" name="uid" required>
    <label for="password"><b>Password</b></label>
    <input type="password" id="password" placeholder="Enter Password" name="password" required>
    <button class='button'>Log in</button>
    <div>
    <span class="psw2">Want to delete an account? <a href="{{site.baseurl}}/delete"> Delete</a></span>
    <span class="psw">Need an account? <a href="{{site.baseurl}}/signup"> Sign Up</a></span>
    </div>
  

</form>
<script type="module">
    import { uri, options } from '{{site.baseurl}}/assets/js/api/config.js';
    function login_user(){
      var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
        const url = uri + '/api/users/authenticate';
        const body = {
            uid: document.getElementById("uid").value,
            password: document.getElementById("password").value,
        };
        const authOptions = { 
            method: 'POST', 
            cache: 'no-cache',
            headers: myHeaders,
            body: JSON.stringify(body)
        };
        fetch(url, authOptions)
        .then(response => {
            if (!response.ok) {
                const errorMsg = 'Login error: ' + response.status;
                console.log(errorMsg);
                return;
            }
            window.location.href = "{{site.baseurl}}/main";
        })
        .catch(err => {
            console.error(err);
        });
    }
    window.login_user = login_user;
</script>
