---
layout: base
title: David's CSA Page
description: Home Page
hide: true
---
<style>
body {
        width: 100vw;
        height: 100vh;
        overflow: hidden;
        background:url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/1197275/oceanBackdrop.jpg);
        background-size:cover;
        background-repeat:no-repeat;
    }
</style>
<body>    

<div id="tank"></div>

<script>
(function () {
    var myoptions, gui
    const fishes = ["🐟 🐠 🐡", "🐡", "🐠", "🐟", "🐟 🐠 🦑 🐙"]
    var tank = document.getElementById("tank")
    var toggleButton = document.getElementById("toggleGui")
    var WINDOW_MIN
    const MIN_THRESHOLD = 650
    var timeouts = [];

    window.onload = () => {
        generateControls()
        initializeTank()
    }
    window.addEventListener("resize", () => {
        initializeTank()
    })

    // Attach the click event listener to the new button
    toggleButton.addEventListener("click", () => {
        gui.closed ? gui.open() : gui.close()
    })

    function initializeTank() {
        WINDOW_MIN = Math.min(tank.clientHeight, tank.clientWidth)
        generateFishTank()
        if (WINDOW_MIN <= MIN_THRESHOLD) {
            gui.close()
        } else {
            gui.close()
        }
    }

    function generateFishTank() {
        clearTimeouts()
        tank.innerHTML = ""
        for (let i = 0; i < myoptions.NumFishGroups; i++) {
            let species = pick(myoptions.FishSpecies.split(" "))
            let numFish = 1
            if (!myoptions.SingleFishOnly && (Math.random() * 100) > (100 - myoptions.PercentSchools)) {
                numFish = getRandomInt(1, myoptions.MaxPerSchool)
            }
            let hueShift = myoptions.ColorChanging ? getRandomInt(0, 360) : 0

            let school = generateSchool(numFish, species, hueShift)
            tank.appendChild(school)
            loop(school)
        }
    }

    function generateSchool(numFish, species, hueShift) {
        let root = document.createElement("div");
        root.setAttribute("class", "school")
        root.style.width = `${getRandomFloat(100,1000)}px`
        root.style.height = `${getRandomFloat(100,700)}px`
        root.style.left = `${getRandomFloat(0,100)}%`
        root.style.top = `${getRandomFloat(0,100)}%`

        let maxFishSize = WINDOW_MIN < MIN_THRESHOLD ? 50 : 80
        let minFishSize = WINDOW_MIN < MIN_THRESHOLD ? 5 : 10
        let staticSize = getRandomInt(minFishSize, maxFishSize / 2)
        let allSameSize = numFish > 1 && Math.random() > .7

        for (let i = 0; i < numFish; i++) {
            let fishPos = [getRandomFloat(0, 100), getRandomFloat(0, 100)]
            let size = allSameSize ? staticSize : getRandomInt(minFishSize, maxFishSize)
            let fish = generateFish(fishPos, hueShift, size, species)
            root.appendChild(fish);
        }
        return root
    }

    function loop(school) {
        let timeout = school.getAttribute('data-timeout')
        clearTimeout(timeout)
        let minInterval = myoptions.SwimSpeed == "Slow" ? 10000 : myoptions.SwimSpeed == "Moderate" ? 5000 : 3000
        let maxInterval = myoptions.SwimSpeed == "Slow" ? 30000 : myoptions.SwimSpeed == "Moderate" ? 20000 : 10000
        let nextCall = getRandomInt(minInterval, maxInterval)
        moveSchool(school, nextCall)
        timeout = setTimeout(loop.bind(this, school), nextCall)
        timeouts.push(timeout)
        school.setAttribute('data-timeout', timeout)
    }

    function moveSchool(school, nextCall) {
        let currentX = parseInt(school.getAttribute("data-x")) || 0
        let moveMoreVertically = isSquid(school.querySelector(".fish").textContent)
        let newX = moveMoreVertically ? getRandomFloat(-tank.clientWidth/4, tank.clientWidth/4) : getRandomFloat(-tank.clientWidth, tank.clientWidth)
        let newY = moveMoreVertically ? getRandomFloat(-tank.clientHeight, tank.clientHeight) : getRandomFloat(-tank.clientHeight / 4, tank.clientHeight / 4)

        const isRight = newX > currentX;
        let easing = Math.random() > .5 ? "ease" : "ease-in-out"
        school.style.transition = `transform ${nextCall}ms ${easing}`
        school.style.transform = `translate(${newX}px, ${newY}px)`
        school.setAttribute("data-x", newX)

        let maxTranslationDistance = WINDOW_MIN < MIN_THRESHOLD ? 50 : 100;;
        [...school.querySelectorAll(".fish")].forEach(fish => {
            let direction = fish.querySelector(".direction")
            direction.style.transform = `scaleX(${isRight?-1:1})`
            direction.style.transition = `transform ${getRandomFloat(.2,.6)}s`
            if (school.children.length > 1) {
                let translateX = getRandomFloat(-maxTranslationDistance, maxTranslationDistance)
                let translateY = getRandomFloat(-maxTranslationDistance, maxTranslationDistance)
                fish.style.transform = `translateX(${translateX}px) translateY(${translateY}px)`
                let easing = Math.random() > .5 ? "ease" : "ease-in-out"
                fish.style.transition = `all ${nextCall}ms ${easing}`
            }
        })
    }

    function generateFish(pos, hueShift, size, icon) {
        let htm = `<div class="direction">${icon}</div>`;
        let f = document.createElement("div");
        f.setAttribute("class", "fish");
        f.style.filter = `hue-rotate(${hueShift}deg)`;
        f.style.left = `${pos[0]}%`;
        f.style.top = `${pos[1]}%`;
        f.style.fontSize = `${size}px`;
        f.setAttribute("tabindex", "-1");
        f.style.pointerEvents = 'none';
        f.style.zIndex = '1';
        f.innerHTML = htm;
        return f;
    }


    function Options() {
        this.NumFishGroups = "20"
        this.SwimSpeed = "Moderate"
        this.FishSpecies = "🐟 🐠 🐡"
    }

    function generateControls() {
        myoptions = new Options();
        gui = new dat.GUI();
        gui.add(myoptions, "NumFishGroups").listen().onChange(setValue)
        gui.add(myoptions, "SwimSpeed", ["Slow", "Moderate", "Fast"]).listen().onChange(setValue)
        gui.add(myoptions, "FishSpecies", fishes).listen().onChange(setValue);
    }

    function setValue() {
        generateFishTank()
    }

    function pick(arr) {
        return arr[Math.floor(Math.random() * arr.length)];
    }

    function getRandomInt(min, max) {
        min = Math.ceil(min)
        max = Math.floor(max)
        return Math.floor(Math.random() * (max - min + 1)) + min
    }

    function getRandomFloat(min, max) {
        return (Math.random() * (max - min)) + min
    }

    function isMobile() {
        let mobile = window.matchMedia(`only screen and (max-width: ${MIN_THRESHOLD}px), only screen and (max-height:${MIN_THRESHOLD}px)`).matches;
        return mobile || navigator.userAgent.indexOf("Firefox") != -1 || navigator.userAgent.indexOf("Silk") != -1;
    }

    function clearTimeouts() {
        for (var i = 0; i < timeouts.length; i++) {
            window.clearTimeout(timeouts[i])
        }
        timeouts = []
    }

    function setGUI(name, val) {
        for (var i = 0; i < gui.__controllers.length; i++) {
            if (gui.__controllers[i].property == name) {
                gui.__controllers[i].setValue(val)
                break;
            }
        }
    }

    function isSquid(s) {
        return s == "🦑" || s == "🐙"
    }

    setGUI("NumFishGroups", 20)
    setGUI("SwimSpeed", "Moderate")
    setGUI("FishSpecies", "🐟 🐠 🐡")

})();

</script>


<script src="https://cdnjs.cloudflare.com/ajax/libs/dat-gui/0.7.6/dat.gui.min.js"></script>


</body>