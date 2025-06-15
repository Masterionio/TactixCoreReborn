// service_worker.js — TactixCore Reborn Service Worker

const CACHE_NAME = 'tactixcore-cache-v1';
const ASSETS_TO_CACHE = [
  '/',
  '/index.html',
  '/style.css',
  '/script.js',
  '/config/config.ini',
  '/config/config.py',
  '/offline.html'  // Optional offline fallback page, create if needed
];

// Install event — cache core assets
self.addEventListener('install', (event) => {
  console.log('[ServiceWorker] Installing and caching assets');
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS_TO_CACHE);
    }).then(() => self.skipWaiting())
  );
});

// Activate event — clean old caches
self.addEventListener('activate', (event) => {
  console.log('[ServiceWorker] Activating and cleaning old caches');
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((name) => {
          if (name !== CACHE_NAME) {
            console.log('[ServiceWorker] Deleting old cache:', name);
            return caches.delete(name);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// Fetch event — respond with cache first, fallback to network
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      if (cachedResponse) {
        // Serve from cache
        return cachedResponse;
      }
      // Fetch from network and cache dynamically
      return fetch(event.request).then((networkResponse) => {
        // Check valid response
        if (!networkResponse || networkResponse.status !== 200 || networkResponse.type !== 'basic') {
          return networkResponse;
        }
        // Clone response to cache it
        const responseToCache = networkResponse.clone();
        caches.open(CACHE_NAME).then((cache) => {
          cache.put(event.request, responseToCache);
        });
        return networkResponse;
      }).catch(() => {
        // If offline and request fails, show offline fallback for navigations
        if (event.request.mode === 'navigate') {
          return caches.match('/offline.html');
        }
      });
    })
  );
});
