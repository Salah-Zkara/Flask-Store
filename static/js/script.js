let buttons=Array.from(document.getElementsByClassName("addtocart"))


let cartItems=[]
function addHandler(e){
    let parent=e.target.parentNode

}

buttons.forEach(e => {
    e.addEventListener('click',addHandler,false)
    
});

function remove_item(array,item) {
    const index = array.indexOf(item)
    if (index > -1) { array.splice(index, 1) }
}

function addHandler(e){
    let parent=e.target.parentNode
    let item=parent.id
    let node_cercle=e.target.childNodes[1]
    if (cartItems.includes(item)) {
        node_cercle.removeAttribute('id')
        remove_item(cartItems,item)
    }
    else{
        node_cercle.setAttribute('id','cercle')
        cartItems.push(item)
    }
    console.log(cartItems)

    document.getElementById('cart').innerHTML=cartItems.length


}