console.log("world")

const form = document.querySelector("#add_form")

function showCupcakes(cupcake){
    let display = document.querySelector("#display")
  
    let li = document.createElement("li")
    let img = document.createElement("img")
    let div = document.createElement("div")
    li.innerText = `${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}`
    img.src = cupcake.image
    img.width = 200
    div.append(li)
    div.append(img)
    display.append(div);  
      
}
async function initialCupcakes(){
    let res = await axios.get("/api/cupcakes")
    cupcakes = res.data.cupcakes
    for (let i =0 ; i < res.data.cupcakes.length; i++){
        cupcake = res.data.cupcakes[i]
        showCupcakes(cupcake);
    }
    
}

async function update(e){
    e.preventDefault()
    const flavor = document.querySelector("#flavor").value
    const size = document.querySelector("#size").value
    const rating = document.querySelector("#rating").value
    const image = document.querySelector("#image").value
    const newCupcake = await axios.post('/api/cupcakes', {flavor:flavor, size:size, rating:rating, image:image})
    cupcake = newCupcake.data.cupcake
    showCupcakes(cupcake)
    form.reset()
}
form.addEventListener("submit", update )

initialCupcakes();