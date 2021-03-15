
//Login Page Draft 

//import User Table file

//Global Variables
var userNameInput = "";
var passwordInput = "";

var testAccounts = [
    {
        username: "main",
        password: "pass"
    }, 
    {
        username: "other",
        password: "Ball"
    }
]

//checkCredentials is a function to verify username/password

function getInfo(){

    //import UN/pass table

    userNameInput = document.getElementById("username").nodeValue;
    passwordInput = document.getElementById("password").nodeValue;
    console.log("Your Username is " + userNameInput + " and your password is " + passwordInput)

}

getInfo();

    /*for (var i = 0; i < UNTable.length; i++_){
        if (unameString != any element in UN section of table  OR 
        (unameString == some element in table AND passString != matching password element))
            Return "Username and/or password incorrect, please try again"
    

        else if (unameString == any element in the UN section on the table &&
        passString == corresponding password in table)
            permit user to access main navigation page

        else 
            return "unknown error, please refresh the page and try again"
        }
    
    */

     