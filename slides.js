$(document).ready(function () {
    particlesJS("particles-js", {
        "particles": {
          "number": {
            "value": 80,
            "density": {
              "enable": true,
              "value_area": 850
            }
          },
          "color": {
            "value": "#ffffff"
          },
          "shape": {
            "type": "circle",
            "stroke": {
              "width": 0,
              "color": "#000000"
            },
            "polygon": {
              "nb_sides": 5
            },
          },
          "opacity": {
            "value": 0.5,
            "random": false,
            "anim": {
              "enable": false,
              "speed": 0.1,
              "opacity_min": 0.1,
              "sync": false
            }
          },
          "size": {
            "value": 3,
            "random": true,
            "anim": {
              "enable": false,
              "speed": 10,
              "size_min": 0.1,
              "sync": false
            }
          },
          "line_linked": {
            "enable": true,
            "distance": 150,
            "color": "#ffffff",
            "opacity": 0.35,
            "width": 1
          },
          "move": {
            "enable": true,
            "speed": 2,
            "direction": "none",
            "random": false,
            "straight": false,
            "out_mode": "out",
            "bounce": false,
            "attract": {
              "enable": false,
              "rotateX": 600,
              "rotateY": 1200
            }
          }
        },
        "interactivity": {
          "detect_on": "window",
          "events": {
            "onhover": {
              "enable": true,
              "mode": "grab"
            },
            "onclick": {
              "enable": true,
              "mode": "push"
            },
            "resize": true
          },
          "modes": {
            "grab": {
              "distance": 140,
              "line_linked": {
                "opacity": 1
              }
            },
            "bubble": {
              "distance": 400,
              "size": 40,
              "duration": 2,
              "opacity": 8,
              "speed": 3
            },
            "repulse": {
              "distance": 200,
              "duration": 0.4
            },
            "push": {
              "particles_nb": 3
            },
            "remove": {
              "particles_nb": 2
            }
          }
        },
        "retina_detect": true
      });

    const colorArray = [
        "#683A5E",
        "#262626",
    ];
    const slides = document.querySelectorAll("section");
    const container = document.querySelector("#panelWrap");
    // ParticlesJS Config.
    const video = document.querySelector("#video");
    let dur = 0.5;
    let offsets = [];
    let oldSlide = 0;
    let activeSlide = 0;
    let dots = document.querySelector(".dots");
    let navDots = [];
    let iw = window.innerWidth;
    let blocked = false;

    const larrow = document.querySelector("#leftArrow");
    larrow.addEventListener("click", slideAnim);
    const rarrow = document.querySelector("#rightArrow");
    rarrow.addEventListener("click", slideAnim);

    // set slides background colors and create the nav dots
    for (let i = 0; i < slides.length; i++) {
        // gsap.set(slides[i], {
        //     backgroundColor: colorArray[i]
        // });
        let newDot = document.createElement("div");
        newDot.className = "dot";
        newDot.index = i;
        navDots.push(newDot);
        newDot.addEventListener("click", slideAnim);
        dots.appendChild(newDot);
    }

    // get elements positioned
    gsap.set(".dots, .titleWrap", {
        xPercent: -50
    });

    // lower screen animation with nav dots and rotating titles
    const dotAnim = gsap.timeline({
        paused: true
    });
    dotAnim.to(
        ".dot", {
            stagger: {
                each: 1,
                yoyo: true,
                repeat: 1
            },
            scale: 2.1,
            rotation: 0.1,
            ease: "none"
        },
        0.5
    );
    dotAnim.to(
        ".title",
        slides.length + 1, {
            y: -(slides.length * 30),
            rotation: 0.01,
            ease: "none"
        },
        0
    );
    dotAnim.time(1);
    // make the whole thing draggable
    let dragMe = Draggable.create(container, {
        type: "x",
        edgeResistance: 1,
        snap: offsets,
        bounds: "#masterWrap",
        onDrag: tweenDot,
        onThrowUpdate: tweenDot,
        onDragEnd: slideAnim,
        allowNativeTouchScrolling: false,
        zIndexBoost: false,
        cursor: "default"
    });

    dragMe[0].id = "dragger";
    sizeIt();

    // main action check which of the 4 types of interaction called the function
    function slideAnim(e) {
        oldSlide = activeSlide;
        // dragging the panels
        if (this.id === "dragger") {
            activeSlide = offsets.indexOf(this.endX);
        } else {
            if (gsap.isTweening(container)) {
                return;
            }
            // arrow clicks
            if (this.id === "leftArrow" || this.id === "rightArrow") {
                activeSlide =
                    this.id === "rightArrow" ? (activeSlide += 1) : (activeSlide -= 1);
                // click on a dot
            } else if (this.className === "dot") {
                activeSlide = this.index;
                // scrollwheel
            } else {
                if (!blocked){
                    activeSlide = e.deltaY > 0 ? (activeSlide += 1) : (activeSlide -= 1);
                    blocked = true
                    setTimeout(function(){blocked = false},350);
                }
            }
        }
        // make sure we're not past the end or beginning slide
        activeSlide = activeSlide < 0 ? 0 : activeSlide;
        console.log(activeSlide)

        activeSlide = activeSlide > slides.length - 1 ? slides.length - 1 : activeSlide;
        if (oldSlide === activeSlide) {
            return;
        }

        if(activeSlide == 0){
            larrow.style.opacity = 0
        } else if (activeSlide + 1 == slides.length){
            rarrow.style.opacity = 0
        } else {
            rarrow.style.opacity = 1
            larrow.style.opacity = 1
        }
        const currentSection = slides[activeSlide]
        if(activeSlide == 1){
            setTimeout(function(){video.play()},500);
            gsap.from(currentSection, {
                autoAlpha: 0,
                opacity:0,
                duration: 1,
                delay: 0.1,
                ease: Power3.easeIn
              });
        }
        else {
            video.pause();
            gsap.from(currentSection, {
                autoAlpha: 0,
                y: 65,
                duration: 0.75,
                delay: 0.5,
              });
        }

        // if we're dragging we don't animate the container
        if (this.id != "dragger") {
            gsap.to(container, dur, {
                x: offsets[activeSlide],
                onUpdate: tweenDot
            });
        }
    }

    // update the draggable element snap points
    function sizeIt() {
        offsets = [];
        iw = window.innerWidth;
        gsap.set("#panelWrap", {
            width: slides.length * iw
        });
        gsap.set(slides, {
            width: iw
        });
        for (let i = 0; i < slides.length; i++) {
            offsets.push(-slides[i].offsetLeft);
        }
        gsap.set(container, {
            x: offsets[activeSlide]
        });
        dragMe[0].vars.snap = offsets;
        console.log(offsets)
    }

    gsap.set(".hideMe", {
        opacity: 1
    });
    window.addEventListener("wheel", slideAnim);
    window.addEventListener("resize", sizeIt);

    // update dot animation when dragger moves
    function tweenDot() {
        gsap.set(dotAnim, {
            time: Math.abs(gsap.getProperty(container, "x") / iw) + 1
        });
    }
});