# Khalida Educational Foundation Website

A modern, professional foundation website built to honor a legacy of educational dedication. This site showcases the foundation's mission to empower children through quality education and skill-based learning programs.

## 🌟 Features

- **Modern Design**: Clean, professional interface with warm, trustworthy color palette
- **Fully Responsive**: Mobile-first design that looks great on all devices
- **Interactive Elements**: Animated counters, smooth scrolling, modal gallery
- **AI Initiative Section**: Featured program highlighting cutting-edge AI education for kids
- **Complete Functionality**: Contact forms, donation CTAs, volunteer sign-up
- **Accessibility**: High contrast, readable typography, semantic HTML
- **Fast Loading**: Optimized images and minimal dependencies

## 📋 Site Structure

### Single-Page Scrolling Website

1. **Hero Section** - Foundation introduction with primary CTAs
2. **About** - Tribute to founder's mother and foundation mission
3. **Programs & Initiatives** - 5 core programs with detailed descriptions
4. **AI Initiative** - Future Leaders Program: AI for Young Minds
5. **Impact** - Statistics and measurable outcomes
6. **Get Involved** - Donation, volunteer, and partnership opportunities
7. **Gallery** - Visual showcase of programs and events
8. **Testimonials** - Stories from beneficiaries and supporters
9. **Contact** - Contact form and information
10. **Footer** - Quick links, newsletter signup, social media

## 🎨 Design & Branding

### Color Palette

