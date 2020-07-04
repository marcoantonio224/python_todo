
// ============= API CRUD METHODS =================
/* ============ CREATE A LIST CATEGORY ============== */
document.getElementById('list-form').onsubmit = (e)=> {
  e.preventDefault();
  let list = document.getElementById('list-name');
  const data = {'name': list.value}; // [key, value]
  // Custom API with fetch method
  makeRequest('/lists/create', 'POST', data)
  .then((response)=>{
    return response.json();
  })
  .then((jsonResponse) => {
    let liItem = document.createElement('li');
    liItem.textContent = jsonResponse['name'];
    document.getElementById('lists').appendChild(liItem);
    errorElement.className = "hidden";
    description.value ='';
    location.reload();
  })
  .catch(err => {
    console.log(err)
    errorElement.className = "";
  });
}
/* ===================================================== */


/* ============ DELETE LIST CATEGORY =========== */
  // const deleteButtons = document.querySelectorAll('.delete');
  // for(let i =0; i < deleteButtons.length; i++) {
  //   const deleteButton = deleteButtons[i];
  //   deleteButton.onclick = function(e) {
  //     const todoID = e.target.dataset['id'];
  //     makeRequest(`/todos/${todoID}/set-completed`, 'DELETE')
  //     .then((response)=>{
  //       return response.json();
  //     })
  //     .then((jsonResponse) => {
  //       console.log(jsonResponse)
  //       const { todoID } = jsonResponse;
  //       console.log(todoID)
  //       const todoItemDelete = document.getElementById('todo-item-'+todoID);
  //       console.log(todoItemDelete)
  //       todoItemDelete.remove();
  //       errorElement.className = "hidden";
  //     })
  //     .catch(err => {
  //       console.log(err)
  //       errorElement.className = "";
  //     });
  //   }
  // }
/* ===================================================== */



