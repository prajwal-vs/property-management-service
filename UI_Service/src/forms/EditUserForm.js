import React, { useState, useEffect } from 'react'

const EditUserForm = props => {
  const [ user, setUser ] = useState(props.currentUser)
  console.log(props.currentUser);

  useEffect(
    () => {
      setUser(props.currentUser)
    },
    [ props ]
  )
  // You can tell React to skip applying an effect if certain values haven’t changed between re-renders. [ props ]

  const handleInputChange = event => {
    const { name, value } = event.target
    setUser({ ...user, [name]: value })
  }

  return (
    <form
      onSubmit={event => {
        event.preventDefault()
        props.updateUser(user.building_id, user)
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
      <input type="text" name="floors" value={user.total_floors} onChange={handleInputChange} />
      <button>Update building details</button>
      <button onClick={() => props.setEditing(false)} className="button muted-button">
        Cancel
      </button>
    </form>
  )
}

export default EditUserForm
