'use strict';

// manage theme control ***************************************************************************
const switcher = document.querySelector('.btn');
switcher.addEventListener('click', function () {
    document.body.classList.toggle('light-theme');
    document.body.classList.toggle('dark-theme');

    const className = document.body.className;
    if (className == "light-theme") {
        this.textContent = "Dark";
    } else {
        this.textContent = "Light";
    }
});


// display seed count *****************************************************************************
function getStr() {
    num = eel.num()
    document.getElementById('x').innerHTML = num;
}