var cButton = document.getElementById("cButton");
var cImage = document.getElementById("cImg");
var eImage = document.getElementById("eImg");
cImage.style.display = "none";
cButton.addEventListener("click",function(){
	cButton.classList.remove("rotate-arrow");
	void cButton.offsetWidth;
	cButton.classList.add("rotate-arrow");
	if(cImage.style.display == "none"){
		cImage.style.display = "block";
		eImage.style.display = "none";
	}else{
		eImage.style.display = "block";
		cImage.style.display = "none";
	}
});