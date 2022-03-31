function myModal(val){
    document.getElementById('id01').style.display='block'
}
function exitModal(){
    document.getElementById('id01').style.display='none'
}
function confirmDelete(id){
    myModal();
    document.getElementById('confirm_delete').value = id;
}