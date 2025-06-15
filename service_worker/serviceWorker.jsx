// serviceWorker.jsx - React PWA style Service Worker registration and caching

const CACHE_NAME = 'tactixcore-cache-v1';
const ASSETS_TO_CACHE = [
  '/',
  '/index.html',
  '/script.js',
  '/style.css',
  '/config/config.ini',
  '/config/config.py',
];

self.addEventListener('install', (event) => {
  console.log('[ServiceWorker] Install');
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('[ServiceWorker] Caching all assets');
      return cache.addAll(ASSETS_TO_CACHE);
    })
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  console.log('[ServiceWorker] Activate');
  event.waitUntil(
    caches.keys().then((keyList) =>
      Promise.all(
        keyList.map((key) => {
          if (key !== CACHE_NAME) {
            console.log('[ServiceWorker] Removing old cache', key);
            return caches.delete(key);
          }
        })
      )
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', (event) => {
  console.log('[ServiceWorker] Fetch', event.request.url);
  event.respondWith(
    caches.match(event.request).then((response) => {
      return (
        response ||
        fetch(event.request).catch(() =>
          caches.match('/offline.html') // Optional offline fallback
        )
      );
    })
  );
});
