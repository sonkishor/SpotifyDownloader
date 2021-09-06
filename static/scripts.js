function changeStatus() {
    document.getElementById("statusDiv").style.display = 'none'
    document.getElementById("loading").style.display = 'block'
    document.getElementById("navbar").style.display = 'none'
    document.getElementById("embed").src = linkp;
    console.log(linkp);
}


