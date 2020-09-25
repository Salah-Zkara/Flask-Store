myform=document.getElementsByClassName("contactForm")[0]
btn_add=document.getElementById("add")
btn_add.addEventListener('click',show)

function show() {
    myform.style.display="block"
}