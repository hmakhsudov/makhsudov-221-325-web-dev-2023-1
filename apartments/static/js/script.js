$('.content__cart-image').slick({
    autoplay: true,
    autoplaySpeed: 3000,
});


$('.apartment__gallery').slick({

});

setTimeout(function() {
    var successMessage = document.querySelector('.success-message');
    if (successMessage) {
        successMessage.style.display = 'none';
    }
}, 5000);


document.addEventListener("DOMContentLoaded", function() {
    var buttons = document.querySelectorAll(".scroll-to-div");
    
    function scrollToTarget(targetElement) {
      var offset = targetElement.offsetTop;
      window.scrollTo({ top: offset, behavior: "smooth" });
    }
    
    function handleButtonClick(e) {
      e.preventDefault();
      
      var target = this.dataset.target;
      var targetElement = document.querySelector(target);
      
      scrollToTarget(targetElement);
      
      // Add active class to clicked button
      buttons.forEach(function(button) {
        button.classList.remove("active");
      });
      this.classList.add("active");
    }
    
    buttons.forEach(function(button) {
      button.addEventListener("click", handleButtonClick);
    });
    
    // Check if the page URL has a hash targeting a section
    if (window.location.hash) {
      var targetElement = document.querySelector(window.location.hash);
      if (targetElement) {
        scrollToTarget(targetElement);
        
        // Add active class to corresponding button
        buttons.forEach(function(button) {
          if (button.dataset.target === window.location.hash) {
            button.classList.add("active");
          } else {
            button.classList.remove("active");
          }
        });
      }
    }
  });
  