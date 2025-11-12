# Build Error Resolution Guide

## Changes Made to Fix PWA Configuration

### 1. **Fixed next.config.js**
   - Changed `register: true` to `register: false` 
   - Removed `sw: 'service-worker.js'` line
   - **Reason**: Conflicts between next-pwa's automatic registration and manual registration in _app.tsx

### 2. **Service Worker Registration**
   - Manual registration in `pages/_app.tsx` handles the custom service worker
   - Located at `/public/service-worker.js`

## Troubleshooting Build Errors

### If you see errors related to service worker:

1. **Clear cache and reinstall dependencies:**
   ```bash
   cd apps/web
   rm -rf node_modules package-lock.json .next
   npm install
   npm run build
   ```

2. **Check Node.js version:**
   ```bash
   node --version  # Should be v18+
   npm --version   # Should be v9+
   ```

3. **Build with verbose output:**
   ```bash
   npm run build -- --debug
   ```

### If you see HTTPS/offline errors:

- PWA features require HTTPS in production, but work with HTTP on localhost
- Offline functionality is tested in Chrome DevTools > Application > Service Workers

### If next-pwa conflicts persist:

Alternative: Use Next.js's native Service Worker support instead of next-pwa:

1. Move service-worker.js to `public/` directory (already done ✓)
2. Register manually in _app.tsx (already done ✓)
3. Consider removing next-pwa dependency if it causes conflicts:
   ```bash
   npm uninstall next-pwa
   ```

## Verified PWA Assets

✓ All icon files created:
- `/public/icons/icon-{192,256,384,512}x{192,256,384,512}.png`
- `/public/icons/icon-maskable-{192,512}x{192,512}.png`

✓ Favicon files created:
- `/public/favicon.ico`
- `/public/favicon-{16,32}x{16,32}.png`

✓ Screenshots created:
- `/public/screenshots/screenshot-{540x720,1280x720}.png`

✓ Configuration files in place:
- `manifest.json` ✓
- `offline.html` ✓
- `offline.tsx` ✓
- `service-worker.js` ✓
- `next.config.js` (fixed) ✓
- `_app.tsx` ✓

## Next Steps

1. Run: `cd apps/web && npm install`
2. Run: `npm run build`
3. Run: `npm start`
4. Test in Chrome DevTools: F12 > Application > Service Workers

If errors persist, provide the specific error message from the build output.
