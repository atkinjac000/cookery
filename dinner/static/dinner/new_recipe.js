const ingredient_inputs_div = document.querySelector("#ingredient-inputs");
const add_ingredient_button = document.querySelector("#add-ingredient");
const ingredient_selector = document.querySelector("#select-ingredient");
const ingredient_list_div = document.querySelector("#ingredient-list");

fetch("http://localhost:8000/dinner/ingredients")
	.then(response => response.json())
	.then(json => {
		const ingredients = json.ingredients;
		for (const ingredient of ingredients) {
			i = document.createElement("option");
			i.value = ingredient;
			i.textContent = ingredient;
			console.log(i.textContent);
			ingredient_selector.appendChild(i);
		}
	});


add_ingredient_button.addEventListener("click", () => {
	const p = document.createElement("li");
	p.textContent = ingredient_selector.value;
	ingredient_list_div.appendChild(p);
	ingredient_selector.value = "";
});
