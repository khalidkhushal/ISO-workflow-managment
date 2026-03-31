import React, { useState } from 'react';
import Login from './components/auth/Login';
import Register from './components/auth/Register';
import Dashboard from './components/Dashboard';
import useAuth from './hooks/useAuth';
import Loading from './components/common/Loading';

function App() {
  const { user, loading, login, logout } = useAuth();
  const [currentView, setCurrentView] = useState('login');

  if (loading) {
    return <Loading message="Checking authentication..." />;
  }

  const handleLogin = (userData) => {
    login(userData);
    setCurrentView('dashboard');
  };

  const handleRegister = () => {
    alert('Registration successful! Please login.');
    setCurrentView('login');
  };

  const handleLogout = () => {
    logout();
    setCurrentView('login');
  };

  return (
    <div className="container">
      {currentView === 'login' && (
        <Login
          onLogin={handleLogin}
          onSwitchToRegister={() => setCurrentView('register')}
        />
      )}

      {currentView === 'register' && (
        <Register
          onRegister={handleRegister}
          onSwitchToLogin={() => setCurrentView('login')}
        />
      )}

      {currentView === 'dashboard' && user && (
        <Dashboard
          user={user}
          onLogout={handleLogout}
        />
      )}
    </div>
  );
}

export default App;