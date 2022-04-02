function modalImageDisplay(val){
    document.getElementById('mod_image_preview').style.display='block'
}
function exitImageModal(){
    document.getElementById('mod_image_preview').style.display='none'
}
function ImagePreview(id){
    modalImageDisplay();
    document.getElementById("myImgPreview").src = id;
}