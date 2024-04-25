// components/todo/TodoDetails.js
import React from 'react';

const TodoDetails = ({ todo }) => {
  return (
    <div>
      <h2>Todo Details</h2>
      <p>Description: {todo.description}</p>
      <p>Status: {todo.status}</p>
      {/* Add more details as needed */}
    </div>
  );
};

export default TodoDetails;
