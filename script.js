function getFormValues()
{
    //form responses
    var name = document.getElementById('Name').value;
    var email = document.getElementById("Email").value;
    var field = document.getElementById('field').value;
    var level = document.getElementById('level').value;
    var gender = document.querySelector('input[name="gender-specific"]:checked').value;
    var extracurricular = document.getElementById('extracurricular').value;
    var volunteering = document.querySelector('input[name="volunteering"]:checked').value;
    var ethnicity = document.querySelector('input[name="ethnicity"]:checked').value;


    /* //to view them on the website//
    document.getElementById('result').innerHTML = 
    "Name: "+name+"<br>"+
    "Email: " + email + "<br>" +
    "Field: "+field+"<br>"+
    "Level: "+level+"<br>"+
    "Gender: " + gender + "<br>" +
    "Extracurricular: "+ extracurricular+"<br>"+
    "Volunteering: "+volunteering + "<br>" + 
    "Ethnicity: "+ethnicity;
    */

}