import React from 'react';

export default function OfflinePage() {
  return (
    <html>
      <head>
        <title>Offline - BetArena</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <style>{`
          * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
          }
          body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            color: #333;
          }
          .container {
            text-align: center;
            background: white;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            max-width: 500px;
          }
          .icon {
            font-size: 64px;
            margin-bottom: 20px;
          }
          h1 {
            font-size: 32px;
            margin-bottom: 10px;
            color: #333;
          }
          p {
            font-size: 16px;
            color: #666;
            line-height: 1.6;
            margin-bottom: 30px;
          }
          button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 6px;
            cursor: pointer;
            font-size: 16px;
            transition: transform 0.2s, box-shadow 0.2s;
          }
          button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
          }
          button:active {
            transform: translateY(0);
          }
        `}</style>
      </head>
      <body>
        <div className="container">
          <div className="icon">📡</div>
          <h1>You're Offline</h1>
          <p>
            It looks like you've lost your internet connection. Don't worry, you can still access some cached content.
          </p>
          <p style={{ fontSize: '14px', color: '#999' }}>
            Some features may be limited until your connection is restored.
          </p>
          <button onClick={() => window.location.reload()}>
            Try Again
          </button>
        </div>
      </body>
    </html>
  );
}