- **Primary**: Navy Blue (#1a3a52) - Trust and professionalism
- **Secondary**: Teal (#1D809F) - Education and growth
- **Accent**: Warm Gold (#ecb807) - Hope and warmth
- **AI Section**: Electric Blue & Cyber Lime - Innovation and future

### Typography

- **Headings**: Poppins (Modern, professional)
- **Body**: Inter (Readable, accessible)

## 🚀 Quick Start - Local Setup

### Prerequisites

- A modern web browser (Chrome, Firefox, Safari, Edge)
- A code editor (VS Code recommended)
- Basic understanding of HTML/CSS/JavaScript

### Installation Steps

1. **Clone or Download the Repository**

   ```bash
   git clone https://github.com/masimriaz/khalida-foundation.git
   cd khalida-foundation
   ```

2. **Project Structure**

   ```
   khalida-foundation/
   ├── index.html          # Main HTML file
   ├── css/
   │   ├── styles.css      # Bootstrap + base styles
   │   └── custom.css      # Custom foundation styles
   ├── js/
   │   └── scripts.js      # Interactive functionality
   ├── assets/
   │   ├── favicon.ico
   │   └── img/            # Images folder
   │       ├── bg-masthead.jpg
   │       ├── ai-poster-1.jpg
   │       ├── course-outline.jpg
   │       └── gallery-*.jpg
   └── README.md
   ```

3. **Add Your Images**

   Place your images in the `assets/img/` folder with these names:

   - `bg-masthead.jpg` - Hero background (1920x1080px recommended)
   - `ai-poster-1.jpg` - AI program poster
   - `course-outline.jpg` - Course curriculum visual
   - `gallery-1.jpg` to `gallery-5.jpg` - Gallery images

   **Tip**: You can use any image format (.jpg, .png, .webp) by updating the file extensions in index.html

4. **Run Locally**

   **Option A: Using VS Code Live Server**

   - Install "Live Server" extension in VS Code
   - Right-click on `index.html`
   - Select "Open with Live Server"
   - Site will open at `http://localhost:5500`

   **Option B: Using Python**

   ```bash
   # Python 3
   python -m http.server 8000

   # Then open browser to http://localhost:8000
   ```

   **Option C: Using Node.js**

   ```bash
   npx http-server

   # Then open browser to http://localhost:8080
   ```

   **Option D: Direct File Access**

   - Simply double-click `index.html`
   - Opens directly in your default browser

## 🌐 Deployment to GitHub Pages

### Step 1: Push to GitHub

If you haven't already pushed your code:

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit changes
git commit -m "Initial commit - Khalida Foundation website"

# Add remote repository
git remote add origin https://github.com/masimriaz/khalida-foundation.git

# Push to GitHub
git push -u origin main
```

### Step 2: Enable GitHub Pages

1. Go to your repository on GitHub: `https://github.com/masimriaz/khalida-foundation`
2. Click on **Settings** (top right)
3. Scroll down to **Pages** section (left sidebar)
4. Under **Source**, select:
   - Branch: `main`
   - Folder: `/ (root)`
5. Click **Save**
6. Wait 1-2 minutes for deployment
7. Your site will be live at: `https://masimriaz.github.io/khalida-foundation/`

### Step 3: Custom Domain (Optional)

To use a custom domain like `www.khalidafoundation.org`:

1. Buy a domain from a registrar (GoDaddy, Namecheap, etc.)
2. In GitHub Pages settings, add your custom domain
3. In your domain registrar's DNS settings, add these records:

   ```
   Type: A
   Name: @
   Value: 185.199.108.153

   Type: A
   Name: @
   Value: 185.199.109.153

   Type: A
   Name: @
   Value: 185.199.110.153

   Type: A
   Name: @
   Value: 185.199.111.153

   Type: CNAME
   Name: www
   Value: masimriaz.github.io
   ```

4. Wait 24-48 hours for DNS propagation
5. Enable HTTPS in GitHub Pages settings

## 📝 Customization Guide

### Update Content

1. **Foundation Name**: Search and replace "Khalida Educational Foundation" in `index.html`
2. **Contact Information**: Edit the contact section in `index.html` (lines ~450-500)
3. **Social Media Links**: Update URLs in footer and contact sections
4. **Mission Statement**: Edit hero section and about section content

### Replace Images

All images are in `assets/img/`. Simply replace files with the same names:

```
assets/img/
├── bg-masthead.jpg       # Hero background
├── ai-poster-1.jpg       # AI program poster
├── course-outline.jpg    # Course details
├── gallery-1.jpg         # Scholarship ceremony
├── gallery-2.jpg         # Classroom
├── gallery-3.jpg         # Teacher training
├── gallery-4.jpg         # Community event
└── gallery-5.jpg         # Skills workshop
```

### Modify Colors

Edit `css/custom.css` at the top (lines 1-30):

```css
:root {
  --foundation-navy: #1a3a52; /* Main color */
  --warm-accent: #d4a574; /* Accent color */
  --warm-gold: #ecb807; /* CTA color */
  /* Modify these values */
}
```

### Connect Forms to Backend

The contact form currently shows an alert. To connect to a real backend:

Edit `js/scripts.js` (around line 140):

```javascript
// Replace the alert with actual form submission:
fetch("YOUR_BACKEND_URL/api/contact", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(data),
})
  .then((response) => response.json())
  .then((data) => {
    alert("Thank you! Your message has been sent.");
    contactForm.reset();
  })
  .catch((error) => {
    alert("Sorry, there was an error. Please try again.");
  });
```

**Recommended Form Services:**

- **Formspree**: https://formspree.io (Free tier available)
- **Netlify Forms**: If you host on Netlify
- **EmailJS**: https://www.emailjs.com (Free tier available)

## 🛠️ Technologies Used

- **HTML5** - Semantic markup
- **CSS3** - Custom styling with CSS variables
- **Bootstrap 5** - Responsive grid and components
- **JavaScript (ES6)** - Interactive features
- **Font Awesome** - Icons
- **Google Fonts** - Poppins & Inter fonts

## 📱 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## ⚡ Performance Optimization

Current optimizations:

- Lazy loading ready (uncomment in HTML if needed)
- Optimized CSS delivery
- Minimal JavaScript dependencies
- CSS animations use transform/opacity for 60fps

**Additional Optimizations**:

1. Compress images using TinyPNG or ImageOptim
2. Use WebP format for images
3. Enable Cloudflare CDN if using custom domain
4. Minify CSS/JS for production (optional)

## 🔒 Security Best Practices

- All external resources use HTTPS
- No sensitive data in client-side code
- Forms should validate on backend (when connected)
- Regular updates of Bootstrap and dependencies

## 📄 License

This project is open source and available for use by the Khalida Educational Foundation.

## 🤝 Contributing

To contribute improvements:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -m 'Add improvement'`)
4. Push to branch (`git push origin feature/improvement`)
5. Open a Pull Request

## 📞 Support

For technical issues or questions:

- Email: info@khalidafoundation.org
- GitHub Issues: https://github.com/masimriaz/khalida-foundation/issues

## 🎯 Roadmap

Future enhancements:

- [ ] Blog/News section
- [ ] Donation payment gateway integration (Stripe, PayPal)
- [ ] Event calendar
- [ ] Volunteer portal/dashboard
- [ ] Multi-language support
- [ ] Student success stories database
- [ ] Annual report downloads
- [ ] Live chat support

---

## Quick Reference: Updating Common Elements

### Change Hero Image

Replace `assets/img/bg-masthead.jpg` with your image

### Update Statistics

Edit `index.html` around line 300, modify `data-target` values:

```html
<div class="stat-number" data-target="1250">0</div>
```

### Add Gallery Image

1. Add image to `assets/img/`
2. Copy a gallery-item div in `index.html`
3. Update `data-img`, `data-title`, and `src` attributes

### Modify Programs

Edit the program cards section (around line 150-250 in `index.html`)

---

**Built with ❤️ for the Khalida Educational Foundation**

_Empowering Futures Through Education_
