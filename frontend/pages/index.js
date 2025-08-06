import { useState, useEffect } from 'react';
import axios from 'axios';

export default function Home() {
  const [message, setMessage] = useState('Loading...');
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState('');

  useEffect(() => {
    // Fetch from backend API
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8001';
      const response = await axios.get(`${apiUrl}/api/hello`);
      setMessage(response.data.message);
      
      // Fetch todos
      const todosResponse = await axios.get(`${apiUrl}/api/todos`);
      setTodos(todosResponse.data);
    } catch (error) {
      setMessage('Failed to connect to backend');
    }
  };

  const addTodo = async () => {
    if (!newTodo.trim()) return;
    
    try {
      const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8001';
      const response = await axios.post(`${apiUrl}/api/todos`, {
        title: newTodo,
        completed: false
      });
      setTodos([...todos, response.data]);
      setNewTodo('');
    } catch (error) {
      console.error('Failed to add todo:', error);
    }
  };

  return (
    <div style={{ padding: '2rem', fontFamily: 'Arial, sans-serif' }}>
      <h1>🚀 Test Fullstack App</h1>
      <p>Backend says: <strong>{message}</strong></p>
      
      <div style={{ marginTop: '2rem' }}>
        <h2>📝 Todo List (from Database)</h2>
        <div style={{ marginBottom: '1rem' }}>
          <input
            type="text"
            value={newTodo}
            onChange={(e) => setNewTodo(e.target.value)}
            placeholder="Add new todo"
            style={{ padding: '0.5rem', marginRight: '0.5rem' }}
          />
          <button onClick={addTodo} style={{ padding: '0.5rem' }}>
            Add Todo
          </button>
        </div>
        
        <ul>
          {todos.map((todo) => (
            <li key={todo.id}>
              {todo.title} {todo.completed ? '✅' : '⏳'}
            </li>
          ))}
        </ul>
      </div>
      
      <div style={{ marginTop: '2rem', fontSize: '0.8rem', color: '#666' }}>
        <p>Environment: {process.env.NODE_ENV}</p>
        <p>API URL: {process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8001'}</p>
      </div>
    </div>
  );
}