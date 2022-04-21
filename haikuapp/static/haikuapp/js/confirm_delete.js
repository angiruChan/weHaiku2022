// Haiku Entries Modal Functions
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


// Categories Modal Functions
function myModal1(val){
document.getElementById('del_categ').style.display='block'
}
function exitModal1(){
    document.getElementById('del_categ').style.display='none'
}
function confirmDelete_Categ(id){
    myModal1();
    document.getElementById('confirm_del_categ').value = id;
}


// Haiku Modal Functions
function myModal2(val){
document.getElementById('del_haiku').style.display='block'
}
function exitModal2(){
    document.getElementById('del_haiku').style.display='none'
}
function confirmDelete_Haiku(id){
    myModal2();
    document.getElementById('confirm_del_haiku').value = id;
}


// Add Comment Modal
function exitCommentModal(){
    document.getElementById('commentModal').style.display='none'
}
function addComment(val){
    document.getElementById('commentModal').style.display='block'
}

