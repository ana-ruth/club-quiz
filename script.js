
function getFormValues()
{
    //form responses
    var name = document.getElementById('Name').value;
    var email = document.getElementById("Email").value;
    var field = document.getElementById('field').value;
    var level = document.getElementById('level').value;
    var gender = document.querySelector('input[name="gender-specific"]:checked')?.value === 'Yes' ? 1 : 0;
    var extracurricular = document.getElementById('extracurricular').value;
    var volunteering = document.querySelector('input[name="volunteering"]:checked')?.value === 'Yes' ? 1 : 0;
    var ethnicity = document.querySelector('input[name="ethnicity"]:checked')?.value === 'Yes' ? 1 : 0;

// Return an object formatted for QuizResponse
    return {
        name: name,
        email: email,
        field: field,
        level: level,
        gender: gender,
        extracurricular: extracurricular,
        volunteering: volunteering,
        ethnicity: ethnicity
    }

}

function submitQuizResponse() {
    var formData = getFormValues();
    fetch('http://127.0.0.1:8000/quiz', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        displayRecommendations(data.recommendations);
    })
    .catch(error => {
        console.error('Error:', error);
        // Handle the error appropriately
    });
}

function displayRecommendations(recommendations) {
    const clubList = document.getElementById('club-results');
    const noResults = document.getElementById('no-results');
    clubList.innerHTML = ''; // Clear previous results
    
    if (clubs && clubs.length > 0) {
        clubs.forEach(club => {
            const li = document.createElement('li');
            li.textContent = club;
            clubList.appendChild(li);
        });
        clubList.style.display = 'block';
        noResults.style.display = 'none';
    } else {
        clubList.style.display = 'none';
        noResults.style.display = 'block';
    }

    document.getElementById('dialog').showModal();
}