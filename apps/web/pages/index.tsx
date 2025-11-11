import { useState, useEffect } from 'react';
import Head from 'next/head';
import styles from '@/styles/Home.module.css';

export default function Home() {
  const [apiHealth, setApiHealth] = useState<{ ok: boolean; service: string } | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/backend/healthz')
      .then(res => res.json())
      .then(data => {
        setApiHealth(data);
        setLoading(false);
      })
      .catch(err => {
        console.error('Failed to fetch API health:', err);
        setLoading(false);
      });
  }, []);

  return (
    <>
      <Head>
        <title>BetArena - Sports Betting Suggestions</title>
        <meta name="description" content="Sports betting suggestions app" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </Head>
      <main className={styles.main}>
        <div className={styles.container}>
          <h1 className={styles.title}>BetArena</h1>
          <p className={styles.description}>
            Sports Betting Suggestions Platform
          </p>
          
          <div className={styles.status}>
            <h2>System Status</h2>
            {loading ? (
              <p>Checking services...</p>
            ) : (
              <div className={styles.healthCheck}>
                <div className={styles.service}>
                  <span className={styles.serviceName}>API Service:</span>
                  <span className={apiHealth?.ok ? styles.online : styles.offline}>
                    {apiHealth?.ok ? '✓ Online' : '✗ Offline'}
                  </span>
                </div>
              </div>
            )}
          </div>
        </div>
      </main>
    </>
  );
}
