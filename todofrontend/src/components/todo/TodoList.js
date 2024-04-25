import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TodoList = () => {
    const [todos, setTodos] = useState([]);

    useEffect(() => {
        // Fetch todos from the backend when the component mounts
        axios.get(`/api/projects/${projectId}/todos/`)
            .then(response => {
                setTodos(response.data);
            })
            .catch(error => {
                console.error('Error fetching todos:', error);
            });
    }, []);

    return (
        <div>
            <h1>Todo List</h1>
            <ul>
                {todos.map(todo => (
                    <li key={todo.id}>{todo.description}</li>
                ))}
            </ul>
        </div>
    );
};

export default TodoList;
