function copyclipboard(e){
    const copyText = e.previousElementSibling
    copyText.select()
    navigator.clipboard.writeText(copyText.value)
    alert("Copied clipboard :"+ copyText.value)
}