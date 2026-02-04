import { useState } from 'react';
import { Lock } from 'lucide-react';

export default function ShieldLearnUI() {
  const [showLogin, setShowLogin] = useState(false);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [rememberMe, setRememberMe] = useState(false);

  const handleLogin = () => {
    console.log('Login attempt:', { username, password, rememberMe });
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleLogin();
    }
  };

  if (!showLogin) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-indigo-200 via-purple-200 to-blue-200 flex items-center justify-center p-8">
        <div className="text-center">
          {/* Shield Logo */}
          <div className="mb-8 flex justify-center">
            <svg width="400" height="400" viewBox="0 0 400 400" className="drop-shadow-lg">
              {/* Outer Shield */}
              <path d="M200 50 L350 120 L350 250 Q350 320 200 370 Q50 320 50 250 L50 120 Z" 
                    fill="none" stroke="#64748b" strokeWidth="8" opacity="0.6"/>
              
              {/* Middle Shield */}
              <path d="M200 70 L330 130 L330 240 Q330 300 200 345 Q70 300 70 240 L70 130 Z" 
                    fill="none" stroke="#64748b" strokeWidth="8" opacity="0.7"/>
              
              {/* Inner Shield */}
              <path d="M200 90 L310 140 L310 230 Q310 280 200 320 Q90 280 90 230 L90 140 Z" 
                    fill="none" stroke="#64748b" strokeWidth="8" opacity="0.8"/>
              
              {/* Person Icon */}
              <circle cx="200" cy="165" r="20" fill="#64748b"/>
              <path d="M200 190 Q180 190 170 200 L170 220 L230 220 L230 200 Q220 190 200 190 Z" fill="#64748b"/>
              
              {/* Laptop */}
              <rect x="175" y="200" width="50" height="30" rx="2" fill="#64748b"/>
              <rect x="170" y="230" width="60" height="4" rx="2" fill="#64748b"/>
              
              {/* Text SHIELD */}
              <text x="200" y="270" fontFamily="Arial, sans-serif" fontSize="48" fontWeight="bold" 
                    fill="#64748b" textAnchor="middle">SHIELD</text>
              
              {/* Text LEARN */}
              <text x="200" y="300" fontFamily="Arial, sans-serif" fontSize="24" 
                    fill="#64748b" textAnchor="middle" letterSpacing="4">LEARN</text>
            </svg>
          </div>

          {/* Welcome Text */}
          <h1 className="text-4xl font-bold text-white mb-4 tracking-wide drop-shadow-md">
            WELCOME TO SHIELDLEARN!
          </h1>
          
          <p className="text-2xl text-white mb-8 drop-shadow">
            click on the lock to get started
          </p>

          {/* Lock Button */}
          <button 
            onClick={() => setShowLogin(true)}
            className="bg-gradient-to-br from-amber-400 to-amber-600 hover:from-amber-500 hover:to-amber-700 rounded-full p-8 shadow-2xl transition-transform hover:scale-110 active:scale-95"
          >
            <Lock size={64} className="text-slate-700" />
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-200 via-purple-200 to-blue-200 flex items-center justify-center p-8">
      <div className="bg-white/80 backdrop-blur-sm rounded-lg shadow-2xl p-8 w-full max-w-md">
        {/* Small Shield Logo */}
        <div className="flex justify-end mb-4">
          <svg width="60" height="60" viewBox="0 0 100 100">
            <path d="M50 10 L85 25 L85 55 Q85 70 50 85 Q15 70 15 55 L15 25 Z" 
                  fill="none" stroke="#64748b" strokeWidth="3"/>
            <text x="50" y="60" fontFamily="Arial" fontSize="20" fill="#64748b" 
                  textAnchor="middle" fontWeight="bold">SHIELD</text>
          </svg>
        </div>

        {/* Lock Icon */}
        <div className="flex justify-center mb-6">
          <div className="bg-gradient-to-br from-slate-600 to-slate-800 rounded-full p-8">
            <Lock size={64} className="text-amber-400" />
          </div>
        </div>

        {/* Login Inputs */}
        <div className="space-y-4">
          <div>
            <input
              type="text"
              placeholder="enter your username here:"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              onKeyPress={handleKeyPress}
              className="w-full px-4 py-3 border-2 border-gray-300 rounded-lg focus:outline-none focus:border-blue-500 bg-white"
            />
          </div>

          <div>
            <input
              type="password"
              placeholder="enter your password here:"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              onKeyPress={handleKeyPress}
              className="w-full px-4 py-3 border-2 border-gray-300 rounded-lg focus:outline-none focus:border-blue-500 bg-white"
            />
          </div>

          <div className="flex items-center justify-between text-sm">
            <label className="flex items-center gap-2 cursor-pointer">
              <input
                type="checkbox"
                checked={rememberMe}
                onChange={(e) => setRememberMe(e.target.checked)}
                className="w-4 h-4"
              />
              <span className="text-gray-700">remember me?</span>
            </label>
            <a href="#" className="text-red-500 hover:text-red-600">
              forgot username or password?
            </a>
          </div>

          <button
            onClick={handleLogin}
            className="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 rounded-full text-xl transition-colors shadow-lg"
          >
            LOGIN
          </button>
        </div>

        {/* Register Link */}
        <div className="text-center mt-6">
          <a href="#" className="text-blue-600 hover:text-blue-700 font-semibold">
            No account? Register here!
          </a>
        </div>
      </div>
    </div>
  );
}