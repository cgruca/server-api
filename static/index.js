document.addEventListener('mousemove', (e) => {
    const star = document.createElement('div');
    star.classList.add('star');

    // Randomize size
    const size = Math.random() * 60 + 5; // Between 5px and 15px
    star.style.width = `${size}px`;
    star.style.height = `${size}px`;

    // Position the star at the mouse coordinates
    star.style.left = `${e.pageX - 25}px`;
    star.style.top = `${e.pageY - 25}px`;

    // Add random rotation or twinkle effect
    star.style.transform = `translate(-50%, -50%) rotate(${Math.random() * 360}deg)`;

    document.body.appendChild(star);

    // Remove the star after the animation is complete
    setTimeout(() => {
      star.remove();
    }, 1000);
});

window.addEventListener('load', () => {
    const audio = document.getElementById('audio');
    audio.play()
      .then(() => {
        console.log("Audio is playing");
      })
      .catch((error) => {
        console.error("Audio playback failed:", error);
      });
});

const giraffe = document.querySelector(".giraffe");

giraffe.addEventListener('click', function() {
  giraffe.classList.toggle('rotated'); // Toggle the "rotated" class to trigger the rotation
});

document.addEventListener("click", function() {
    var audio = document.getElementById("audio");
    audio.play().catch(function(error) {
        console.log("Error playing audio:", error);
    });
});