function setFormMessage(formElement, type, message){
    const messageElement = formElement.querySelector(".form__message");
    
    messageElement.textContent = message;
    messageElement.classList.remove("form__message--success", "form__message--error");
    messageElement.classList.add('form__message--${type}');
}

//setFormMessage(loginForm, "success", "You're logged in!");

function setInputError(inputElement, message) {
    inputElement.classList.add("form__input--error");
    inputElement.parentElement.querySelector(".form__input-error-message").textContent = message;
};

function clearInputError(inputElement){
    inputElement.classList.remove("form__input--error");
    inputElement.parentElement.querySelector(".form__input-error-message").textContent= "";
};

document.addEventListener("DOMContentLoaded", () => {
  const submit = document.querySelector("#login");
});

  submit.addEventListener("submit", e => {
      e.preventDefault();

      //peform fetch from django

      setInputError(submit, "Invalid username/password combination");
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