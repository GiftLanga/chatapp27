function validateLogin(e) {
  const loginForm = document.forms["loginForm"];
  const username = document.forms["loginForm"]["username"].value;
  const password = document.forms["loginForm"]["password"].value;
  e.preventDefault();
  if(username === "" && password === ""){
    alert('username and password required');
    return false;
  }

  if(username === ""){
    alert('username required');
    return false;
  }

  if(password === ""){
    alert('password required');
    return false;
  }

  loginForm.submit();
  return true;
}