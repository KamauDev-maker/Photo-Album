function copyclipboard(){
    let copyText = document.getElementById('link')
        copyText.select();
        let imageUrl = window.location.href +copyText.value.slice(1)
        navigator.clipboard.writeText(imageUrl)
        alert("Copied to clipboard:"+ imageUrl)
}