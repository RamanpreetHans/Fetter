function login()
{
	var username = document.getElementById("username").value;
	var pass = document.getElementById("password").value;
	//Check for valid login page
	
	if(username == "RamanHans")
	window.location.href="Homepage.html";
	
	if(username == "Samapth Nayak")
		window.location.href="InstituteAdmin.html";

	if(username == "Bhagat Kirtiraj")
		window.location.href="superAdminHomepage.html"
}