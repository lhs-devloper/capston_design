const target = document.querySelector(".sex");
console.log(target);

function onclick1() {
    if (target.className == "sex") {
        target.className = "unsex";
    } else {
        target.className = "sex";
    }
}