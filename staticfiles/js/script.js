function copyclipboard(e){
    const copyText = e.previousElementSibling
    copyText.select()
    let imageUrl = window.location.origin + "/" +copyText.value.slice(1)
    navigator.clipboard.writeText(imageUrl)
    alert("Copied clipboard:"+ imageUrl)
}