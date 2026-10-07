# Fotograf Portfolio Website 📸

Eine moderne, responsive Portfolio-Website für professionelle Fotografen. Entwickelt mit HTML5, CSS3 und Vanilla JavaScript.

## ✨ Features

### Design & Layout
- **Modernes, minimalistisches Design** mit eleganter Typografie
- **Vollständig responsive** - optimiert für Desktop, Tablet und Mobile
- **Smooth Scrolling** für bessere Navigation
- **Scroll-Animationen** für dynamische Inhalte
- **Sticky Navigation** mit Scroll-Effekt

### Portfolio-Funktionen
- **Filterbares Portfolio** nach Kategorien (Portraits, Hochzeiten, Landschaften, Events)
- **Lightbox-Galerie** mit Bildnavigation
- **Keyboard-Navigation** (Pfeiltasten, ESC zum Schließen)
- **Touch-optimiert** für mobile Geräte
- **Lazy Loading** für optimale Performance

### Sektionen
1. **Hero Section** - Eindrucksvolle Willkommensseite mit Call-to-Action
2. **Über Mich** - Persönliche Vorstellung mit Statistiken
3. **Portfolio** - Filterbares Bildergalerie mit 9 Beispielbildern
4. **Leistungen** - Übersicht der angebotenen Services
5. **Kontakt** - Kontaktformular und Kontaktinformationen

## 🚀 Verwendung

### Lokale Ansicht
1. Öffnen Sie die `index.html` Datei in einem modernen Webbrowser
2. Oder verwenden Sie einen lokalen Webserver:
   ```bash
   # Mit Python 3
   python -m http.server 8000
   
   # Mit Node.js (http-server)
   npx http-server
   ```
3. Öffnen Sie `http://localhost:8000` in Ihrem Browser

### Live-Deployment
Die Seite kann auf verschiedenen Plattformen gehostet werden:
- **GitHub Pages** - Kostenlos für öffentliche Repositories
- **Netlify** - Einfaches Drag & Drop Deployment
- **Vercel** - Optimiert für statische Websites
- **Cloudflare Pages** - Schnelles globales CDN

## 🎨 Anpassung

### Persönliche Daten ändern
Öffnen Sie `index.html` und ändern Sie:
- **Name**: Suchen Sie nach "Max Mustermann" und ersetzen Sie ihn
- **Kontaktdaten**: In der Kontakt-Sektion (Email, Telefon, Standort)
- **Social Media Links**: Im Footer und Kontaktbereich

### Bilder ersetzen
**Eigene Bilder verwenden:**
1. Erstellen Sie einen `images` Ordner
2. Fügen Sie Ihre Fotos hinzu
3. Ersetzen Sie die Unsplash-URLs in `index.html`:
   ```html
   <!-- Vorher -->
   <img src="https://images.unsplash.com/..." alt="...">
   
   <!-- Nachher -->
   <img src="images/mein-foto.jpg" alt="...">
   ```

**Empfohlene Bildgrößen:**
- Hero-Hintergrundbild: 1920x1080px oder größer
- Portfolio-Bilder: 800x800px (quadratisch)
- About-Bild: 600x800px

### Farben ändern
Passen Sie die Farbvariablen in `styles.css` an:
```css
:root {
    --primary-color: #2c3e50;      /* Hauptfarbe */
    --secondary-color: #e74c3c;    /* Akzentfarbe */
    --accent-color: #f39c12;       /* Zusätzliche Akzentfarbe */
}
```

### Portfolio-Kategorien
In `index.html` können Sie Kategorien hinzufügen/ändern:
```html
<!-- Filter-Buttons -->
<button class="filter-btn" data-filter="ihre-kategorie">Ihre Kategorie</button>

<!-- Portfolio-Items -->
<div class="portfolio-item" data-category="ihre-kategorie">
    <!-- Inhalt -->
</div>
```

### Schriftarten ändern
Die Seite verwendet Google Fonts (Playfair Display + Poppins). 
Ändern Sie in `index.html` und `styles.css`:
```css
font-family: 'Ihre-Schriftart', sans-serif;
```

## 📱 Browser-Kompatibilität

Getestet und optimiert für:
- ✅ Chrome/Edge (neueste Versionen)
- ✅ Firefox (neueste Versionen)
- ✅ Safari (neueste Versionen)
- ✅ Mobile Browser (iOS Safari, Chrome Mobile)

## 🛠️ Technologie-Stack

- **HTML5** - Semantisches Markup
- **CSS3** - Grid, Flexbox, Animationen
- **JavaScript (ES6+)** - Vanilla JS, keine Dependencies
- **Google Fonts** - Playfair Display & Poppins
- **Unsplash** - Placeholder-Bilder (in Produktion ersetzen)

## 📋 Dateistruktur

```
portfolio-photographer/
├── index.html          # Hauptseite mit allen Sektionen
├── styles.css          # Alle Styles und responsive Design
├── script.js           # Interaktivität und Animationen
└── README.md           # Diese Datei
```

## 🎯 Performance-Tipps

1. **Bilder optimieren**: Verwenden Sie WebP-Format für bessere Kompression
2. **Lazy Loading**: Bereits implementiert für Portfolio-Bilder
3. **Caching**: Konfigurieren Sie Browser-Caching auf Ihrem Server
4. **CDN**: Nutzen Sie ein CDN für schnellere Ladezeiten weltweit
5. **Minification**: Minifizieren Sie CSS und JS für Produktion

## 📝 Kontaktformular

Das Kontaktformular zeigt aktuell nur eine Bestätigungsmeldung. 
Für echte Email-Funktionalität:

### Option 1: Backend-Service
```javascript
// In script.js - fetch zu Ihrem Backend
fetch('/api/contact', {
    method: 'POST',
    body: JSON.stringify(formData)
})
```

### Option 2: Email-Service (Formspree, EmailJS)
```html
<!-- Formspree Beispiel -->
<form action="https://formspree.io/f/ihre-form-id" method="POST">
```

### Option 3: Netlify Forms
```html
<!-- Netlify Forms -->
<form name="contact" method="POST" data-netlify="true">
```

## 🔒 SEO & Accessibility

- ✅ Semantisches HTML5
- ✅ Alt-Texte für alle Bilder
- ✅ ARIA-Labels für Links
- ✅ Meta-Descriptions
- ✅ Mobile-responsive
- ✅ Lighthouse-Score optimiert

## 📄 Lizenz

Dieses Template kann frei verwendet und angepasst werden.
Bei Verwendung wäre ein Link zurück willkommen, aber nicht erforderlich.

## 🤝 Support

Bei Fragen oder Problemen:
1. Überprüfen Sie die Browser-Konsole auf Fehler
2. Stellen Sie sicher, dass alle Dateien korrekt verlinkt sind
3. Testen Sie in einem anderen Browser

## 🎨 Weitere Anpassungen

**Neue Sektion hinzufügen:**
```html
<section id="neue-sektion" class="neue-sektion">
    <div class="container">
        <div class="section-header">
            <h2 class="section-title">Ihr Titel</h2>
            <div class="title-underline"></div>
        </div>
        <!-- Ihr Inhalt -->
    </div>
</section>
```

**Neue Animation hinzufügen:**
```css
@keyframes ihre-animation {
    from { /* Start */ }
    to { /* Ende */ }
}
```

---

**Viel Erfolg mit Ihrer Portfolio-Website! 📸✨**
