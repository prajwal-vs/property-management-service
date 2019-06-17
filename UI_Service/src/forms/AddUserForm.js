import React, { useState } from 'react'

const AddUserForm = props => {
	const initialFormState = { name: '', address: '',contact_no:'',landmark:'',floors:'' }
	const [ user, setUser ] = useState(initialFormState)

	const handleInputChange = event => {
		const { name, value } = event.target

		setUser({ ...user, [name]: value })
	}

	return (
		<form
			onSubmit={event => {
				event.preventDefault()
				if (!user.name || !user.address) return

				props.addUser(user)
				setUser(initialFormState)
			}}
		>
	  <label>Name</label>
      <input type="text" name="name" value={user.name} onChange={handleInputChange} />
      <label>Address</label>
      <input type="text" name="address" value={user.address} onChange={handleInputChange} />
      <label>Contact_No</label>
      <input type="integer" name="contact_no" value={user.contact_no} onChange={handleInputChange} />
      <label>Landmark</label>
      <input type="text" name="landmark" value={user.landmark} onChange={handleInputChange} />
      <label>Floors</label>
      <input type="text" name="floors" value={user.floors} onChange={handleInputChange} />
			<button>Add new building</button>
		</form>
	)
}

export default AddUserForm
