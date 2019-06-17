import React, { useState, Fragment,useEffect } from 'react'
import AddUserForm from './forms/AddUserForm'
import EditUserForm from './forms/EditUserForm'
import UserTable from './tables/UserTable'

const App = () => {


const url = "http://localhost:8080/api/v1/building";
   const [data, updateData] = useState([])

   async function reloaddata(){
   	   const resp = await fetch(url)
       const json = await resp.json()
       updateData(json.data)
   }

   useEffect(reloaddata, [url]);

	

	const initialFormState = { id: null, name: '', username: '' }

	const [ currentUser, setCurrentUser ] = useState(initialFormState)
	const [ editing, setEditing ] = useState(false)

	// CRUD operations
	const addUser = user => {
		//console.log("adduser",user); 
		async function a(){
      		 await fetch(url, {method: 'POST',body: JSON.stringify(user)})
      		 .then(reloaddata())
			}; 
		a()


	}

	const deleteUser = id => {
		setEditing(false)
		updateData(data.filter(user => user.building_id !== id))
		async function a(){
      		 await fetch('http://localhost:8080/api/v1/building/'+id, {method: 'DELETE'})
			}; 
		a()

	}

	const updateUser = (id, updatedUser) => {
		setEditing(false)
		updateData(data.map(user => (user.building_id === id ? updatedUser : user)));

		async function a(){
      		 await fetch('http://localhost:8080/api/v1/building/'+id, {method: 'PUT',body: JSON.stringify(updatedUser)})
			}; 
		a()


	}

	const editRow = user => {
		setEditing(true)
		setCurrentUser({...user})
	}

	return (
		<div className="container">
			<h1>Property Management Service</h1>
			<div className="flex-row">
				<div className="flex-large">
					{editing ? (
						<Fragment>
							<h2>Edit user</h2>
							<EditUserForm
								editing={editing}
								setEditing={setEditing}
								currentUser={currentUser}
								updateUser={updateUser}
							/>
						</Fragment>
					) : (
						<Fragment>
							<h2>Add user</h2>
							<AddUserForm addUser={addUser} />
						</Fragment>
					)}
				</div>
				<div className="flex-large">
					<h2>View users</h2>
					<UserTable users={data} editRow={editRow} deleteUser={deleteUser} />
				</div>
			</div>
		</div>
	)
}

export default App
