import { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [status, setStatus] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchStatus = async () => {
      try {
        // Fetching from the FastAPI backend
        const response = await fetch('http://localhost:8000/api/data');
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setStatus(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchStatus();
  }, []);

  return (
    <div className="container">
      <div className="cyber-card">
        <h1 className="cyber-glitch" data-text="SYSTEM STATUS">SYSTEM STATUS</h1>

        <div className="terminal-window">
          <div className="terminal-header">
            <span className="dot red"></span>
            <span className="dot yellow"></span>
            <span className="dot green"></span>
            <span className="title">root@brain-vault:~# curl /api/data</span>
          </div>

          <div className="terminal-body">
            {loading && <p className="blink">Initializing connection sequence...</p>}

            {error && (
              <p className="error">
                [ERROR] Connection Refused<br />
                {error}<br />
                &gt; Check if FastAPI server is running on port 8000
              </p>
            )}

            {status && (
              <div className="success">
                <p>&gt; Connection Established.</p>
                <p>&gt; Message: <span className="highlight">{status.message}</span></p>
                <p>&gt; Status: <span className="status-ok">{status.status}</span></p>
              </div>
            )}

            <div className="cursor">_</div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
