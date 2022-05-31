function copyclipboard(e){
    const copyText = e.previousElementSibling
    copyText.select()
    // let imageUrl = window.location.origin + "/" +copyText.value.slice(1)
    navigator.clipboard.writeText(copyText.value)
    alert("Copied clipboard :"+ copyText.value)
}