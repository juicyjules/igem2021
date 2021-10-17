console.log("animation loaded")
document.addEventListener("DOMContentLoaded", function(){
    gsap.utils.toArray(".home-block").forEach(section => {
        console.log("lets go")
        gsap.from(section.querySelectorAll("p, h1"), {
          scrollTrigger: {
              trigger: section,
              start: () => "bottom 90%",
          },
          autoAlpha: 0,
          y: 30,
          duration: 0.75,
          stagger: 0.75,
          delay: 0.2,
        });
      });
});