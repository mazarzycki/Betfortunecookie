document.addEventListener("DOMContentLoaded", function() {
    const fortuneCookie = document.getElementById("cookie");

    // Create the audio element for the crack sound
    const crackSound = document.createElement('audio');
    crackSound.src = "/static/sounds/crack.wav"; // Path to your crack sound file
    crackSound.preload = "auto"; // Preload the audio file

    if (fortuneCookie) {
        fortuneCookie.addEventListener("click", function() {
            // Play the crack sound
            crackSound.play();
            
            // Redirect to the accept tip page when the cookie is clicked
            window.location.href = '/accept';
        });
    }

    const okButton = document.getElementById("ok-button");
    if (okButton) {
        okButton.addEventListener("click", function() {
            fetch('/get_tip')
                .then(response => response.json())
                .then(data => {
                    const tipContainer = document.getElementById('tip-container');
                    tipContainer.innerHTML = `Match: ${data.match} <br> Tip: ${data.tip}`;

                    okButton.remove();

                    document.getElementById("accept-text").remove();

                    const backButton = document.createElement('button');
                    backButton.textContent = 'Go Back to Cookie';
                    backButton.addEventListener('click', function() {
                        window.location.href = '/';
                    });

                    const acceptContainer = document.getElementById('accept-container');
                    acceptContainer.appendChild(backButton);
                })
                .catch(error => console.error('Error fetching tip:', error));
        });
    }
});
