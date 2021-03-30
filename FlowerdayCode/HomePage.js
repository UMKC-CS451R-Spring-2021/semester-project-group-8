function setFormMessage(formElement, type, message){
    const messageElement = formElement.querySelector(".form__message");
    
    messageElement.textContent = message;
    messageElement.classList.remove("form__message--success", "form__message--error");
    messageElement.classList.add('form__message--${type}');
}

setFormMessage(loginForm, "success", "You're logged in!");

document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.querySelector("#login");

  document.querySelector("#linkLogin").addEventListener("click", e =>{
      e.preventDefault();
  });

  loginForm.addEventListener("submit", e => {
      e.preventDefault();

      //peform fetch from django

      setFormMessage(loginForm, "error", "Invalid username/password combination");
  });
});
//BELOW CODE IS STARTER TEMPLATE FOR FETCHING FROM DJANGO
/*
$.ajax({
    type: "GET",
    url: '/my_def_in_view',
    data: {
        "result": result,
    },
    dataType: "json",
    success: function (data) {
        // any process in data
        alert("successfull")
    },
    failure: function () {
        alert("failure");
    }
});*/