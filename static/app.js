// querying menu item element
let home = document.querySelectorAll(".menu-item");

// add event while clicked to inject active class
for (let i = 0; i < home.length; i++) {
    home[i].addEventListener("click", (e) => {
        e.preventDefault;
        home[i].classList.add("active");
    })
}
