import React, { useState } from 'react'
import LoginForm from './LoginForm';
import RegisterForm from './RegisterForm';


 const Main = () => {
    const [showLoginForm, setShowLoginForm] = useState(false);
    const [showRegisterForm, setShowRegisterForm] = useState(false);
    const toggleLoginForm = () => {
        setShowLoginForm(prevState => !prevState); // Инвертируем состояние
        setShowRegisterForm(false);
    };
    const toggleRegisterForm = () => {
        setShowRegisterForm(prevState => !prevState);
        setShowLoginForm(false);
    }
  return (
    <div>
        {showLoginForm && <LoginForm toggleLoginForm={toggleLoginForm} />} 
      <button onClick={toggleLoginForm}>
        Login
      </button>
      {showRegisterForm && <RegisterForm toggleRegisterForm={toggleRegisterForm} />} 
      <button onClick={toggleRegisterForm}>
        Register
      </button>
    
    </div>
    
  )
}
export default Main;
